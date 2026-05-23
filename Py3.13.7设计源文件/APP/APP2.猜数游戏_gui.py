# ==========================================
# App2. 猜数游戏 - GUI版本 (CustomTkinter 美化)
# ==========================================

import sys
import random

# ── 依赖检查 ──
try:
    import customtkinter as ctk
    from CTkMessagebox import CTkMessagebox
except ImportError:
    import subprocess, sys as _sys
    subprocess.check_call([_sys.executable, "-m", "pip", "install", "customtkinter", "CTkMessagebox", "-q"])
    import customtkinter as ctk
    from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class GuessNumberApp(ctk.CTk):
    """猜数游戏主应用"""

    def __init__(self):
        super().__init__()
        self._target = random.randint(1, 100)
        self._count  = 0
        self._setup_window()
        self._build_ui()

    # ==================== 窗口 ====================

    def _setup_window(self):
        self.title("猜数游戏")
        self.geometry("500x620")
        self.minsize(420, 500)
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - 500) // 2
        y = (self.winfo_screenheight() - 620) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=(15, 10))

        # ── 标题 ──
        ctk.CTkLabel(
            scroll, text="🎯  猜数游戏",
            font=ctk.CTkFont(size=26, weight="bold"),
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            scroll, text="我想好了一个 1 ~ 100 之间的整数，来猜猜看！",
            font=ctk.CTkFont(size=13), text_color="gray60",
        ).pack(pady=(0, 15))

        # ── 输入卡片 ──
        card = ctk.CTkFrame(scroll, corner_radius=14)
        card.pack(fill="x", pady=8, padx=4)

        ctk.CTkLabel(card, text="📝  你的猜测", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=16, pady=(12, 6))

        input_row = ctk.CTkFrame(card, fg_color="transparent")
        input_row.pack(fill="x", padx=16, pady=(0, 12))

        self._entry = ctk.CTkEntry(
            input_row, placeholder_text="输入 1 ~ 100 之间的数字", height=38,
            font=ctk.CTkFont(size=14),
        )
        self._entry.pack(fill="x", expand=True)
        self._entry.focus()
        self._entry.bind("<Return>", lambda _: self._guess())

        # ── 结果卡片 ──
        self._result_card = ctk.CTkFrame(scroll, corner_radius=14)
        self._result_card.pack(fill="x", pady=8, padx=4)

        ctk.CTkLabel(self._result_card, text="📊  当前提示", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=16, pady=(12, 6))

        self._hint_label = ctk.CTkLabel(
            self._result_card, text="等待你的第一次猜测...",
            font=ctk.CTkFont(size=15), text_color="gray50",
        )
        self._hint_label.pack(padx=16, pady=(0, 14))

        # ── 统计卡片 ──
        stats = ctk.CTkFrame(scroll, corner_radius=14)
        stats.pack(fill="x", pady=8, padx=4)

        ctk.CTkLabel(stats, text="📈  统计信息", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=16, pady=(12, 6))

        self._count_label = ctk.CTkLabel(
            stats, text="已猜次数：0  次",
            font=ctk.CTkFont(size=13),
        )
        self._count_label.pack(anchor="w", padx=16, pady=(0, 14))

        # ── 按钮区 ──
        btn_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        btn_frame.pack(pady=(10, 20))

        ctk.CTkButton(
            btn_frame, text="▶  猜  一  次", width=160, height=42,
            font=ctk.CTkFont(size=15, weight="bold"),
            corner_radius=10, command=self._guess,
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            btn_frame, text="🔄  重新开始", width=160, height=42,
            font=ctk.CTkFont(size=15),
            fg_color="gray30", hover_color="gray40",
            corner_radius=10, command=self._new_game,
        ).pack(side="left", padx=10)

    # ==================== 逻辑 ====================

    def _guess(self):
        val = self._entry.get().strip()
        if not val.isdigit():
            self._show_hint("⚠️ 请输入有效的数字！", "#FF8C00")
            return

        num = int(val)
        if num < 1 or num > 100:
            self._show_hint("⚠️ 数字必须在 1 ~ 100 之间！", "#FF8C00")
            return

        self._count += 1
        self._count_label.configure(text=f"已猜次数：{self._count}  次")
        self._entry.delete(0, "end")

        if num == self._target:
            self._on_win()
        elif num < self._target:
            self._show_hint("📉  猜小了，再大一点！", "#FF8C00")
        else:
            self._show_hint("📈  猜大了，再小一点！", "#FF8C00")

    def _on_win(self):
        self._show_hint(f"🎉  恭喜你猜对了！答案就是  {self._target}", "#1E90")
        CTkMessagebox(
            title="🎊 恭喜！",
            message=f"你用了  {self._count}  次猜对了数字  {self._target}！",
            icon="check",
        )
        self._entry.configure(state="disabled")

    def _new_game(self):
        self._target = random.randint(1, 100)
        self._count  = 0
        self._count_label.configure(text="已猜次数：0  次")
        self._show_hint("🆕 新游戏已开始，等待你的猜测...", "gray50")
        self._entry.configure(state="normal")
        self._entry.delete(0, "end")
        self._entry.focus()

    def _show_hint(self, text: str, color: str):
        self._hint_label.configure(text=text, text_color=color)


# ==================== 入口 ====================

if __name__ == "__main__":
    GuessNumberApp().mainloop()
