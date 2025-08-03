@echo off
TITLE Mentis Launcher
SET "FLAG_FILE=setup_complete.flag"

REM Check if the setup completion flag exists.
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
    
    REM If setup was successful, create the flag file.
    ECHO Setup successful. Creating completion flag.
    ECHO Setup completed on %DATE% at %TIME% > "%FLAG_FILE%"
    
    ECHO.
    ECHO Setup is complete! The application will now start.
    pause
    CALL launcher.bat
)