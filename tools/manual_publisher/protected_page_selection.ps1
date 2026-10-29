function Get-ProtectedPageSelection {
    param([string]$StateFile)

    $selections = @{}
    if (Test-Path -LiteralPath $StateFile -PathType Leaf) {
        try {
            $saved = Get-Content -LiteralPath $StateFile -Raw -Encoding UTF8 | ConvertFrom-Json
            if ($saved.Version -eq 1 -and $null -ne $saved.Pages) {
                foreach ($property in $saved.Pages.PSObject.Properties) {
                    if ($property.Value -is [bool]) {
                        $selections[$property.Name] = $property.Value
                    }
                }
            }
        } catch {
            # A missing or invalid preference file falls back to the last build.
        }
    }
    return $selections
}

function Save-ProtectedPageSelection {
    param(
        [string]$StateFile,
        [hashtable]$Selections
    )

    $stateDirectory = Split-Path -Parent $StateFile
    [void][System.IO.Directory]::CreateDirectory($stateDirectory)
    $json = ConvertTo-Json -InputObject @{ Version = 1; Pages = $Selections } -Depth 3
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    $temporaryFile = Join-Path $stateDirectory ('protected-page-selection-' + [guid]::NewGuid().ToString('N') + '.tmp')
    [System.IO.File]::WriteAllText($temporaryFile, $json, $utf8NoBom)
    Move-Item -LiteralPath $temporaryFile -Destination $StateFile -Force
}

function Get-ProtectedPageCheckedState {
    param(
        [string]$OutputPath,
        [bool]$DefaultChecked,
        [hashtable]$Selections,
        [string]$BuildRoot
    )

    if ($Selections.ContainsKey($OutputPath)) {
        return [bool]$Selections[$OutputPath]
    }

    $builtPage = Join-Path $BuildRoot $OutputPath
    if (Test-Path -LiteralPath $builtPage -PathType Leaf) {
        return [bool](Select-String -LiteralPath $builtPage -Encoding UTF8 -SimpleMatch -Quiet `
            -Pattern '<meta name="ars-protected-page" content="encrypted">')
    }

    if ($Selections.Count -gt 0) {
        return $false
    }
    return $DefaultChecked
}
