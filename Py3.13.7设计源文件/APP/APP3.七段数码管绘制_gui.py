# ==========================================
# App3. 七段数码管绘制 - GUI版本 (CustomTkinter 美化)
# ==========================================

import sys
import os
import tkinter as tk
# ── 依赖检查 ──
try:
    import customtkinter as ctk
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "-q"])
    import customtkinter as ctk

from tkinter import colorchooser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── 七段数码管定义 ──
# 七段数码管段定义：0=灭，1=亮（顺序：上、右上、右下、下、左上、左下、中）
SEGMENTS = {
    '0': [1, 1, 1, 1, 1, 1, 0],
    '1': [0, 1, 1, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1],
    '3': [1, 1, 1, 1, 0, 0, 1],
    '4': [0, 1, 1, 0, 0, 1, 1],
    '5': [1, 0, 1, 1, 0, 1, 1],
    '6': [1, 0, 1, 1, 1, 1, 1],
    '7': [1, 1, 1, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1],
}


class SevenSegmentApp(ctk.CTk):
    """七段数码管绘制主应用"""

    def __init__(self):
        super().__init__()
        self._segment_color = "#1E90FF"
        self._setup_window()
        self._build_ui()

    # ==================== 窗口设置 ====================

    def _setup_window(self):
        self.title("七段数码管绘制")
        self.geometry("820x680")
        self.minsize(700, 580)
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 820) // 2
        y = (self.winfo_screenheight() - 680) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=16, pady=(12, 8))

        # ── 标题 ──
        ctk.CTkLabel(
            scroll, text="🔢  七段数码管绘制",
            font=ctk.CTkFont(size=24, weight="bold"),
        ).pack(pady=(8, 4))

        ctk.CTkLabel(
            scroll, text="输入数字，实时绘制七段数码管",
            font=ctk.CTkFont(size=12), text_color="gray60",
        ).pack(pady=(0, 12))

        # ── 控制卡片 ──
        self._build_control_card(scroll)

        # ── 画布卡片 ──
        self._build_canvas_card(scroll)

    # ── 控制卡片 ──
    def _build_control_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="x", pady=6, padx=2)

        ctk.CTkLabel(
            card, text="🎛  控制面板",
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(anchor="w", padx=14, pady=(10, 6))

        # 第一行：输入 + 按钮
        row1 = ctk.CTkFrame(card, fg_color="transparent")
        row1.pack(fill="x", padx=14, pady=4)

        ctk.CTkLabel(row1, text="数字", width=40, anchor="w").pack(side="left")
        self._entry = ctk.CTkEntry(
            row1, placeholder_text="输入数字，如 20260107", height=34
        )
        self._entry.pack(side="left", fill="x", expand=True, padx=8)
        self._entry.insert(0, "20260107")
        self._entry.bind("<Return>", lambda _: self._draw())

        ctk.CTkButton(
            row1, text="▶ 绘制", width=90, height=34,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._draw,
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            row1, text="✕ 清空", width=90, height=34,
            fg_color="gray30", hover_color="gray40",
            command=lambda: self._canvas.delete("all"),
        ).pack(side="left", padx=4)

        # 第二行：颜色 + 粗细
        row2 = ctk.CTkFrame(card, fg_color="transparent")
        row2.pack(fill="x", padx=14, pady=4)

        ctk.CTkButton(
            row2, text="🎨 段颜色", width=100, height=30,
            command=self._choose_color,
        ).pack(side="left", padx=(0, 8))

        self._color_btn = ctk.CTkButton(
            row2, text=self._segment_color,
            width=80, height=30, fg_color=self._segment_color,
            text_color="white", command=self._choose_color,
        )
        self._color_btn.pack(side="left")

        ctk.CTkLabel(row2, text="  粗细", width=50, anchor="w").pack(side="left", padx=(16, 4))
        self._width_var = ctk.IntVar(value=8)
        width_slider = ctk.CTkSlider(
            row2, from_=3, to=20, variable=self._width_var, width=120
        )
        width_slider.pack(side="left", padx=4)
        self._width_label = ctk.CTkLabel(row2, text="8", width=30)
        self._width_label.pack(side="left")
        self._width_var.trace_add("write", self._on_width_change)

        # 第三行：动画开关 + 速度
        row3 = ctk.CTkFrame(card, fg_color="transparent")
        row3.pack(fill="x", padx=14, pady=(4, 10))

        self._animate_var = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            row3, text="🎬 绘制动画", variable=self._animate_var,
        ).pack(side="left", padx=(0, 12))

        ctk.CTkLabel(row3, text="速度", width=40, anchor="w").pack(side="left")
        self._speed_var = ctk.IntVar(value=80)
        speed_slider = ctk.CTkSlider(
            row3, from_=10, to=400, variable=self._speed_var, width=100
        )
        speed_slider.pack(side="left", padx=4)
        self._speed_label = ctk.CTkLabel(row3, text="80ms", width=50)
        self._speed_label.pack(side="left")
        self._speed_var.trace_add("write", self._on_speed_change)

    # ── 画布卡片 ──
    def _build_canvas_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="both", expand=True, pady=6, padx=2)

        ctk.CTkLabel(
            card, text="🖼  显示区域",
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(anchor="w", padx=14, pady=(10, 6))

        # customtkinter 没有 CTkCanvas，用 tk.Canvas + CTkFrame 包裹
        canvas_frame = ctk.CTkFrame(card, corner_radius=8, fg_color="gray10")
        canvas_frame.pack(fill="both", expand=True, padx=14, pady=(0, 10))
        self._canvas = tk.Canvas(canvas_frame, bg="#1a1a1a", highlightthickness=0)
        self._canvas.pack(fill="both", expand=True, padx=4, pady=4)

    # ==================== 回调 ====================

    def _on_width_change(self, *args):
        self._width_label.configure(text=str(self._width_var.get()))

    def _on_speed_change(self, *args):
        self._speed_label.configure(text=f"{self._speed_var.get()}ms")

    def _choose_color(self):
        color = colorchooser.askcolor(title="选择段颜色", initialcolor=self._segment_color)
        if color and color[1]:
            self._segment_color = color[1]
            self._color_btn.configure(text=color[1], fg_color=color[1])

    # ==================== 绘制逻辑 ====================

    def _draw(self):
        number = self._entry.get().strip()
        if not number.isdigit():
            return
        self._canvas.delete("all")
        w = self._canvas.winfo_width() or 600
        h = self._canvas.winfo_height() or 300
        digit_w = w // max(len(number), 1)
        seg_len = min(digit_w // 2, h // 3)
        seg_w = self._width_var.get()

        if self._animate_var.get():
            self._draw_animated(number, digit_w, seg_len, seg_w)
        else:
            for i, ch in enumerate(number):
                self._draw_digit(i, ch, digit_w, seg_len, seg_w)

    def _draw_digit(self, index, digit, digit_w, seg_len, seg_w):
        x = index * digit_w + digit_w // 2
        y = self._canvas.winfo_height() // 2
        segs = SEGMENTS.get(digit, [0]*7)
        for i, state in enumerate(segs):
            if state:
                self._draw_segment(x, y, i, seg_len, seg_w)

    def _draw_animated(self, number, digit_w, seg_len, seg_w):
        def step(idx=0, seg_idx=0):
            if idx >= len(number):
                return
            digit = number[idx]
            segs = SEGMENTS.get(digit, [0]*7)
            if seg_idx < 7:
                if segs[seg_idx]:
                    x = idx * digit_w + digit_w // 2
                    y = self._canvas.winfo_height() // 2
                    self._draw_segment(x, y, seg_idx, seg_len, seg_w)
                self.after(self._speed_var.get(), lambda: step(idx, seg_idx + 1))
            else:
                self.after(10, lambda: step(idx + 1, 0))
        step()

    def _draw_segment(self, cx, cy, seg, seg_len, seg_w):
        """在画布上绘制一段"""
        h = seg_len
        w = seg_w
        gap = seg_w + 2

        positions = {
            0: (cx - h//2, cy - h - gap*2, cx + h//2, cy - h - gap*2),
            1: (cx + h//2 + gap, cy - h - gap, cx + h//2 + gap, cy - gap//2),
            2: (cx + h//2 + gap, cy + gap//2, cx + h//2 + gap, cy + h + gap),
            3: (cx - h//2, cy + h + gap*2, cx + h//2, cy + h + gap*2),
            4: (cx - h//2 - gap, cy + gap//2, cx - h//2 - gap, cy + h + gap),
            5: (cx - h//2 - gap, cy - h - gap, cx - h//2 - gap, cy - gap//2),
            6: (cx - h//2, cy - gap//2, cx + h//2, cy - gap//2),
        }

        if seg in positions:
            x1, y1, x2, y2 = positions[seg]
            self._canvas.create_line(
                x1, y1, x2, y2,
                width=seg_w, fill=self._segment_color, capstyle="round"
            )


# ==================== 入口 ====================

if __name__ == "__main__":
    SevenSegmentApp().mainloop()
