[English](README.en.md) | 简体中文

<div align="center">
<h1>高级语言上机实习项目</h1>

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-6366f1)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-Education-green)

<p align="center">
  <a href="https://github.com/HunLi-X">
    <img src="https://img.shields.io/badge/Auther--HunLi-ff69b4?logo=github&logoColor=white" alt="Auth" />
  </a>
  <a href="https://cnb.cool/u/xhunli">
    <img src="https://img.shields.io/badge/CNB-xhunli-F76945?logo=data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIwIDMyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0yMjguOTA2IDQwLjI0MTJDMjI5Ljg4MiAzNy41MTA4IDIyOC45MDYgMzQuMzkwMyAyMjYuNzU5IDMyLjQ0QzIxOS4zNDIgMjYuMDA0IDIwMC43OTkgMTIuMzUxOSAxNzMuMDgyIDEwLjQwMTZDMTQxLjg1MiA4LjA2MTIxIDEyMi41MjggMTYuNDQ3NSAxMTIuNzY5IDIyLjY4ODVDMTA4LjQ3NCAyNS40MTg5IDEwOC4yNzkgMzEuNDY0OSAxMTIuMTgzIDM0LjM5MDNMMTkxLjYyNSA5Ni4yMTQ5QzE5OC42NTIgMTAxLjY3NiAyMDguOTk3IDk4LjU1NTMgMjExLjcyOSA5MC4xNjlMMjI4LjcxMSA0MC4yNDEySDIyOC45MDZaIiBmaWxsPSIjRkY2MjAwIi8+DQo8cGF0aCBkPSJNMzIuOTM4MSAyMjMuNTY0QzI5LjYxOTkgMjI1LjcxIDI4LjI1MzYgMjI5LjgwNSAyOS4yMjk1IDIzMy41MTFDMzIuMTU3MyAyNDQuNDMyIDQxLjMzMTIgMjY2Ljg2MSA2Ni45MDA5IDI4Ny41MzRDOTIuNDcwNiAzMDguMDEyIDEyMi43MjUgMzEwLjM1MyAxMzUuNjA3IDMwOS45NjNDMTM5LjUxMSAzMDkuOTYzIDE0Mi44MjkgMzA3LjQyNyAxNDQgMzAzLjcyMkwxOTQuOTQ1IDE0Mi42MjdDMTk4LjY1MyAxMzAuOTI1IDE4NS41NzYgMTIxLjE3MyAxNzUuNDI2IDEyNy45OTlMMzIuOTM4MSAyMjMuNTY0WiIgZmlsbD0iI0ZGNjIwMCIvPg0KPHBhdGggZD0iTTcwLjIxNjkgNTMuNDk1NUM2Ny42Nzk0IDUyLjUyMDMgNjQuOTQ2OCA1Mi43MTUzIDYyLjYwNDUgNTMuODg1NUM1My4yMzU1IDU4Ljk1NjMgMjkuMDMyIDc0Ljc1MzggMTYuNTQgMTA3LjMyNEM2Ljc4MDU0IDEzMi4yODggMTAuMDk4NyAxNTkuOTgyIDEyLjgzMTQgMTczLjQzOUMxMy42MTIxIDE3Ny45MjUgMTguMjk2NyAxODAuNDYgMjIuNTkwOCAxNzguNzA1TDE3NS40MjQgMTE5LjAyNkMxODYuMzU0IDExNC43MzUgMTg2LjM1NCA5OS4zMjc2IDE3NS40MjQgOTUuMDM2OUw3MC4yMTY5IDUzLjQ5NTVaIiBmaWxsPSIjRkY2MjAwIi8+DQo8cGF0aCBkPSJNMjk3LjAzIDE2OC45NjhDMzAxLjUxOSAxNzEuODkzIDMwNy41NyAxNjkuMzU4IDMwOC4zNTEgMTY0LjA5MkMzMTAuMzAxIDE1MC4wNSAzMTIuMDYgMTI1Ljg2NiAzMDQuMDU3IDEwNy4zMzZDMjkzLjMyMSA4Mi45NTkxIDI3NC45NzQgNjcuNzQ2OCAyNjYuMTkgNjEuNzAwOEMyNjMuNDU4IDU5Ljc1MDUgMjU5Ljc0OSA1OS45NDU2IDI1Ny4yMTIgNjIuMjg1OUwyMTguNTY0IDk2LjQxNjJDMjEyLjMxOCAxMDIuMDcyIDIxMi45MDQgMTEyLjAxOSAyMTkuOTMxIDExNi42OTlMMjk3LjAzIDE2OC45NjhaIiBmaWxsPSIjRkY2MjAwIi8+DQo8cGF0aCBkPSJNMTg5LjA4OSAyOTkuNDI4QzE4OC42OTkgMzAzLjkxNCAxOTIuNjAzIDMwNy44MTQgMTk3LjA5MiAzMDcuMjI5QzIxMS43MzEgMzA1LjY2OSAyNDEuNzkgMjk5LjgxOCAyNjQuMjM3IDI3OC4zNjVDMjg2LjA5OCAyNTcuNDk2IDI5My4zMiAyMzIuNzI4IDI5NS4yNzIgMjIyLjc4MUMyOTUuODU4IDIyMC4wNTEgMjk1LjI3MiAyMTcuMzIgMjkzLjUxNSAyMTUuMTc1TDIyNS45OCAxMzEuODk3QzIxOC43NTggMTIyLjkyNSAyMDQuMTE5IDEyNy40MTEgMjAzLjE0MyAxMzguOTE4TDE4OS4wODkgMjk5LjIzM1YyOTkuNDI4WiIgZmlsbD0iI0ZGNjIwMCIvPg0KPC9zdmc+DQo=&logoColor=white" alt="CNB" />
  </a>
  <a href="https://hunli.100w.top/">
    <img src="https://img.shields.io/badge/Blog-昏黎站-008080?logo=googlechrome&logoColor=white" alt="Blog" />
  </a>
</p>

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
