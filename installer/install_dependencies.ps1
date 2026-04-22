$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvRoot = Join-Path $repoRoot '.venv'
$venvPython = Join-Path $venvRoot 'Scripts\python.exe'
$shouldWaitForEnter = $true

if ($args -contains '--no-wait') {
    $shouldWaitForEnter = $false
}

function Test-PythonCandidate {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Command,
        [string[]]$CommandArgs = @(),
        [Parameter(Mandatory = $true)]
        [string]$Label
    )

    try {
        & $Command @CommandArgs --version *> $null
        if ($LASTEXITCODE -eq 0) {
            return [pscustomobject]@{
                Command    = $Command
                CommandArgs = $CommandArgs
                Label      = $Label
            }
        }
    } catch {
    }

    return $null
}

function Find-PythonCandidate {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Candidates
    )

    foreach ($candidate in $Candidates) {
        $resolved = Test-PythonCandidate -Command $candidate.Command -CommandArgs $candidate.CommandArgs -Label $candidate.Label
        if ($null -ne $resolved) {
            return $resolved
        }
    }

    return $null
}

function Get-BootstrapPython {
    $candidates = New-Object System.Collections.Generic.List[object]

    $runtimeRoot = Join-Path $repoRoot 'runtime'
    if (Test-Path $runtimeRoot) {
        Get-ChildItem -LiteralPath $runtimeRoot -Directory -Filter 'Python*' |
            Sort-Object Name -Descending |
            ForEach-Object {
                $pythonExe = Join-Path $_.FullName 'python.exe'
                if (Test-Path $pythonExe) {
                    $candidates.Add([pscustomobject]@{
                        Command     = $pythonExe
                        CommandArgs = @()
                        Label       = $pythonExe
                    })
                }
            }
    }

    $localPython = Join-Path $env:LocalAppData 'Programs\Python\Python312\python.exe'
    if (Test-Path $localPython) {
        $candidates.Add([pscustomobject]@{
            Command     = $localPython
            CommandArgs = @()
            Label       = $localPython
        })
    }

    $candidates.Add([pscustomobject]@{
        Command     = 'python'
        CommandArgs = @()
        Label       = 'python'
    })
    $candidates.Add([pscustomobject]@{
        Command     = 'py'
        CommandArgs = @('-3')
        Label       = 'py -3'
    })

    return Find-PythonCandidate -Candidates $candidates.ToArray()
}

function Install-PythonWithWinget {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PackageId
    )

    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if ($null -eq $winget) {
        return $false
    }

    Write-Host "Python non trovato. Provo a installare automaticamente $PackageId tramite winget..."

    & $winget.Source install --id $PackageId --exact --scope user --accept-package-agreements --accept-source-agreements --disable-interactivity
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Installazione automatica di Python tramite winget fallita con codice $LASTEXITCODE."
        return $false
    }

    return $true
}

$exitCode = 0

try {
    $installPython = $null

    if (Test-Path $venvPython) {
        $installPython = Test-PythonCandidate -Command $venvPython -Label $venvPython
    }

    if ($null -eq $installPython) {
        $bootstrapPython = Get-BootstrapPython
        if ($null -eq $bootstrapPython) {
            $pythonInstalled = Install-PythonWithWinget -PackageId 'Python.Python.3.12'
            if ($pythonInstalled) {
                $bootstrapPython = Get-BootstrapPython
            }
        }

        if ($null -eq $bootstrapPython) {
            throw @"
Nessun interprete Python utilizzabile trovato.

Percorsi e comandi controllati:
  - .venv\Scripts\python.exe
  - runtime\Python*\python.exe
  - $env:LocalAppData\Programs\Python\Python312\python.exe
  - python
  - py -3

Tentativo automatico eseguito:
  - winget install --id Python.Python.3.12 --scope user

Installa Python 3.12 e rilancia questo setup.
"@
        }

        Write-Host "Creo l'ambiente virtuale locale in $venvRoot usando $($bootstrapPython.Label)"
        & $bootstrapPython.Command @($bootstrapPython.CommandArgs + @('-m', 'venv', $venvRoot))
        if ($LASTEXITCODE -ne 0 -or -not (Test-Path $venvPython)) {
            throw "Impossibile creare l'ambiente virtuale locale in $venvRoot."
        }

        $installPython = Test-PythonCandidate -Command $venvPython -Label $venvPython
    }

    if ($null -eq $installPython) {
        throw "Impossibile usare il Python dell'ambiente virtuale locale: $venvPython"
    }

    & $installPython.Command @($installPython.CommandArgs + @('-m', 'pip', 'install', '--upgrade', 'pip'))
    if ($LASTEXITCODE -ne 0) {
        throw "Aggiornamento di pip fallito."
    }

    & $installPython.Command @($installPython.CommandArgs + @('-m', 'pip', 'install', '-r', (Join-Path $repoRoot 'requirements.txt')))
    if ($LASTEXITCODE -ne 0) {
        throw "Installazione delle dipendenze fallita."
    }

    Write-Host "Dipendenze installate nell'ambiente locale: $($installPython.Label)"
} catch {
    $exitCode = 1
    Write-Host ""
    Write-Error $_
} finally {
    if ($shouldWaitForEnter) {
        Write-Host ""
        Read-Host 'Premi Invio per chiudere'
    }
}

exit $exitCode
