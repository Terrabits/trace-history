@echo off
SET ROOT_DIR=%~dp0..


setlocal
cd %ROOT_DIR%


rem install
pip install --editable .[dev]
