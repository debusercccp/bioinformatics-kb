# Setup del vault su Windows: installa cio' che serve all'import dei docx e fa il push su GitHub.
# Avvio: doppio clic su .scripts\setup-windows.cmd (oppure: powershell -ExecutionPolicy Bypass -File .scripts\setup-windows.ps1)
$ErrorActionPreference = 'Stop'
$Vault = Split-Path -Parent $PSScriptRoot

function Refresh-Path {
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
}
function Has($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Works($exe, $arg) { try { & $exe $arg *> $null; return $LASTEXITCODE -eq 0 } catch { return $false } }
function Install($id, $name) {
    Write-Host "-> installo $name ($id)" -ForegroundColor Cyan
    winget install --id $id -e --source winget --accept-package-agreements --accept-source-agreements --silent
    Refresh-Path
}

if (-not (Has winget)) { throw 'winget non trovato: installa "App Installer" dal Microsoft Store e rilancia.' }

# Git (Git Bash serve per .scripts/update.sh)
if (-not (Has git)) { Install 'Git.Git' 'Git for Windows' }
# Python 3 (python o py; l'alias "python3" del Microsoft Store non conta)
if (-not ((Works 'python' '--version') -or (Works 'py' '--version'))) { Install 'Python.Python.3.12' 'Python 3.12' }
# Pandoc >= 3 (altrimenti update.sh ne scarica una copia privata via pip)
if (-not (Has pandoc)) { Install 'JohnMacFarlane.Pandoc' 'Pandoc' }
# LibreOffice (soffice: converte le immagini EMF dei docx)
if (-not (Test-Path "$env:ProgramFiles\LibreOffice\program\soffice.exe")) { Install 'TheDocumentFoundation.LibreOffice' 'LibreOffice' }
# ImageMagick (magick: ritaglia le immagini convertite)
if (-not (Has magick) -and -not (Get-ChildItem "$env:ProgramFiles\ImageMagick-*\magick.exe" -ErrorAction SilentlyContinue)) { Install 'ImageMagick.ImageMagick' 'ImageMagick' }

Write-Host "`nVerifica:" -ForegroundColor Green
Refresh-Path
foreach ($c in 'git', 'python', 'py', 'pandoc', 'magick') {
    $p = (Get-Command $c -ErrorAction SilentlyContinue).Source
    Write-Host ("  {0,-7} {1}" -f $c, $(if ($p) { $p } else { '-' }))
}
Write-Host ("  soffice {0}" -f $(if (Test-Path "$env:ProgramFiles\LibreOffice\program\soffice.exe") { "$env:ProgramFiles\LibreOffice\program\soffice.exe" } else { '-' }))

# Prova dell'import (non cambia nulla se i docx non sono cambiati)
$bash = "$env:ProgramFiles\Git\bin\bash.exe"
if (Test-Path $bash) {
    Write-Host "`nProva import (.scripts/update.sh):" -ForegroundColor Green
    Push-Location $Vault; & $bash .scripts/update.sh; Pop-Location
}

# Push su GitHub (usa le credenziali di Git Credential Manager: al primo push si apre il login nel browser)
Write-Host "`nPush su GitHub:" -ForegroundColor Green
git -C $Vault status -sb | Select-Object -First 1
git -C $Vault push origin main
if ($LASTEXITCODE -eq 0) { Write-Host 'Push completato.' -ForegroundColor Green } else { Write-Host 'Push non riuscito: vedi il messaggio sopra.' -ForegroundColor Red }
