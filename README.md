[English](README.en.md) | 简体中文

<div align="center">
<h1>高级语言上机实习项目</h1>

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-6366f1)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-Education-green)


[![Auth](https://img.shields.io/badge/Auther--HunLi-ff69b4.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAADZElEQVR4nO2ZX2iPURjHP/7/aZN/E21DaZvtwoVYyQUuGXLB/LtkLRcUhSJMSVwg3KCUJPJvLmRZtMQFLvwZhUJk/saGLWaYV6eet06n9/3tfd+9531/sW89td9z3vOc8z3nPOc8zzPoQQ+yAnlAA/AbcCzKR2ClTSL7LRNwNPkB5Noi0pggEQeYbovIh4SJLLBBojfwK2EiVTaIjEyYhANsskGkNAUi+2wQmZECkRM2iCxMgUi9DSKrxPhS7GOZjHXPhvGtYlwdMduYKWO9tmH8oBgvxj6KZawOoFfcxk+L8RzsI0fzkyFhO28EvqXg0FHlK1DtReRzFkzOCSmfvIhczIKJOSHlmheRgcAK4E4WTNDpQp4Ba4P4zxRgO3ArgSQqqDQDx4AKCWBDYwSwRDP4JWECG4CpQB9iwCTNsBsJl8srvxk4CtQBN4Enkre0GKQ7RaekCXgAXAcuAHuB1bLaZcAgrd+2uK78ai0PsfLSBshG70u9IDJmyUq2AYvlbD5N4Dg9l/EnArdFV9sdIlfEiLrNzFAlqPwE2kP2OaKNlyfH8Q9QFJVIixgepukqIuTdRRI3Be1TaczjnOgXRSXyTgwUarrBIVb4htbvcMA+nR7+UCdtc6MSOS8G9hj6+gjlnHEBd+WuMVaZ9FMyJiqRydrgB4B80VcFmFBtxALfFm3nlwPv48rfK7WoWDkc8jgpYq0eE/kOnAGG+4RBh3z6qTGOyzfIJeG2nQL6EQMmaEaTgtNdv+jKcFJwbI33XxEpAM76+IArrXIbFqVFpE0MuzeXF4nmEI9ecwZbhVo6GzsaxLhnniw74YQUVdDwwjppv2yzaPbIJ7HJdJz8RIX5JgYAL6V9vg0ifYEXMsAaj3Z3cpfkmPmhQAs5vHxgh+gbbdS0XMyTQdrkbdHhTiwTCdMHTCLl8hCqeGsalnFSO2JDNb3XxOZINqhkttFmfq8W4I1PbGcFuVr21qCloe7EarRvmzT9K01fYxAZJVmgA1yNKxwh4NF4q0Wr+UZs5JIxndskoVLoEskI1e/HRu6TCEpklR1ZebPcqk/YT9cu1UL190NgNCmhQGpfTjelLo2dMNEf2BkylXVF7eL6qAU3WyiVvCHIv7A7pBY2nizGWGC3FOr0XeoQZ96VIcbqAf8K/gLNGaTJ3vwbFgAAAABJRU5ErkJggg==)](https://github.com/HunLi-X)
[![cnb](https://img.shields.io/badge/CNB-xhunli-F76945?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAppJREFUOE9tk01rE1EUhs+5H5lJ0iQT3FRX2Yi4avoLkv4CWxBcNt11oZiuFKGmXQhFN6kuRESSgitXKf6A5g+I6cqFLiKCiptOkraZ5H4cuZOkH9oLw+UO8z7nvGfei3DFohoEQLAKCGWyGJCSbQZsD3ei7r+f45WATV6xmjdISyAlYLaDliveux+ti5ozwLAaFPhIlk6G6f18sxuO7l9bBiWbVoncDGCMWMl++PI/gJ7IohkmD0zkBxT5oRn5LTpN7ULqBByEtFywWvRyHz8Fx3dvN0UwuMPyR0uJFycddH7tKPHZRn7BjnwwkQcUud0HO/K7oOENcTYPRCEAFERmsCpyfZDZfpdnBosOUKGx13BC60QTIdjpmSzrEWDR+UagjsgMciLXAwfhc4MNpKfQtOPE6mVh0gEOaeTXtWXXEdADpJAR/GaZ/rrM9Us82wORPd5zHbRp7JVcyxR5PRP5LTPy6uo0HXIlG9awMgLuEUABkBYI7VLyxs+yyPW3+Nyg4zqoG+UV7TDRlMBbWA/D43u3qlbLGmgRWM2BjFxjQjWQGQBuu4bYYvrm14JMnQSXcjBcny9A5DXIiDJp9/8FWCXAAOaFUEfILTgIcttOvf+2NJnLdI0fBFUyskZKBGTEJEAmBuzr9LCSUDwGQAwwgMzu+m9/VWOAeZSsk+YP48C4li/sRok1nlBd5PogBjgxNw70PfHyqBADyEVXicasZXCVpxYiLfO+HxVZDHCVYwvu2ebPT7fOLNAm65AWLnEAzvsEcOi9/lPU1aACXDfOLdhD9kxNszGdweQGYstqXgItJwDFNxKvwrp57G8h0zVwldHuA0IFt8El83yIs2FSDcpgxDJpUUTwK7gTduN3AK5iG7ehc/E2/gUPD3q3eY4awwAAAABJRU5ErkJggq==)](https://cnb.cool/u/xhunli)

<p>高级语言上机实习综合实践项目，包含 5 个 Python 应用程序的 GUI 和控制台版本。</p>
<img src="https://cnb.cool/66666/resource/-/git/raw/main/img/hengtiao.gif" width="100%" height="3">
</div><br>
  
> 一键启动，支持深色/浅色主题切换。

</div>

---

## 快速开始

```bash
# 双击启动脚本（Windows）
启动.bat

# 或手动运行
pip install -r "Py3.13.7设计源文件/requirements.txt"
python "Py3.13.7设计源文件/main.py"
```
## 项目简介

本项目是高级语言上机实习的综合实践项目，包含5个Python应用程序的GUI和控制台版本。项目采用模块化设计，每个APP独立运行，同时提供统一的启动器界面。

---

## 项目结构

```
Py3.13.7设计源文件/
├── main.py                          # 主程序启动器
├── APP/                             # 应用程序目录
│   ├── APP1.数制转换.py             # 控制台版本
│   ├── APP1.数制转换_gui.py         # GUI版本
│   ├── APP2.猜数游戏.py
│   ├── APP2.猜数游戏_gui.py
│   ├── APP3.七段数码管绘制.py
│   ├── APP3.七段数码管绘制_gui.py
│   ├── APP4.学生成绩管理系统.py
│   ├── APP4.学生成绩管理系统_gui.py
│   ├── APP5.Excel文件，xls，xlsx处理.py
│   └── APP5.Excel文件，xls，xlsx处理_gui.py
└── DATA/                            # 数据文件目录
```

---

## 应用程序说明

### APP1 - 数制转换

**功能**: 支持任意进制之间的相互转换（2-36进制）

**主要特性**:
- 支持 2、8、10、16、32、36 等多种进制输入
- 可自由选择目标进制进行转换
- 同时显示所有常用进制结果（二进制、八进制、十进制、十六进制）
- 支持负数和0的处理

**使用示例**:
- 将十六进制 `FF` 转换为二进制
- 将二进制 `1010` 转换为八进制
- 将十进制 `255` 转换为任意进制

---

### APP2 - 猜数游戏

**功能**: 1-100范围内的猜数字游戏

**主要特性**:
- 系统随机生成1-100之间的整数
- 用户输入猜测的数字
- 系统提示"大了"、"小了"或"猜对了"
- 统计猜测次数

---

### APP3 - 七段数码管绘制

**功能**: 使用Canvas绘制七段数码管显示数字

**主要特性**:
- 使用Tkinter Canvas绘制
- 支持0-9数字显示
- 可自定义颜色和尺寸
- 显示当前时间

---

### APP4 - 学生成绩管理系统

**功能**: 使用字典操作实现的学生成绩管理

**主要特性**:
- 学生信息录入（学号、姓名、成绩）
- 成绩查询功能
- 成绩统计分析
- 成绩排序功能
- 数据持久化

---

### APP5 - Excel文件处理

**功能**: 按部门拆分Excel表格

**主要特性**:
- 支持 `.xls` 和 `.xlsx` 格式
- 按部门列拆分工作表
- 自动生成多个Excel文件
- 保留原格式

**依赖库**:
```bash
pip install openpyxl xlrd
```

---

## 环境要求

- **Python版本**: 3.13.7
- **操作系统**: Windows / Linux / macOS
- **依赖库**: openpyxl, xlrd (仅APP5需要)

---

## 安装依赖

```bash
pip install openpyxl xlrd
```

---

## 运行方式

### 方式一：使用主启动器（推荐）

```bash
python main.py
```

启动后可选择 **GUI界面** 或 **控制台** 模式运行各个APP。

### 方式二：直接运行单个APP

**控制台版本**:
```bash
python APP/APP1.数制转换.py
python APP/APP2.猜数游戏.py
python APP/APP3.七段数码管绘制.py
python APP/APP4.学生成绩管理系统.py
python APP/APP5.Excel文件，xls，xlsx处理.py
```

**GUI版本**:
```bash
python APP/APP1.数制转换_gui.py
python APP/APP2.猜数游戏_gui.py
python APP/APP3.七段数码管绘制_gui.py
python APP/APP4.学生成绩管理系统_gui.py
python APP/APP5.Excel文件，xls，xlsx处理_gui.py
```

---

## 技术栈

- **GUI框架**: tkinter
- **数据处理**: openpyxl, xlrd
- **核心技术**: 字典操作、文件I/O、Canvas绘图、subprocess进程管理

---

## 项目特色

1. **双模式支持**: 每个APP都提供GUI和控制台两个版本
2. **统一启动器**: 通过主程序可以方便地启动所有APP
3. **模块化设计**: 每个APP独立，便于维护和扩展
4. **用户友好**: GUI界面美观，操作直观
5. **功能完善**: 涵盖多种编程知识点和实际应用场景

---

## 知识点覆盖

- 数据类型转换
- 条件判断与循环
- 字典和列表操作
- 文件读写
- 异常处理
- GUI编程
- 进程管理
- Excel文件处理
- Canvas绘图

---

## 更新日志

### 2026-05
- 主界面升级为 **CustomTkinter**，支持深色/浅色主题切换
- 新增 `启动.bat` 一键启动脚本，自动安装依赖
- 新增 `requirements.txt` 依赖清单
- 日志面板优化，异步启动不阻塞 UI
- 全局信息脱敏，移除个人隐私信息
- 新增 Excel 处理 GUI 版本及配套数据文件

### 2025-01
- 更新APP1：支持任意进制之间的转换（2-36进制）
- 优化主启动器界面布局
- 增强日志显示功能
- 新增各学院分表 Excel 文件
- 添加项目 README 文档
- 初始化项目：添加 5 个 Python 应用程序及 GUI 版本

---

## 许可证

本项目仅供学习交流使用。
