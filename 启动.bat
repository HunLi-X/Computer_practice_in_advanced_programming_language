@echo off
chcp 65001 >nul
title 高级语言上机实习项目 - 一键启动

echo.
echo ╔════════════════════════════════╗
echo ║   高级语言上机实习项目         ║
echo ║   Python 3.13 一键启动器       ║
echo ╚════════════════════════════════╝
echo.

:: ── 检查 Python ──
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python，请先安装 Python 3.13+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [✓] Python 环境正常

:: ── 切换到脚本所在目录 ──
cd /d "%~dp0"

:: ── 检查并安装依赖 ──
echo [*] 检查依赖库...
python -c "import customtkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] 正在安装 customtkinter ...
    python -m pip install customtkinter -q -i https://pypi.tuna.tsinghua.edu.cn/simple
    if %errorlevel% neq 0 (
        python -m pip install customtkinter -q
    )
)
python -c "import CTkMessagebox" >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] 正在安装 CTkMessagebox ...
    python -m pip install CTkMessagebox -q -i https://pypi.tuna.tsinghua.edu.cn/simple
    if %errorlevel% neq 0 (
        python -m pip install CTkMessagebox -q
    )
)
echo [✓] 依赖检查完成

:: ── 启动主程序 ──
echo [*] 启动主程序...
echo.
python "Py3.13.7设计源文件\main.py"

if %errorlevel% neq 0 (
    echo.
    echo [错误] 启动失败，请检查 Python 环境
    pause
    exit /b 1
)

echo.
echo [✓] 程序已退出
echo.
pause