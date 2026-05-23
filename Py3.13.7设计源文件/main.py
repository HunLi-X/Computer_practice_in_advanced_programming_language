# ==========================================
# 主程序 - APP 集合启动器 (CustomTkinter 美化版)
# 功能: 一键启动5个Python应用程序，支持GUI和控制台模式
# ==========================================

import sys
import os
import subprocess
import datetime
import threading

# ── 检查依赖 ──
try:
    import customtkinter as ctk
    from CTkMessagebox import CTkMessagebox
except ImportError:
    print("缺少依赖库, 正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "CTkMessagebox", "-q"])
    import customtkinter as ctk
    from CTkMessagebox import CTkMessagebox

# ── 路径配置 ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, "APP")
sys.path.insert(0, APP_DIR)

# ── 应用列表 ──
APPS = [
    {
        "name": "数制转换",
        "icon": "🔢",
        "console": "APP1.数制转换.py",
        "gui": "APP1.数制转换_gui.py",
        "desc": "任意进制转换(2-36)",
        "color": "#6366f1",
    },
    {
        "name": "猜数游戏",
        "icon": "🎯",
        "console": "APP2.猜数游戏.py",
        "gui": "APP2.猜数游戏_gui.py",
        "desc": "1-100猜数字游戏",
        "color": "#f59e0b",
    },
    {
        "name": "数码管绘制",
        "icon": "🖥️",
        "console": "APP3.七段数码管绘制.py",
        "gui": "APP3.七段数码管绘制_gui.py",
        "desc": "七段数码管显示",
        "color": "#10b981",
    },
    {
        "name": "成绩管理",
        "icon": "📊",
        "console": "APP4.学生成绩管理系统.py",
        "gui": "APP4.学生成绩管理系统_gui.py",
        "desc": "学生成绩管理系统",
        "color": "#8b5cf6",
    },
    {
        "name": "Excel处理",
        "icon": "📁",
        "console": "APP5.Excel文件，xls，xlsx处理.py",
        "gui": "APP5.Excel文件，xls，xlsx处理_gui.py",
        "desc": "按部门拆分Excel",
        "color": "#ef4444",
    },
]


class MainApp(ctk.CTk):
    """主应用窗口"""

    def __init__(self):
        super().__init__()

        # ── 窗口设置 ──
        self.title("高级语言上机实习项目")
        self.geometry("1050x720")
        self.minsize(950, 650)

        # 居中显示
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 1050) // 2
        y = (self.winfo_screenheight() - 720) // 2
        self.geometry(f"+{x}+{y}")

        # ── 主题配置 ──
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ── 状态变量 ──
        self.launch_mode = ctk.StringVar(value="gui")
        self.running_count = 0

        # ── 构建 UI ──
        self._build_header()
        self._build_mode_selector()
        self._build_app_cards()
        self._build_log_panel()
        self._build_footer()

        # ── 初始日志 ──
        self.log("🌐 系统", "项目启动成功", "success")
        self.log("📂 系统", f"APP 目录: {APP_DIR}", "info")

    # ==================== 构建 UI ====================

    def _build_header(self):
        """顶部标题栏"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(25, 5))

        ctk.CTkLabel(
            header,
            text="⚡ 高级语言上机实习项目",
            font=ctk.CTkFont(size=28, weight="bold"),
        ).pack(side="left")

        # 主题切换
        self.theme_btn = ctk.CTkButton(
            header,
            text="☀️ 浅色",
            width=100,
            command=self._toggle_theme,
            fg_color="transparent",
            border_width=1,
        )
        self.theme_btn.pack(side="right")

    def _build_mode_selector(self):
        """模式选择栏"""
        bar = ctk.CTkFrame(self, fg_color="transparent")
        bar.pack(fill="x", padx=30, pady=(10, 5))

        ctk.CTkLabel(bar, text="启动模式", font=ctk.CTkFont(size=13, weight="bold")).pack(
            side="left", padx=(0, 15)
        )

        modes = [
            ("🖥️  GUI 模式 (推荐)", "gui"),
            ("💻  控制台模式", "console"),
        ]
        for text, value in modes:
            ctk.CTkRadioButton(
                bar,
                text=text,
                variable=self.launch_mode,
                value=value,
                command=self._on_mode_change,
                font=ctk.CTkFont(size=13),
            ).pack(side="left", padx=15)

        self.mode_hint = ctk.CTkLabel(
            bar,
            text="",
            font=ctk.CTkFont(size=12),
            text_color="gray",
        )
        self.mode_hint.pack(side="right")

    def _build_app_cards(self):
        """应用卡片区"""
        container = ctk.CTkScrollableFrame(
            self, fg_color="transparent", height=280
        )
        container.pack(fill="both", expand=True, padx=30, pady=10)

        self.card_frames = []
        for i, app in enumerate(APPS):
            card = ctk.CTkFrame(container, fg_color=("gray95", "gray17"), corner_radius=12)
            card.pack(fill="x", pady=6, padx=2)

            # 左侧图标区
            icon_frame = ctk.CTkFrame(
                card, width=56, height=56, corner_radius=12, fg_color=app["color"]
            )
            icon_frame.pack(side="left", padx=(15, 15), pady=12)
            icon_frame.pack_propagate(False)
            ctk.CTkLabel(icon_frame, text=app["icon"], font=ctk.CTkFont(size=22)).pack(
                expand=True
            )

            # 中间文字
            text_col = ctk.CTkFrame(card, fg_color="transparent")
            text_col.pack(side="left", fill="both", expand=True, pady=8)
            ctk.CTkLabel(
                text_col,
                text=app["name"],
                font=ctk.CTkFont(size=15, weight="bold"),
            ).pack(anchor="w")
            ctk.CTkLabel(
                text_col,
                text=app["desc"],
                font=ctk.CTkFont(size=12),
                text_color="gray",
            ).pack(anchor="w")

            # 右侧按钮
            btn_col = ctk.CTkFrame(card, fg_color="transparent")
            btn_col.pack(side="right", padx=15, pady=12)

            ctk.CTkButton(
                btn_col,
                text="▶ 启动",
                width=100,
                height=34,
                font=ctk.CTkFont(size=13, weight="bold"),
                corner_radius=8,
                command=lambda a=app, i=i: self._run_app_thread(a),
            ).pack(side="left")

            self.card_frames.append(card)

    def _build_log_panel(self):
        """底部日志面板"""
        log_frame = ctk.CTkFrame(self, corner_radius=12)
        log_frame.pack(fill="both", padx=30, pady=(8, 5), ipadx=4, ipady=4)

        # 标题行
        title_row = ctk.CTkFrame(log_frame, fg_color="transparent")
        title_row.pack(fill="x", padx=12, pady=(8, 2))

        ctk.CTkLabel(
            title_row,
            text="📋 运行日志",
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(side="left")

        ctk.CTkButton(
            title_row,
            text="清空",
            width=60,
            height=26,
            font=ctk.CTkFont(size=11),
            command=self.clear_log,
        ).pack(side="right")

        # 日志文本框
        self.log_box = ctk.CTkTextbox(
            log_frame,
            height=150,
            font=ctk.CTkFont(family="Consolas", size=12),
            wrap="word",
        )
        self.log_box.pack(fill="both", expand=True, padx=12, pady=(2, 10))
        self.log_box.configure(state="disabled")

    def _build_footer(self):
        """底部状态栏"""
        footer = ctk.CTkFrame(self, fg_color="transparent", height=30)
        footer.pack(fill="x", padx=30, pady=(2, 12))

        self.status_label = ctk.CTkLabel(
            footer,
            text="🟢 就绪 — 等待操作",
            font=ctk.CTkFont(size=11),
            text_color="gray",
        )
        self.status_label.pack(side="left")

        ctk.CTkLabel(
            footer,
            text="Python 3.13 | CustomTkinter",
            font=ctk.CTkFont(size=11),
            text_color="gray",
        ).pack(side="right")

    # ==================== 核心逻辑 ====================

    def _toggle_theme(self):
        """切换明暗主题"""
        current = ctk.get_appearance_mode()
        if current == "Dark":
            ctk.set_appearance_mode("light")
            self.theme_btn.configure(text="🌙 深色")
        else:
            ctk.set_appearance_mode("dark")
            self.theme_btn.configure(text="☀️ 浅色")

    def _on_mode_change(self):
        """模式切换"""
        mode = self.launch_mode.get()
        label = "GUI 模式" if mode == "gui" else "控制台模式"
        self.mode_hint.configure(text=f"当前: {label}")
        self.log("⚙️ 系统", f"切换到 {label}", "info")

    def _run_app_thread(self, app):
        """线程化启动 APP（避免阻塞 UI）"""
        threading.Thread(target=self._run_app, args=(app,), daemon=True).start()

    def _run_app(self, app):
        """启动单个 APP"""
        mode = self.launch_mode.get()
        filename = app["gui"] if mode == "gui" else app["console"]
        filepath = os.path.join(APP_DIR, filename)

        if not os.path.exists(filepath):
            self.log("❌ 错误", f"文件不存在: {filename}", "error")
            self.after(0, lambda: CTkMessagebox(
                title="错误", message=f"找不到文件:\n{filename}", icon="cancel"
            ))
            return

        self.running_count += 1
        self._update_status()

        self.log("🚀", f"{app['icon']} {app['name']} — {filename}", "info")

        try:
            if mode == "gui":
                subprocess.Popen([sys.executable, filepath])
            else:
                if sys.platform == "win32":
                    subprocess.Popen(
                        [sys.executable, filepath],
                        creationflags=subprocess.CREATE_NEW_CONSOLE,
                    )
                else:
                    subprocess.Popen([sys.executable, filepath])
            self.log("✅", f"{app['name']} 启动成功", "success")
        except Exception as e:
            self.log("❌", f"{app['name']} 启动失败: {e}", "error")
            self.after(0, lambda: CTkMessagebox(
                title="错误", message=f"启动失败:\n{e}", icon="cancel"
            ))

        self.running_count = max(0, self.running_count - 1)
        self._update_status()

    def _update_status(self):
        """更新状态栏"""
        if self.running_count > 0:
            self.status_label.configure(
                text=f"🔄 运行中 — {self.running_count} 个进程活跃",
                text_color="#f59e0b",
            )
        else:
            self.status_label.configure(
                text="🟢 就绪 — 等待操作", text_color="gray"
            )

    # ==================== 日志系统 ====================

    def log(self, prefix, message, level="default"):
        """写入日志"""
        now = datetime.datetime.now().strftime("%H:%M:%S")
        line = f"[{now}] {prefix} {message}\n"

        self.log_box.configure(state="normal")
        self.log_box.insert("end", line)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def clear_log(self):
        """清空日志"""
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.log("🧹 系统", "日志已清空", "info")


# ==================== 入口 ====================

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()