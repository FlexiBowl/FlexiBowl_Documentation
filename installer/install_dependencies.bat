@echo off
setlocal

set "SHOULD_WAIT_FOR_ENTER=0"

if /I "%~1"=="--no-wait" (
  set "SHOULD_WAIT_FOR_ENTER=0"
) else (
  set "SHOULD_WAIT_FOR_ENTER=1"
)

powershell -ExecutionPolicy Bypass -File "%~dp0install_dependencies.ps1" %*
set "INSTALL_STATUS=%errorlevel%"

if "%SHOULD_WAIT_FOR_ENTER%"=="1" (
  echo.
  set /p "=Premi Invio per chiudere..."
)

exit /b %INSTALL_STATUS%
