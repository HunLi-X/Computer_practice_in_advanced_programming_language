# ==========================================
# App3. 七段数码管绘制 - GUI版本 (CustomTkinter 美化)
# ==========================================

import sys
import os
import tkinter as tk
import time as _time

# ---- 依赖检查 ----
try:
    import customtkinter as ctk
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "-q"])
    import customtkinter as ctk

from tkinter import colorchooser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---- 设计系统 ----
COLORS = {
    "bg":           "#0A0E1A",
    "card":         "#131B2E",
    "card_border":  "#1E2D4D",
    "primary":      "#6366F1",
    "primary_hover":"#4F46E5",
    "secondary":    "#1E293B",
    "accent":       "#818CF8",
    "success":      "#10B981",
    "warning":      "#F59E0B",
    "error":        "#EF4444",
    "text":         "#E2E8F0",
    "text_muted":   "#64748B",
    "input_bg":     "#0F172A",
    "canvas_bg":    "#0D1117",
}

FONT_PARAMS = {
    "hero":       {"family": "Microsoft YaHei", "size": 18, "weight": "bold"},
    "heading":    {"family": "Microsoft YaHei", "size": 12, "weight": "bold"},
    "body":       {"family": "Microsoft YaHei", "size": 11},
    "small":      {"family": "Microsoft YaHei", "size": 10},
}

PADDING = {"xs": 3, "sm": 6, "md": 10, "lg": 14}

# ---- 七段数码管定义 ----
SEGMENTS = {
    '0': [1,1,1,1,1,1,0], '1': [0,1,1,0,0,0,0], '2': [1,1,0,1,1,0,1],
    '3': [1,1,1,1,0,0,1], '4': [0,1,1,0,0,1,1], '5': [1,0,1,1,0,1,1],
    '6': [1,0,1,1,1,1,1], '7': [1,1,1,0,0,0,0], '8': [1,1,1,1,1,1,1],
    '9': [1,1,1,1,0,1,1],
    'A': [1,1,1,0,1,1,1], 'B': [0,0,1,1,1,1,1], 'C': [1,0,0,1,1,1,0],
    'D': [0,1,1,1,1,0,1], 'E': [1,0,0,1,1,1,1], 'F': [1,0,0,0,1,1,1],
    ':': [0,0,0,0,0,0,0],
}


class SevenSegmentApp(ctk.CTk):
    """七段数码管绘制主窗口"""

    def __init__(self):
        super().__init__()
        self._fonts = {k: ctk.CTkFont(**v) for k, v in FONT_PARAMS.items()}
        self._on_color = "#FF4444"
        self._bg_color = COLORS["canvas_bg"]
        self._time_job = None
        self._setup_window()
        self._build_ui()

    def _setup_window(self):
        self.title("七段数码管绘制")
        self.geometry("900x560")
        self.minsize(740, 440)
        self.configure(fg_color=COLORS["bg"])
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 900) // 2
        y = (self.winfo_screenheight() - 560) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        # 左右分栏
        sidebar = ctk.CTkFrame(self, width=260, corner_radius=0, fg_color=COLORS["card"])
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.pack(side="right", fill="both", expand=True)

        self._build_sidebar(sidebar)
        self._build_canvas(right)

    # ---- 左侧控制栏 ----
    def _build_sidebar(self, parent):
        # 标题
        title_frame = ctk.CTkFrame(parent, fg_color="transparent")
        title_frame.pack(fill="x", padx=PADDING["md"], pady=(PADDING["md"], PADDING["sm"]))
        ctk.CTkLabel(title_frame, text="七段数码管", font=self._fonts["hero"], text_color=COLORS["text"]).pack(anchor="w")
        ctk.CTkLabel(title_frame, text="支持 0-9 / A-F / 时钟", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(anchor="w", pady=(2, 0))

        ctk.CTkFrame(parent, height=1, fg_color=COLORS["card_border"]).pack(fill="x", padx=PADDING["md"], pady=PADDING["xs"])

        inner = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=PADDING["xs"])
        inner._scrollbar.configure(width=4)

        # ---- 输入 ----
        self._section_label(inner, "输入")
        self._entry = ctk.CTkEntry(inner, placeholder_text="0-9 / A-F", height=30, font=self._fonts["body"], fg_color=COLORS["input_bg"])
        self._entry.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["xs"]))
        self._entry.insert(0, "0123456789")
        self._entry.bind("<KeyRelease>", lambda _: self._draw())
        self._entry.bind("<Return>", lambda _: self._draw())

        btn_row = ctk.CTkFrame(inner, fg_color="transparent")
        btn_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))
        ctk.CTkButton(btn_row, text="绘制", height=30, font=self._fonts["heading"], corner_radius=8, fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"], command=self._draw).pack(side="left", fill="x", expand=True, padx=(0, PADDING["xs"]))
        ctk.CTkButton(btn_row, text="清空", height=30, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["secondary"], hover_color="#334155", command=lambda: self._canvas.delete("all")).pack(side="left")

        # ---- 时钟模式 ----
        self._section_label(inner, "时钟模式")
        self._time_mode = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(inner, text="启用时钟", variable=self._time_mode, font=self._fonts["body"], corner_radius=4, checkbox_width=18, checkbox_height=18, command=self._toggle_time_mode).pack(anchor="w", padx=PADDING["md"], pady=(0, PADDING["xs"]))

        fmt_row = ctk.CTkFrame(inner, fg_color="transparent")
        fmt_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))
        ctk.CTkLabel(fmt_row, text="格式", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(side="left")
        self._time_format = ctk.CTkComboBox(fmt_row, width=120, values=["HH:MM:SS", "HH:MM", "YYYY-MM-DD"], font=self._fonts["small"], dropdown_font=self._fonts["small"], state="readonly")
        self._time_format.pack(side="left", padx=PADDING["sm"])
        self._time_format.set("HH:MM:SS")
        self._time_format.configure(command=lambda _: self._draw())

        self._time_label = ctk.CTkLabel(inner, text="", font=self._fonts["small"], text_color=COLORS["accent"])
        self._time_label.pack(anchor="w", padx=PADDING["md"], pady=(0, PADDING["sm"]))

        # ---- 段颜色 ----
        self._section_label(inner, "段颜色")
        color_row = ctk.CTkFrame(inner, fg_color="transparent")
        color_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))
        self._color_btn = ctk.CTkButton(color_row, text=self._on_color, height=28, fg_color=self._on_color, text_color="white", corner_radius=6, font=self._fonts["small"], command=self._choose_color)
        self._color_btn.pack(side="left", fill="x", expand=True, padx=(0, PADDING["xs"]))
        ctk.CTkButton(color_row, text="选择", width=50, height=28, font=self._fonts["body"], corner_radius=6, command=self._choose_color).pack(side="left")

        # ---- 背景颜色 ----
        self._section_label(inner, "背景颜色")
        bg_row = ctk.CTkFrame(inner, fg_color="transparent")
        bg_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))
        self._bg_btn = ctk.CTkButton(bg_row, text=self._bg_color, height=28, fg_color=self._bg_color, text_color="white", corner_radius=6, font=self._fonts["small"], command=self._choose_bg_color)
        self._bg_btn.pack(side="left", fill="x", expand=True, padx=(0, PADDING["xs"]))
        ctk.CTkButton(bg_row, text="选择", width=50, height=28, font=self._fonts["body"], corner_radius=6, command=self._choose_bg_color).pack(side="left")

        # ---- 线条粗细 ----
        self._section_label(inner, "线条粗细")
        w_row = ctk.CTkFrame(inner, fg_color="transparent")
        w_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))
        self._width_var = ctk.IntVar(value=8)
        ctk.CTkSlider(w_row, from_=3, to=20, variable=self._width_var, height=16, corner_radius=4).pack(side="left", fill="x", expand=True, padx=(0, PADDING["xs"]))
        self._width_label = ctk.CTkLabel(w_row, text="8", width=24, font=self._fonts["small"])
        self._width_label.pack(side="left")
        self._width_var.trace_add("write", self._on_width_change)

        # ---- 动画 ----
        self._section_label(inner, "动画")
        self._animate_var = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(inner, text="绘制动画", variable=self._animate_var, font=self._fonts["body"], corner_radius=4, checkbox_width=18, checkbox_height=18).pack(anchor="w", padx=PADDING["md"], pady=(0, PADDING["xs"]))

        s_row = ctk.CTkFrame(inner, fg_color="transparent")
        s_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["md"]))
        ctk.CTkLabel(s_row, text="速度", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(side="left")
        self._speed_var = ctk.IntVar(value=80)
        ctk.CTkSlider(s_row, from_=10, to=400, variable=self._speed_var, height=16, corner_radius=4).pack(side="left", fill="x", expand=True, padx=PADDING["xs"])
        self._speed_label = ctk.CTkLabel(s_row, text="80ms", width=40, font=self._fonts["small"])
        self._speed_label.pack(side="left")
        self._speed_var.trace_add("write", self._on_speed_change)

    def _section_label(self, parent, text):
        ctk.CTkLabel(parent, text=text, font=self._fonts["heading"], text_color=COLORS["text_muted"], anchor="w").pack(fill="x", padx=PADDING["md"], pady=(PADDING["sm"], PADDING["xs"]))

    # ---- 右侧画布 ----
    def _build_canvas(self, parent):
        canvas_frame = ctk.CTkFrame(parent, corner_radius=12, fg_color=COLORS["canvas_bg"], border_color=COLORS["card_border"], border_width=1)
        canvas_frame.pack(fill="both", expand=True, padx=PADDING["md"], pady=PADDING["md"])

        self._canvas = tk.Canvas(canvas_frame, bg=self._bg_color, highlightthickness=0)
        self._canvas.pack(fill="both", expand=True, padx=6, pady=6)
        self._canvas.bind("<Configure>", lambda _: self._draw())

    # ==================== 回调 ====================

    def _on_width_change(self, *args):
        self._width_label.configure(text=str(self._width_var.get()))
        self._draw()

    def _on_speed_change(self, *args):
        self._speed_label.configure(text=f"{self._speed_var.get()}ms")

    def _choose_color(self):
        color = colorchooser.askcolor(title="选择段颜色", initialcolor=self._on_color)
        if color and color[1]:
            self._on_color = color[1]
            self._color_btn.configure(text=color[1], fg_color=color[1])
            self._draw()

    def _choose_bg_color(self):
        color = colorchooser.askcolor(title="选择背景颜色", initialcolor=self._bg_color)
        if color and color[1]:
            self._bg_color = color[1]
            self._bg_btn.configure(text=color[1], fg_color=color[1])
            self._canvas.configure(bg=color[1])
            self._draw()

    def _toggle_time_mode(self):
        if self._time_mode.get():
            self._entry.configure(state="disabled")
            self._update_time()
        else:
            if self._time_job:
                self.after_cancel(self._time_job)
                self._time_job = None
            self._entry.configure(state="normal")
            self._time_label.configure(text="")
            self._draw()

    def _update_time(self):
        if not self._time_mode.get():
            return
        fmt = self._time_format.get()
        if fmt == "HH:MM:SS":
            text = _time.strftime("%H:%M:%S")
        elif fmt == "HH:MM":
            text = _time.strftime("%H:%M")
        else:
            text = _time.strftime("%Y-%m-%d")
        self._time_label.configure(text=f"当前: {text}")
        self._draw_time(text)
        self._time_job = self.after(500, self._update_time)

    # ==================== 绘制逻辑 ====================

    def _draw(self):
        if self._time_mode.get():
            return
        self._canvas.delete("all")
        text = self._entry.get().strip().upper()
        if not text or not all(c in SEGMENTS for c in text):
            return
        self._draw_chars(text)

    def _draw_time(self, text):
        self._canvas.delete("all")
        self._draw_chars(text)

    def _draw_chars(self, text):
        canvas_w = self._canvas.winfo_width()
        canvas_h = self._canvas.winfo_height()
        if canvas_w <= 1 or canvas_h <= 1:
            return

        seg_w = self._width_var.get()
        chars = list(text)
        # 冒号占 0.5 宽度
        units = sum(0.5 if c == ':' else 1 for c in chars)
        digit_w = int(canvas_w / max(units, 1))
        seg_len = min(digit_w // 2, canvas_h // 3)

        x = 0
        for ch in chars:
            if ch == ':':
                self._draw_colon(x + digit_w * 0.25, canvas_h // 2, seg_len, seg_w)
                x += int(digit_w * 0.5)
            else:
                cx = x + digit_w // 2
                cy = canvas_h // 2
                segs = SEGMENTS.get(ch, [0]*7)
                if self._animate_var.get() and not self._time_mode.get():
                    self._draw_animated_digit(cx, cy, segs, seg_len, seg_w, 0)
                else:
                    for i, state in enumerate(segs):
                        if state:
                            self._draw_segment(cx, cy, i, seg_len, seg_w)
                x += digit_w

    def _draw_animated_digit(self, cx, cy, segs, seg_len, seg_w, seg_idx):
        if seg_idx >= 7:
            return
        if segs[seg_idx]:
            self._draw_segment(cx, cy, seg_idx, seg_len, seg_w)
        self.after(self._speed_var.get(), lambda: self._draw_animated_digit(cx, cy, segs, seg_len, seg_w, seg_idx + 1))

    def _draw_colon(self, cx, cy, seg_len, seg_w):
        r = seg_w
        gap = seg_len // 2
        self._canvas.create_oval(cx-r, cy-gap-r, cx+r, cy-gap+r, fill=self._on_color, outline="")
        self._canvas.create_oval(cx-r, cy+gap-r, cx+r, cy+gap+r, fill=self._on_color, outline="")

    def _draw_segment(self, cx, cy, seg, seg_len, seg_w):
        h = seg_len
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
            if abs(y1 - y2) < 0.01:
                yc = (y1 + y2) / 2
                self._canvas.create_line(x1, yc, x2, yc, fill=self._on_color, width=seg_w, capstyle="round")
            elif abs(x1 - x2) < 0.01:
                xc = (x1 + x2) / 2
                self._canvas.create_line(xc, y1, xc, y2, fill=self._on_color, width=seg_w, capstyle="round")
            else:
                self._canvas.create_line(x1, y1, x2, y2, fill=self._on_color, width=seg_w, capstyle="round")


# ==================== 入口 ====================

if __name__ == "__main__":
    app = SevenSegmentApp()
    app.mainloop()
