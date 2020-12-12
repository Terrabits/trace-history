@echo off
SET ROOT_DIR=%~dp0..


setlocal
cd %ROOT_DIR%


rem clean
rmdir /S /Q build
rmdir /S /Q dist
