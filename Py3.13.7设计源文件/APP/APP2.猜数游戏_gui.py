# ==========================================
# App2. 猜数游戏 - GUI版本 (CustomTkinter 美化)
# ==========================================

import sys
import random

# ---- 依赖检查 ----
try:
    import customtkinter as ctk
    from CTkMessagebox import CTkMessagebox
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "CTkMessagebox", "-q"])
    import customtkinter as ctk
    from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---- 设计系统（颜色）----
COLORS = {
    "bg":           "#0A0E1A",
    "card":         "#131B2E",
    "card_border":  "#1E2D4D",
    "primary":      "#6366F1",
    "primary_hover":"#4F46E5",
    "secondary":    "#1E293B",
    "success":      "#10B981",
    "warning":      "#F59E0B",
    "error":        "#EF4444",
    "text":         "#E2E8F0",
    "text_muted":   "#64748B",
    "input_bg":     "#0F172A",
}

# 字体参数（延迟创建，避免 RuntimeError）
FONT_PARAMS = {
    "hero":       {"family": "Microsoft YaHei", "size": 20, "weight": "bold"},
    "heading":    {"family": "Microsoft YaHei", "size": 13, "weight": "bold"},
    "body":       {"family": "Microsoft YaHei", "size": 12},
    "small":      {"family": "Microsoft YaHei", "size": 10},
    "digit":      {"family": "Cascadia Code", "size": 14},
}

PADDING = {
    "xs": 3,
    "sm": 6,
    "md": 10,
    "lg": 14,
    "xl": 18,
}


class GuessNumberApp(ctk.CTk):
    """猜数游戏主窗口"""

    def __init__(self):
        super().__init__()
        self._fonts = {k: ctk.CTkFont(**v) for k, v in FONT_PARAMS.items()}
        self._target = random.randint(1, 100)
        self._attempts  = 0
        self._max_attempts = 10
        self._range_low = 1
        self._range_high = 100
        self._setup_window()
        self._build_ui()

    # ==================== 窗口设置 ====================

    def _setup_window(self):
        self.title("猜数游戏")
        self.geometry("480x500")
        self.minsize(400, 440)
        self.configure(fg_color=COLORS["bg"])
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - 480) // 2
        y = (self.winfo_screenheight() - 500) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=PADDING["lg"], pady=PADDING["md"])

        # ---- 标题行 ----
        header = ctk.CTkFrame(main, fg_color="transparent")
        header.pack(fill="x", pady=(0, PADDING["sm"]))
        ctk.CTkLabel(header, text="🎯  猜数游戏", font=self._fonts["hero"], text_color=COLORS["text"]).pack(side="left")
        ctk.CTkLabel(header, text="  猜 1~100 的整数", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(side="left", padx=(PADDING["sm"], 0), pady=(4, 0))

        # ---- 游戏卡片 ----
        card = ctk.CTkFrame(main, corner_radius=12, fg_color=COLORS["card"], border_color=COLORS["card_border"], border_width=1)
        card.pack(fill="x", pady=(0, PADDING["sm"]))

        # 输入行
        input_row = ctk.CTkFrame(card, fg_color="transparent")
        input_row.pack(fill="x", padx=PADDING["md"], pady=(PADDING["md"], PADDING["xs"]))

        self._entry = ctk.CTkEntry(input_row, placeholder_text="输入 1~100", height=36, font=self._fonts["digit"], fg_color=COLORS["input_bg"])
        self._entry.pack(side="left", fill="x", expand=True, padx=(0, PADDING["xs"]))
        self._entry.focus()
        self._entry.bind("<Return>", lambda _: self._guess())

        ctk.CTkButton(input_row, text="猜一次", width=70, height=36, font=self._fonts["heading"], corner_radius=8, fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"], command=self._guess).pack(side="left")
        ctk.CTkButton(input_row, text="新游戏", width=70, height=36, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["secondary"], hover_color="#334155", command=self._new_game).pack(side="left", padx=(PADDING["xs"], 0))
        ctk.CTkButton(input_row, text="答案", width=50, height=36, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["secondary"], hover_color="#334155", command=self._show_answer).pack(side="left", padx=(PADDING["xs"], 0))

        # 提示行
        hint_row = ctk.CTkFrame(card, fg_color="transparent")
        hint_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["xs"]))

        self._hint_label = ctk.CTkLabel(hint_row, text="等待你的第一次猜测...", font=self._fonts["body"], text_color=COLORS["text_muted"], anchor="w")
        self._hint_label.pack(side="left", fill="x", expand=True)

        self._attempts_label = ctk.CTkLabel(hint_row, text="0/10", font=self._fonts["small"], text_color=COLORS["text_muted"])
        self._attempts_label.pack(side="right")

        # 进度条
        self._progress = ctk.CTkProgressBar(card, height=4, corner_radius=2)
        self._progress.set(0)
        self._progress.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["xs"]))

        # 范围行
        range_row = ctk.CTkFrame(card, fg_color="transparent")
        range_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["md"]))

        self._range_label = ctk.CTkLabel(range_row, text=f"范围: {self._range_low} ~ {self._range_high}", font=self._fonts["small"], text_color=COLORS["text_muted"], anchor="w")
        self._range_label.pack(side="left")

        # ---- 历史卡片 ----
        card_hist = ctk.CTkFrame(main, corner_radius=12, fg_color=COLORS["card"], border_color=COLORS["card_border"], border_width=1)
        card_hist.pack(fill="both", expand=True, pady=(0, 0))

        ctk.CTkLabel(card_hist, text="📝  猜测历史", font=self._fonts["heading"], text_color=COLORS["text"]).pack(anchor="w", padx=PADDING["md"], pady=(PADDING["sm"], PADDING["xs"]))

        self._history_text = ctk.CTkTextbox(card_hist, font=self._fonts["small"], fg_color=COLORS["input_bg"])
        self._history_text.pack(fill="both", expand=True, padx=PADDING["md"], pady=(0, PADDING["md"]))
        self._history_text.insert("0.0", "暂无猜测记录\n")
        self._history_text.configure(state="disabled")

    # ==================== 游戏逻辑 ====================

    def _guess(self):
        guess_str = self._entry.get().strip()
        if not guess_str:
            return

        try:
            guess = int(guess_str)
            if not (1 <= guess <= 100):
                raise ValueError
        except ValueError:
            CTkMessagebox(title="错误", message="请输入 1-100 之间的整数！", icon="warning")
            return

        self._attempts += 1
        progress = min(self._attempts / self._max_attempts, 1.0)
        self._progress.set(progress)
        self._attempts_label.configure(text=f"{self._attempts}/{self._max_attempts}")

        self._history_text.configure(state="normal")
        if self._attempts == 1:
            self._history_text.delete("0.0", "end")
        self._history_text.insert("end", f"第{self._attempts}次: {guess} - ")
        self._history_text.configure(state="disabled")
        self._history_text.see("end")

        if guess == self._target:
            self._on_win()
        elif guess < self._target:
            self._hint_label.configure(text="📉  猜小了，再大一点！", text_color=COLORS["warning"])
            self._range_low = max(self._range_low, guess + 1)
            self._update_range()
            self._history_text.configure(state="normal")
            self._history_text.insert("end", "太小了\n")
            self._history_text.configure(state="disabled")
        else:
            self._hint_label.configure(text="📈  猜大了，再小一点！", text_color=COLORS["warning"])
            self._range_high = min(self._range_high, guess - 1)
            self._update_range()
            self._history_text.configure(state="normal")
            self._history_text.insert("end", "太大了\n")
            self._history_text.configure(state="disabled")

        if self._attempts >= self._max_attempts and guess != self._target:
            self._on_lose()

        self._entry.delete(0, "end")

    def _on_win(self):
        self._hint_label.configure(text=f"🎉  恭喜猜对了！答案是 {self._target}", text_color=COLORS["success"])
        self._entry.configure(state="disabled")
        self._history_text.configure(state="normal")
        self._history_text.insert("end", "猜对了！\n")
        self._history_text.configure(state="disabled")
        CTkMessagebox(title="胜利", message=f"恭喜！第 {self._attempts} 次猜中 {self._target}！", icon="check")

    def _on_lose(self):
        self._hint_label.configure(text=f"💔  游戏结束！答案是 {self._target}", text_color=COLORS["error"])
        self._entry.configure(state="disabled")
        CTkMessagebox(title="失败", message=f"次数用完！答案是 {self._target}", icon="cancel")

    def _new_game(self):
        self._target = random.randint(1, 100)
        self._attempts = 0
        self._range_low = 1
        self._range_high = 100
        self._entry.configure(state="normal")
        self._entry.delete(0, "end")
        self._entry.focus()
        self._hint_label.configure(text="新游戏开始，等待猜测...", text_color=COLORS["text_muted"])
        self._attempts_label.configure(text="0/10")
        self._range_label.configure(text=f"范围: {self._range_low} ~ {self._range_high}")
        self._progress.set(0)
        self._history_text.configure(state="normal")
        self._history_text.delete("0.0", "end")
        self._history_text.insert("0.0", "新游戏开始\n")
        self._history_text.configure(state="disabled")

    def _show_answer(self):
        CTkMessagebox(title="答案", message=f"答案是: {self._target}", icon="info")

    def _update_range(self):
        self._range_label.configure(text=f"范围: {self._range_low} ~ {self._range_high}")


# ==================== 入口 ====================

if __name__ == "__main__":
    app = GuessNumberApp()
    app.mainloop()
