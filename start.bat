@echo off
TITLE Mentis Launcher
SET "FLAG_FILE=%USERPROFILE%\setup_complete.flag"
SET "DATA_DIR=C:\open-webui\data"

REM Create OpenWebUI data directory if it doesn't exist
IF NOT EXIST "%DATA_DIR%" (
    ECHO Creating OpenWebUI data directory...
    mkdir "%DATA_DIR%" 2>nul
)

REM Check if the setup completion flag exists in user directory.
IF EXIST "%FLAG_FILE%" (
    REM If it exists, run the normal launcher.
    ECHO Setup has already been completed. Starting the application...
    CALL launcher.bat
) ELSE (
    REM If it does not exist, run the setup script.
    ECHO First time setup. Running setup.py...
    ECHO This may take a while to download models and dependencies.
    
    REM Run the Python setup script.
    py -3.11 setup.py
    
    REM Check if setup.py ran successfully.
    REM A non-zero errorlevel indicates a failure.
    IF %ERRORLEVEL% NEQ 0 (
        ECHO.
        ECHO Setup failed. Please check the errors above.
        pause
        exit /b %ERRORLEVEL%
    )
    
    REM If setup was successful, create the flag file in user directory.
    ECHO Setup successful. Creating completion flag in user directory.
    ECHO Setup completed on %DATE% at %TIME% > "%FLAG_FILE%"
    
    ECHO.
    ECHO Setup is complete! The application will now start.
    pause
    CALL launcher.bat
)