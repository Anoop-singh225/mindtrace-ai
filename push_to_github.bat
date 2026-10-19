@echo off
title Push MindTrace AI to GitHub
echo ========================================================
echo Pushing MindTrace AI to https://github.com/Anoop-singh225/mindtrace-ai
echo ========================================================
git push -u origin main
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo SUCCESS! Code has been pushed to GitHub successfully!
    echo ========================================================
) else (
    echo.
    echo [NOTE] Make sure you clicked 'Create repository' on GitHub first!
)
pause
