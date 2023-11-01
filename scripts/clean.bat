@echo off
setlocal
SET "ROOT_DIR=%~dp0.."
cd /d "%ROOT_DIR%"


rem clean
rmdir /S /Q build
rmdir /S /Q dist\trace-history
