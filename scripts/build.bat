@echo off
setlocal
SET "ROOT_DIR=%~dp0.."
cd /d "%ROOT_DIR%"


rem build
pyinstaller trace-history.spec %*
