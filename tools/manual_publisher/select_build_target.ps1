$ErrorActionPreference = 'Stop'

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$sourceRoot = Join-Path $repoRoot 'sources'
$buildRoot = Join-Path $repoRoot 'build'
$selectionStateFile = Join-Path $repoRoot '.build_cache/protected-page-selection.json'
. (Join-Path $PSScriptRoot 'protected_page_selection.ps1')

function Get-VersionSortKey {
    param([string]$Label)

    $numbers = [regex]::Matches($Label, '\d+') | ForEach-Object { [int]$_.Value }
    return ,@($numbers, $Label.ToLowerInvariant())
}

function Get-SortedVersions {
    param([string]$Root)

    $versions = Get-ChildItem -LiteralPath $Root -Directory |
        Where-Object { $_.Name -notlike '_*' } |
        Select-Object -ExpandProperty Name

    return $versions | Sort-Object {
        $parts = [regex]::Matches($_, '\d+') | ForEach-Object { '{0:D8}' -f [int]$_.Value }
        (@($parts) -join '.') + '|' + $_.ToLowerInvariant()
    } -Descending
}

function Get-SortedLanguages {
    param([string]$VersionPath)

    $preferredOrder = @{
        'IT' = 0
        'EN' = 1
        'FR' = 2
        'DE' = 3
        'ES' = 4
    }

    return Get-ChildItem -LiteralPath $VersionPath -Directory |
        Where-Object { $_.Name -notlike '_*' } |
        Select-Object -ExpandProperty Name |
        Sort-Object {
            $code = $_.ToUpperInvariant()
            if ($preferredOrder.ContainsKey($code)) {
                '{0:D2}|{1}' -f $preferredOrder[$code], $code
            } else {
                '99|' + $code
            }
        }
}

function Get-MarkdownTitle {
    param([string]$Path)

    $heading = Get-Content -LiteralPath $Path -Encoding UTF8 -TotalCount 60 |
        Where-Object { $_ -match '^\s{0,3}#{1,6}\s+' } |
        Select-Object -First 1

    if ([string]::IsNullOrWhiteSpace($heading)) {
        return [System.IO.Path]::GetFileNameWithoutExtension($Path)
    }

    $title = $heading -replace '^\s{0,3}#{1,6}\s+', ''
    $title = $title -replace '[#*_`]', ''
    $title = $title -replace '<[^>]+>', ''
    $title = $title -replace '\{[^}]+\}', ''
    $title = $title.Trim()

    if ([string]::IsNullOrWhiteSpace($title)) {
        return [System.IO.Path]::GetFileNameWithoutExtension($Path)
    }

    return $title
}

function Get-SourcePageCandidates {
    param(
        [string]$TargetVersion,
        [string]$TargetLanguage
    )

    $candidates = New-Object System.Collections.Generic.List[object]
    $versionsToScan = @()

    if (-not [string]::IsNullOrWhiteSpace($TargetVersion)) {
        $versionsToScan = @($TargetVersion)
    } else {
        $versionsToScan = @(Get-SortedVersions -Root $sourceRoot)
    }

    foreach ($version in $versionsToScan) {
        $versionPath = Join-Path $sourceRoot $version
        if (-not (Test-Path -LiteralPath $versionPath)) {
            continue
        }

        $languagesToScan = @()
        if (-not [string]::IsNullOrWhiteSpace($TargetLanguage)) {
            $languagesToScan = @($TargetLanguage)
        } else {
            $languagesToScan = @(Get-SortedLanguages -VersionPath $versionPath)
        }

        foreach ($language in $languagesToScan) {
            $languagePath = Join-Path $versionPath $language
            if (-not (Test-Path -LiteralPath $languagePath)) {
                continue
            }

            Get-ChildItem -LiteralPath $languagePath -Recurse -File -Filter '*.md' |
                Where-Object { $_.Name -ne 'index.md' -and $_.FullName -like "*\FlexiBowl_manual\*" } |
                ForEach-Object {
                    $relativeMarkdown = $_.FullName.Substring($languagePath.Length).TrimStart('\', '/')
                    $relativeMarkdown = $relativeMarkdown -replace '\\', '/'
                    $relativeHtml = [regex]::Replace($relativeMarkdown, '\.md$', '.html', 'IgnoreCase')
                    $outputPath = (($version, $language, $relativeHtml) -join '/') -replace '\\', '/'
                    $title = Get-MarkdownTitle -Path $_.FullName
                    $defaultChecked = $relativeMarkdown -match '^FlexiBowl_manual/MANUTENZIONE/02'
                    $label = '{0} / {1} / {2}  [{3}]' -f $version, $language, $title, $relativeMarkdown

                    $candidates.Add([pscustomobject]@{
                        Label            = $label
                        OutputPath       = $outputPath
                        IsDefaultChecked = $defaultChecked
                    }) | Out-Null
                }
        }
    }

    return $candidates | Sort-Object Label
}

function Show-ProtectedPageDialog {
    param(
        [string]$TargetVersion,
        [string]$TargetLanguage
    )

    $candidates = @(Get-SourcePageCandidates -TargetVersion $TargetVersion -TargetLanguage $TargetLanguage)
    if ($candidates.Count -eq 0) {
        return [pscustomobject]@{
            Cancelled = $false
            Pages     = @()
        }
    }

    $candidateByLabel = @{}
    $defaultByLabel = @{}
    $rememberedSelections = Get-ProtectedPageSelection -StateFile $selectionStateFile
    foreach ($candidate in $candidates) {
        $candidateByLabel[[string]$candidate.Label] = [string]$candidate.OutputPath
        $defaultByLabel[[string]$candidate.Label] = [bool]$candidate.IsDefaultChecked
    }

    $protectedForm = New-Object System.Windows.Forms.Form
    $protectedForm.Text = 'Pagine da cifrare'
    $protectedForm.StartPosition = 'CenterScreen'
    $protectedForm.FormBorderStyle = 'FixedDialog'
    $protectedForm.MaximizeBox = $false
    $protectedForm.MinimizeBox = $false
    $protectedForm.ClientSize = New-Object System.Drawing.Size(860, 560)
    $protectedForm.Font = New-Object System.Drawing.Font('Segoe UI', 9)
    $protectedForm.Topmost = $true

    $protectedTitle = New-Object System.Windows.Forms.Label
    $protectedTitle.Text = 'Scegli le pagine da cifrare'
    $protectedTitle.Location = New-Object System.Drawing.Point(20, 18)
    $protectedTitle.Size = New-Object System.Drawing.Size(320, 24)
    $protectedTitle.Font = New-Object System.Drawing.Font('Segoe UI Semibold', 11)
    $protectedForm.Controls.Add($protectedTitle)

    $protectedInfo = New-Object System.Windows.Forms.Label
    $protectedInfo.Text = 'Le pagine selezionate saranno protette con password ArS2026!. Le spunte e le deselezioni vengono ricordate alla prossima apertura.'
    $protectedInfo.Location = New-Object System.Drawing.Point(20, 48)
    $protectedInfo.Size = New-Object System.Drawing.Size(805, 38)
    $protectedForm.Controls.Add($protectedInfo)

    $checkedList = New-Object System.Windows.Forms.CheckedListBox
    $checkedList.Location = New-Object System.Drawing.Point(20, 94)
    $checkedList.Size = New-Object System.Drawing.Size(820, 360)
    $checkedList.CheckOnClick = $true
    $checkedList.HorizontalScrollbar = $true
    foreach ($candidate in $candidates) {
        $isChecked = Get-ProtectedPageCheckedState -OutputPath $candidate.OutputPath `
            -DefaultChecked $candidate.IsDefaultChecked -Selections $rememberedSelections -BuildRoot $buildRoot
        [void]$checkedList.Items.Add([string]$candidate.Label, $isChecked)
    }
    $protectedForm.Controls.Add($checkedList)

    $selectDefaultButton = New-Object System.Windows.Forms.Button
    $selectDefaultButton.Text = 'Solo straordinaria'
    $selectDefaultButton.Location = New-Object System.Drawing.Point(20, 468)
    $selectDefaultButton.Size = New-Object System.Drawing.Size(130, 30)
    $selectDefaultButton.Add_Click({
        for ($i = 0; $i -lt $checkedList.Items.Count; $i++) {
            $label = [string]$checkedList.Items[$i]
            $checkedList.SetItemChecked($i, [bool]$defaultByLabel[$label])
        }
    })
    $protectedForm.Controls.Add($selectDefaultButton)

    $selectAllButton = New-Object System.Windows.Forms.Button
    $selectAllButton.Text = 'Seleziona tutto'
    $selectAllButton.Location = New-Object System.Drawing.Point(158, 468)
    $selectAllButton.Size = New-Object System.Drawing.Size(120, 30)
    $selectAllButton.Add_Click({
        for ($i = 0; $i -lt $checkedList.Items.Count; $i++) {
            $checkedList.SetItemChecked($i, $true)
        }
    })
    $protectedForm.Controls.Add($selectAllButton)

    $clearButton = New-Object System.Windows.Forms.Button
    $clearButton.Text = 'Deseleziona tutto'
    $clearButton.Location = New-Object System.Drawing.Point(286, 468)
    $clearButton.Size = New-Object System.Drawing.Size(130, 30)
    $clearButton.Add_Click({
        for ($i = 0; $i -lt $checkedList.Items.Count; $i++) {
            $checkedList.SetItemChecked($i, $false)
        }
    })
    $protectedForm.Controls.Add($clearButton)

    $continueButton = New-Object System.Windows.Forms.Button
    $continueButton.Text = 'Continua'
    $continueButton.Location = New-Object System.Drawing.Point(640, 510)
    $continueButton.Size = New-Object System.Drawing.Size(96, 32)
    $continueButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
    $protectedForm.Controls.Add($continueButton)

    $cancelProtectedButton = New-Object System.Windows.Forms.Button
    $cancelProtectedButton.Text = 'Annulla'
    $cancelProtectedButton.Location = New-Object System.Drawing.Point(744, 510)
    $cancelProtectedButton.Size = New-Object System.Drawing.Size(96, 32)
    $cancelProtectedButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
    $protectedForm.Controls.Add($cancelProtectedButton)

    $protectedForm.AcceptButton = $continueButton
    $protectedForm.CancelButton = $cancelProtectedButton

    $protectedForm.Add_FormClosing({
        for ($i = 0; $i -lt $checkedList.Items.Count; $i++) {
            $label = [string]$checkedList.Items[$i]
            $rememberedSelections[$candidateByLabel[$label]] = $checkedList.GetItemChecked($i)
        }
        Save-ProtectedPageSelection -StateFile $selectionStateFile -Selections $rememberedSelections
    })

    $protectedResult = $protectedForm.ShowDialog()
    if ($protectedResult -ne [System.Windows.Forms.DialogResult]::OK) {
        return [pscustomobject]@{
            Cancelled = $true
            Pages     = @()
        }
    }

    $selectedPages = New-Object System.Collections.Generic.List[string]
    foreach ($item in $checkedList.CheckedItems) {
        $label = [string]$item
        if ($candidateByLabel.ContainsKey($label)) {
            $selectedPages.Add([string]$candidateByLabel[$label]) | Out-Null
        }
    }

    return [pscustomobject]@{
        Cancelled = $false
        Pages     = $selectedPages.ToArray()
    }
}

$versions = Get-SortedVersions -Root $sourceRoot
if (-not $versions -or $versions.Count -eq 0) {
    throw "Nessuna versione trovata in $sourceRoot"
}

$form = New-Object System.Windows.Forms.Form
$form.Text = 'Build Manuale'
$form.StartPosition = 'CenterScreen'
$form.FormBorderStyle = 'FixedDialog'
$form.MaximizeBox = $false
$form.MinimizeBox = $false
$form.ClientSize = New-Object System.Drawing.Size(470, 325)
$form.Font = New-Object System.Drawing.Font('Segoe UI', 9)
$form.Topmost = $true

$titleLabel = New-Object System.Windows.Forms.Label
$titleLabel.Text = 'Scegli il tipo di build'
$titleLabel.Location = New-Object System.Drawing.Point(20, 18)
$titleLabel.Size = New-Object System.Drawing.Size(250, 24)
$titleLabel.Font = New-Object System.Drawing.Font('Segoe UI Semibold', 11)
$form.Controls.Add($titleLabel)

$infoLabel = New-Object System.Windows.Forms.Label
$infoLabel.Text = 'Scegli prima il tipo di build e poi se applicarlo a tutto il manuale oppure a una sola versione e lingua.'
$infoLabel.Location = New-Object System.Drawing.Point(20, 48)
$infoLabel.Size = New-Object System.Drawing.Size(420, 42)
$form.Controls.Add($infoLabel)

$typeLabel = New-Object System.Windows.Forms.Label
$typeLabel.Text = 'Tipo build'
$typeLabel.Location = New-Object System.Drawing.Point(24, 94)
$typeLabel.Size = New-Object System.Drawing.Size(100, 22)
$typeLabel.Font = New-Object System.Drawing.Font('Segoe UI Semibold', 9)
$form.Controls.Add($typeLabel)

$radioQuick = New-Object System.Windows.Forms.RadioButton
$radioQuick.Text = 'Rapido: solo HTML'
$radioQuick.Location = New-Object System.Drawing.Point(44, 118)
$radioQuick.Size = New-Object System.Drawing.Size(180, 24)
$radioQuick.Checked = $true
$form.Controls.Add($radioQuick)

$quickHint = New-Object System.Windows.Forms.Label
$quickHint.Text = 'Piu'' veloce, solo HTML.'
$quickHint.Location = New-Object System.Drawing.Point(64, 140)
$quickHint.Size = New-Object System.Drawing.Size(320, 20)
$form.Controls.Add($quickHint)

$radioFull = New-Object System.Windows.Forms.RadioButton
$radioFull.Text = 'Completo: HTML + ZIP offline'
$radioFull.Location = New-Object System.Drawing.Point(44, 166)
$radioFull.Size = New-Object System.Drawing.Size(220, 24)
$form.Controls.Add($radioFull)

$fullHint = New-Object System.Windows.Forms.Label
$fullHint.Text = 'Genera anche il pacchetto ZIP del sito offline.'
$fullHint.Location = New-Object System.Drawing.Point(64, 188)
$fullHint.Size = New-Object System.Drawing.Size(360, 20)
$form.Controls.Add($fullHint)

$scopeLabel = New-Object System.Windows.Forms.Label
$scopeLabel.Text = 'Ambito'
$scopeLabel.Location = New-Object System.Drawing.Point(24, 220)
$scopeLabel.Size = New-Object System.Drawing.Size(100, 22)
$scopeLabel.Font = New-Object System.Drawing.Font('Segoe UI Semibold', 9)
$form.Controls.Add($scopeLabel)

$radioAll = New-Object System.Windows.Forms.RadioButton
$radioAll.Text = 'Tutte le versioni e lingue'
$radioAll.Location = New-Object System.Drawing.Point(44, 244)
$radioAll.Size = New-Object System.Drawing.Size(220, 24)
$radioAll.Checked = $true
$form.Controls.Add($radioAll)

$radioSingle = New-Object System.Windows.Forms.RadioButton
$radioSingle.Text = 'Solo una versione e lingua'
$radioSingle.Location = New-Object System.Drawing.Point(44, 272)
$radioSingle.Size = New-Object System.Drawing.Size(220, 24)
$form.Controls.Add($radioSingle)

$versionLabel = New-Object System.Windows.Forms.Label
$versionLabel.Text = 'Versione'
$versionLabel.Location = New-Object System.Drawing.Point(274, 244)
$versionLabel.Size = New-Object System.Drawing.Size(80, 22)
$form.Controls.Add($versionLabel)

$versionCombo = New-Object System.Windows.Forms.ComboBox
$versionCombo.Location = New-Object System.Drawing.Point(350, 240)
$versionCombo.Size = New-Object System.Drawing.Size(95, 24)
$versionCombo.DropDownStyle = 'DropDownList'
$versionCombo.Enabled = $false
[void]$versionCombo.Items.AddRange([string[]]$versions)
$versionCombo.SelectedIndex = 0
$form.Controls.Add($versionCombo)

$languageLabel = New-Object System.Windows.Forms.Label
$languageLabel.Text = 'Lingua'
$languageLabel.Location = New-Object System.Drawing.Point(274, 274)
$languageLabel.Size = New-Object System.Drawing.Size(60, 22)
$form.Controls.Add($languageLabel)

$languageCombo = New-Object System.Windows.Forms.ComboBox
$languageCombo.Location = New-Object System.Drawing.Point(350, 270)
$languageCombo.Size = New-Object System.Drawing.Size(95, 24)
$languageCombo.DropDownStyle = 'DropDownList'
$languageCombo.Enabled = $false
$form.Controls.Add($languageCombo)

function Update-LanguageOptions {
    $languageCombo.Items.Clear()

    $selectedVersion = [string]$versionCombo.SelectedItem
    if ([string]::IsNullOrWhiteSpace($selectedVersion)) {
        return
    }

    $versionPath = Join-Path $sourceRoot $selectedVersion
    $languages = Get-SortedLanguages -VersionPath $versionPath
    if ($languages.Count -gt 0) {
        [void]$languageCombo.Items.AddRange([string[]]$languages)
        $languageCombo.SelectedIndex = 0
    }
}

function Set-SingleBuildState {
    param([bool]$Enabled)

    $versionCombo.Enabled = $Enabled
    $languageCombo.Enabled = $Enabled
}

$radioAll.Add_CheckedChanged({
    if ($radioAll.Checked) {
        Set-SingleBuildState -Enabled $false
    }
})

$radioSingle.Add_CheckedChanged({
    if ($radioSingle.Checked) {
        Set-SingleBuildState -Enabled $true
        Update-LanguageOptions
    }
})

$versionCombo.Add_SelectedIndexChanged({
    if ($radioSingle.Checked) {
        Update-LanguageOptions
    }
})

Update-LanguageOptions

$buildButton = New-Object System.Windows.Forms.Button
$buildButton.Text = 'Avvia build'
$buildButton.Location = New-Object System.Drawing.Point(254, 286)
$buildButton.Size = New-Object System.Drawing.Size(96, 32)
$buildButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
$form.Controls.Add($buildButton)

$cancelButton = New-Object System.Windows.Forms.Button
$cancelButton.Text = 'Annulla'
$cancelButton.Location = New-Object System.Drawing.Point(356, 286)
$cancelButton.Size = New-Object System.Drawing.Size(96, 32)
$cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
$form.Controls.Add($cancelButton)

$form.AcceptButton = $buildButton
$form.CancelButton = $cancelButton

$result = $form.ShowDialog()

if ($result -ne [System.Windows.Forms.DialogResult]::OK) {
    Write-Output 'CANCELLED=1'
    exit 0
}

$selectedBuildType = if ($radioFull.Checked) { 'full' } else { 'quick' }
$selectedBuildScope = if ($radioSingle.Checked) { 'single' } else { 'all' }
$selectedVersion = ''
$selectedLanguage = ''

if ($radioSingle.Checked) {
    $selectedVersion = [string]$versionCombo.SelectedItem
    $selectedLanguage = [string]$languageCombo.SelectedItem

    if ([string]::IsNullOrWhiteSpace($selectedVersion) -or [string]::IsNullOrWhiteSpace($selectedLanguage)) {
        [System.Windows.Forms.MessageBox]::Show(
            'Seleziona una versione e una lingua valide.',
            'Selezione incompleta',
            [System.Windows.Forms.MessageBoxButtons]::OK,
            [System.Windows.Forms.MessageBoxIcon]::Warning
        ) | Out-Null
        Write-Output 'CANCELLED=1'
        exit 0
    }
}

$protectedSelection = Show-ProtectedPageDialog -TargetVersion $selectedVersion -TargetLanguage $selectedLanguage
if ($protectedSelection.Cancelled) {
    Write-Output 'CANCELLED=1'
    exit 0
}

$protectedPagesFile = ''
if ($protectedSelection.Pages.Count -gt 0) {
    $protectedPagesFile = Join-Path ([System.IO.Path]::GetTempPath()) ('flexibowl-protected-pages-' + [guid]::NewGuid().ToString('N') + '.json')
    $protectedPagesJson = ConvertTo-Json -InputObject @($protectedSelection.Pages)
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($protectedPagesFile, $protectedPagesJson, $utf8NoBom)
}

Write-Output ('BUILD_TYPE=' + $selectedBuildType)
Write-Output ('BUILD_SCOPE=' + $selectedBuildScope)
if ($selectedBuildScope -eq 'single') {
    Write-Output ('VERSION=' + $selectedVersion)
    Write-Output ('LANGUAGE=' + $selectedLanguage)
}
if (-not [string]::IsNullOrWhiteSpace($protectedPagesFile)) {
    Write-Output ('PROTECTED_PAGES_FILE=' + $protectedPagesFile)
}
