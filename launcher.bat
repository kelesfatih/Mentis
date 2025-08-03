@echo off
TITLE Server Launcher

ECHO Starting Ollama and Open WebUI services...

REM Start the servers in new, separate, hidden windows using PowerShell
powershell -Command "Start-Process -FilePath 'ollama' -ArgumentList 'serve' -WindowStyle Hidden"
powershell -Command "Start-Process -FilePath 'open-webui' -ArgumentList 'serve' -WindowStyle Hidden"

ECHO Waiting for port 8080 to become available. This may take a moment...
ECHO This window will show a dot every second while waiting.

:waitloop
REM Use netstat to check for listening ports and findstr to filter for port 8080.
REM The command looks for a line containing "TCP", ":8080", and "LISTENING".
netstat -an | findstr /R /C:"TCP.*:8080.*LISTENING" > nul

REM findstr sets errorlevel to 0 if the text is found, and 1 if not.
if %errorlevel% equ 0 (
    goto :ready
)

REM Print a dot to show the script is still working, then wait 1 second.
echo|set /p=.
timeout /t 1 /nobreak > nul
goto :waitloop

:ready
echo.
ECHO Port 8080 is now open!
ECHO Launching http://localhost:8080 in your browser...
start http://localhost:8080

ECHO Browser has been launched.
ECHO The servers are running in the background. To stop them, use Task Manager.
pause