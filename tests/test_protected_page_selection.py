import json
import shutil
import subprocess
from pathlib import Path

import pytest


HELPER = Path(__file__).resolve().parents[1] / "tools/manual_publisher/protected_page_selection.ps1"
POWERSHELL = shutil.which("powershell") or shutil.which("pwsh")
pytestmark = pytest.mark.skipif(POWERSHELL is None, reason="PowerShell is needed to test build selection preferences")


def run_selection_script(tmp_path: Path, body: str):
    script = tmp_path / "check_selection.ps1"
    helper_path = str(HELPER).replace("'", "''")
    script.write_text(
        "param([string]$ScratchRoot)\n$ErrorActionPreference = 'Stop'\n"
        + f". '{helper_path}'\n"
        + "$stateFile = Join-Path $ScratchRoot 'preferences/selection.json'\n"
        + "$buildRoot = Join-Path $ScratchRoot 'build'\n"
        + body,
        encoding="utf-8-sig",
    )
    result = subprocess.run(
        [POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", str(script), str(tmp_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return json.loads(result.stdout)


def test_remembers_checked_unchecked_and_empty_selection(tmp_path: Path):
    result = run_selection_script(tmp_path, """
$checked = 'V. 1.0/IT/FlexiBowl_manual/PLUG-IN/page.html'
$unchecked = 'V. 1.0/IT/FlexiBowl_manual/MANUTENZIONE/02_straordinaria.html'
Save-ProtectedPageSelection -StateFile $stateFile -Selections @{ $checked = $true; $unchecked = $false }
$saved = Get-ProtectedPageSelection -StateFile $stateFile
$initial = @(
    (Get-ProtectedPageCheckedState -OutputPath $checked -DefaultChecked $false -Selections $saved -BuildRoot $buildRoot),
    (Get-ProtectedPageCheckedState -OutputPath $unchecked -DefaultChecked $true -Selections $saved -BuildRoot $buildRoot)
)
$saved[$checked] = $false
Save-ProtectedPageSelection -StateFile $stateFile -Selections $saved
$reopened = Get-ProtectedPageSelection -StateFile $stateFile
@{ Initial = $initial; AllUnchecked = @($reopened.Values | Where-Object { $_ }).Count -eq 0 } | ConvertTo-Json
""")
    assert result == {"Initial": [True, False], "AllUnchecked": True}


def test_single_language_changes_preserve_other_language_choices(tmp_path: Path):
    result = run_selection_script(tmp_path, """
$italian = 'V. 1.0/IT/FlexiBowl_manual/page.html'
$english = 'V. 1.0/EN/FlexiBowl_manual/page.html'
Save-ProtectedPageSelection -StateFile $stateFile -Selections @{ $italian = $true; $english = $true }
$singleLanguage = Get-ProtectedPageSelection -StateFile $stateFile
$singleLanguage[$italian] = $false
Save-ProtectedPageSelection -StateFile $stateFile -Selections $singleLanguage
$allLanguages = Get-ProtectedPageSelection -StateFile $stateFile
@{ Italian = $allLanguages[$italian]; English = $allLanguages[$english] } | ConvertTo-Json
""")
    assert result == {"Italian": False, "English": True}


def test_first_open_uses_last_build_then_saved_choices_take_precedence(tmp_path: Path):
    result = run_selection_script(tmp_path, """
[void][System.IO.Directory]::CreateDirectory($buildRoot)
[System.IO.File]::WriteAllText((Join-Path $buildRoot 'protected.html'), '<meta name="ars-protected-page" content="encrypted">')
[System.IO.File]::WriteAllText((Join-Path $buildRoot 'public.html'), '<html><body>Public</body></html>')
$empty = Get-ProtectedPageSelection -StateFile $stateFile
$first = @(
    (Get-ProtectedPageCheckedState -OutputPath 'protected.html' -DefaultChecked $false -Selections $empty -BuildRoot $buildRoot),
    (Get-ProtectedPageCheckedState -OutputPath 'public.html' -DefaultChecked $true -Selections $empty -BuildRoot $buildRoot),
    (Get-ProtectedPageCheckedState -OutputPath 'new.html' -DefaultChecked $true -Selections $empty -BuildRoot $buildRoot)
)
Save-ProtectedPageSelection -StateFile $stateFile -Selections @{ 'protected.html' = $false; 'public.html' = $true }
$saved = Get-ProtectedPageSelection -StateFile $stateFile
$next = @(
    (Get-ProtectedPageCheckedState -OutputPath 'protected.html' -DefaultChecked $true -Selections $saved -BuildRoot $buildRoot),
    (Get-ProtectedPageCheckedState -OutputPath 'public.html' -DefaultChecked $false -Selections $saved -BuildRoot $buildRoot),
    (Get-ProtectedPageCheckedState -OutputPath 'new.html' -DefaultChecked $true -Selections $saved -BuildRoot $buildRoot)
)
@{ First = $first; Next = $next } | ConvertTo-Json
""")
    assert result == {"First": [True, False, True], "Next": [False, True, False]}


def test_invalid_preferences_fall_back_without_stopping_build(tmp_path: Path):
    result = run_selection_script(tmp_path, """
[void][System.IO.Directory]::CreateDirectory((Split-Path -Parent $stateFile))
[System.IO.File]::WriteAllText($stateFile, 'broken json')
$invalid = Get-ProtectedPageSelection -StateFile $stateFile
[System.IO.File]::WriteAllText($stateFile, '{"Version":1,"Pages":{"valid":false,"invalid":"true"}}')
$filtered = Get-ProtectedPageSelection -StateFile $stateFile
@{ InvalidCount = $invalid.Count; FilteredCount = $filtered.Count; RememberedFalse = $filtered['valid'] } | ConvertTo-Json
""")
    assert result == {"InvalidCount": 0, "FilteredCount": 1, "RememberedFalse": False}
