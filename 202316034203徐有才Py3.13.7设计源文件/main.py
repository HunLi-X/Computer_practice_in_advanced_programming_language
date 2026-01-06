# ==========================================
# 主程序 - APP集合启动器
# 功能: GUI可视化调用各个APP，支持GUI和控制台两种模式
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

# 添加APP目录到路径
APP_DIR = os.path.join(os.path.dirname(__file__), 'APP')
sys.path.insert(0, APP_DIR)

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("2023级自动化 - 高级语言上机实习项目")
        self.root.geometry("950x750")
        self.root.configure(bg="#f0f0f0")

        # 创建主框架（上下分栏）
        main_container = ttk.Frame(root)
        main_container.pack(fill=tk.BOTH, expand=True)

        # 上部主框架
        main_frame = ttk.Frame(main_container, padding="30")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 创建标题
        title_label = ttk.Label(
            main_frame,
            text="高级语言上机实习项目",
            font=("Helvetica", 24, "bold"),
            foreground="#1E90FF"
        )
        title_label.pack(pady=20)



        # 启动模式选择
        mode_frame = ttk.LabelFrame(main_frame, text="启动模式", padding="15")
        mode_frame.pack(fill=tk.X, pady=15)

        self.launch_mode = tk.StringVar(value="gui")

        gui_radio = ttk.Radiobutton(
            mode_frame,
            text="🖥️ GUI 界面（推荐）",
            variable=self.launch_mode,
            value="gui",
            command=self.update_mode
        )
        gui_radio.pack(side=tk.LEFT, padx=20)

        console_radio = ttk.Radiobutton(
            mode_frame,
            text="💻 控制台（传统）",
            variable=self.launch_mode,
            value="console",
            command=self.update_mode
        )
        console_radio.pack(side=tk.LEFT, padx=20)

        # 应用按钮框架
        self.button_frame = ttk.Frame(main_frame)
        self.button_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # 应用配置
        self.apps = [
            {
                "name": "数制转换",
                "console": "APP1.数制转换.py",
                "gui": "APP1.数制转换_gui.py",
                "desc": "将十进制数转换为二进制、八进制和十六进制"
            },
            {
                "name": "猜数游戏",
                "console": "APP2.猜数游戏.py",
                "gui": "APP2.猜数游戏_gui.py",
                "desc": "1-100范围内的猜数字游戏"
            },
            {
                "name": "七段数码管绘制",
                "console": "APP3.七段数码管绘制.py",
                "gui": "APP3.七段数码管绘制_gui.py",
                "desc": "使用Canvas绘制七段数码管显示数字"
            },
            {
                "name": "学生成绩管理系统",
                "console": "APP4.学生成绩管理系统.py",
                "gui": "APP4.学生成绩管理系统_gui.py",
                "desc": "字典操作实现的成绩管理"
            },
            {
                "name": "Excel文件处理",
                "console": "APP5.Excel文件，xls，xlsx处理.py",
                "gui": "APP5.Excel文件，xls，xlsx处理_gui.py",
                "desc": "按部门拆分Excel表格"
            },
        ]

        # 创建按钮
        self.create_buttons()

        # 底部信息
        self.footer_label = ttk.Label(
            main_frame,
            text="点击按钮启动相应的应用程序",
            font=("Helvetica", 10),
            foreground="#999999"
        )
        self.footer_label.pack(pady=20)

        # 配置样式
        style = ttk.Style()
        style.configure(
            "App.TButton",
            font=("Helvetica", 12, "bold"),
            padding=(15, 10),
            width=25
        )

        # 创建日志控制台区域
        log_frame = ttk.LabelFrame(main_container, text="运行日志", padding="10")
        log_frame.pack(fill=tk.X, padx=30, pady=(0, 20))

        # 日志文本框
        log_text_frame = ttk.Frame(log_frame)
        log_text_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(
            log_text_frame,
            height=8,
            wrap=tk.WORD,
            font=("Consolas", 9),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="#ffffff"
        )
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 日志滚动条
        log_scrollbar = ttk.Scrollbar(log_text_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scrollbar.set)
        log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 清空日志按钮
        clear_log_btn = ttk.Button(log_frame, text="清空日志", command=self.clear_log)
        clear_log_btn.pack(side=tk.RIGHT, padx=(10, 0))

        # 配置日志颜色标签
        self.log_text.tag_config("info", foreground="#4ec9b0")
        self.log_text.tag_config("success", foreground="#4caf50")
        self.log_text.tag_config("warning", foreground="#ffeb3b")
        self.log_text.tag_config("error", foreground="#f44336")
        self.log_text.tag_config("default", foreground="#d4d4d4")

        # 记录启动日志
        self.log("系统启动", "高级语言上机实习项目已启动", "success")
        self.log("系统", f"工作目录: {os.getcwd()}", "info")
        self.log("系统", f"APP目录: {APP_DIR}", "info")

    def log(self, tag, message, level="default"):
        """记录日志到控制台"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] [{tag}] {message}\n", level)
        self.log_text.see(tk.END)  # 自动滚动到底部

    def clear_log(self):
        """清空日志"""
        self.log_text.delete(1.0, tk.END)
        self.log("系统", "日志已清空", "info")

    def create_buttons(self):
        """创建应用按钮"""
        # 清空现有按钮
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        mode = self.launch_mode.get()

        for i, app in enumerate(self.apps):
            btn_frame = ttk.Frame(self.button_frame)
            btn_frame.grid(row=i, column=0, sticky="ew", padx=40, pady=10)

            # 确定使用的文件
            if mode == "gui" and app["gui"]:
                filename = app["gui"]
                mode_text = "🖥️"
            else:
                filename = app["console"]
                mode_text = "💻"

            button = ttk.Button(
                btn_frame,
                text=f"▶ {app['name']} {mode_text}",
                command=lambda f=filename, m=mode: self.run_app(f, m),
                style="App.TButton"
            )
            button.pack(side=tk.LEFT, padx=(0, 15))

            desc_label = ttk.Label(
                btn_frame,
                text=app["desc"],
                font=("Helvetica", 10),
                foreground="#666666"
            )
            desc_label.pack(side=tk.LEFT)

        # 配置行权重
        self.button_frame.grid_rowconfigure(5, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)

    def update_mode(self):
        """更新启动模式"""
        mode = self.launch_mode.get()
        mode_text = "GUI 界面" if mode == "gui" else "控制台"
        self.footer_label.config(text=f"当前模式: {mode_text} - 点击按钮启动相应的应用程序")
        self.create_buttons()

    def run_app(self, filename, mode):
        """运行指定的APP文件"""
        filepath = os.path.join(APP_DIR, filename)

        if not os.path.exists(filepath):
            self.log("错误", f"找不到文件: {filename}", "error")
            messagebox.showerror("错误", f"找不到文件: {filename}")
            return

        try:
            self.log("启动", f"正在启动 {filename} ({mode}模式)", "info")
            if mode == "gui":
                # GUI模式使用subprocess运行（不创建新控制台）
                subprocess.Popen([sys.executable, filepath])
            else:
                # 控制台模式创建新控制台
                if sys.platform == 'win32':
                    subprocess.Popen([sys.executable, filepath], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    subprocess.Popen([sys.executable, filepath])
            self.log("启动", f"{filename} 启动成功", "success")
        except Exception as e:
            self.log("错误", f"运行失败: {str(e)}", "error")
            messagebox.showerror("错误", f"运行失败: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
