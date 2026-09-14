@echo off
title MindTrace AI - Multi-Agent Safety Observatory
echo ==========================================================
echo Starting MindTrace AI Observatory...
echo ==========================================================
python server.py
if %ERRORLEVEL% NEQ 0 (
    echo Python server failed or Python is not installed. Opening index.html directly...
    start index.html
)
pause
