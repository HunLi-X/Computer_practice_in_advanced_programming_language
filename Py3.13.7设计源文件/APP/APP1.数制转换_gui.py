# ==========================================
# App1. 数制转换 - GUI版本 (CustomTkinter 美化)
# 支持任意进制之间的转换 (2-36进制)
# ==========================================

import sys
import os

# ---- 依赖检查 ----
try:
    import customtkinter as ctk
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "-q"])
    import customtkinter as ctk

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
    "accent":       "#818CF8",
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
    "mono_big":   {"family": "Cascadia Code", "size": 22, "weight": "bold"},
    "mono":       {"family": "Cascadia Code", "size": 11},
}

PADDING = {
    "xs": 3,
    "sm": 6,
    "md": 10,
    "lg": 14,
    "xl": 18,
}

# ---- 进制转换核心 ----
def convert_base(value: str, from_base: int, to_base: int) -> str | None:
    """任意进制互转 (2-36)"""
    try:
        decimal_value = int(value, from_base)
        if to_base == 2:
            return bin(decimal_value)[2:]
        if to_base == 8:
            return oct(decimal_value)[2:]
        if to_base == 10:
            return str(decimal_value)
        if to_base == 16:
            return hex(decimal_value)[2:].upper()
        return _decimal_to_base(decimal_value, to_base)
    except ValueError:
        return None

def _decimal_to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        rem = n % base
        digits.append(chr(ord("A") + rem - 10) if rem >= 10 else str(rem))
        n //= base
    return "".join(reversed(digits))

# ---- 主应用 ----
class NumberBaseApp(ctk.CTk):
    """数制转换主窗口"""

    BASES = ["2", "8", "10", "16", "32", "36"]

    def __init__(self):
        super().__init__()
        self._fonts = {k: ctk.CTkFont(**v) for k, v in FONT_PARAMS.items()}
        self._setup_window()
        self._build_ui()
        self._set_defaults()

    # ==================== 窗口设置 ====================

    def _setup_window(self):
        self.title("数制转换")
        self.geometry("680x560")
        self.minsize(580, 480)
        self.configure(fg_color=COLORS["bg"])
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - 680) // 2
        y = (self.winfo_screenheight() - 560) // 2
        self.geometry(f"+{x}+{y}")

    def _set_defaults(self):
        self.from_combo.set("10")
        self.to_combo.set("2")
        self.input_entry.focus()
        self._do_convert()

    # ==================== 构建 UI ====================

    def _build_ui(self):
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=PADDING["lg"], pady=PADDING["md"])

        # ---- 标题区（紧凑）----
        header = ctk.CTkFrame(main, fg_color="transparent")
        header.pack(fill="x", pady=(0, PADDING["sm"]))
        ctk.CTkLabel(header, text="🔢  数制转换器", font=self._fonts["hero"], text_color=COLORS["text"]).pack(side="left")
        ctk.CTkLabel(header, text="  支持 2~36 进制任意互转", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(side="left", padx=(PADDING["sm"], 0), pady=(4, 0))

        # ---- 输入卡片 ----
        card_in = ctk.CTkFrame(main, corner_radius=12, fg_color=COLORS["card"], border_color=COLORS["card_border"], border_width=1)
        card_in.pack(fill="x", pady=(0, PADDING["sm"]))

        # 第一行：原进制 + 数值输入 + 目标进制
        row1 = ctk.CTkFrame(card_in, fg_color="transparent")
        row1.pack(fill="x", padx=PADDING["md"], pady=(PADDING["md"], PADDING["xs"]))

        ctk.CTkLabel(row1, text="原进制", width=50, anchor="w", font=self._fonts["body"]).pack(side="left")
        self.from_combo = ctk.CTkComboBox(row1, width=80, values=self.BASES, state="readonly", font=self._fonts["body"], dropdown_font=self._fonts["body"])
        self.from_combo.pack(side="left", padx=(0, PADDING["sm"]))
        self.from_combo.configure(command=lambda _: self._do_convert())

        self.input_entry = ctk.CTkEntry(row1, placeholder_text="输入数值", height=34, font=self._fonts["mono"], fg_color=COLORS["input_bg"])
        self.input_entry.pack(side="left", fill="x", expand=True, padx=PADDING["xs"])
        self.input_entry.bind("<KeyRelease>", lambda _: self._do_convert())
        self.input_entry.bind("<Return>", lambda _: self._do_convert())

        ctk.CTkLabel(row1, text="→", font=self._fonts["heading"], text_color=COLORS["accent"]).pack(side="left", padx=PADDING["xs"])

        self.to_combo = ctk.CTkComboBox(row1, width=80, values=self.BASES, state="readonly", font=self._fonts["body"], dropdown_font=self._fonts["body"])
        self.to_combo.pack(side="left", padx=(0, PADDING["sm"]))
        self.to_combo.configure(command=lambda _: self._do_convert())

        ctk.CTkButton(row1, text="转换", width=60, height=32, font=self._fonts["heading"], corner_radius=8, fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"], command=self._do_convert).pack(side="left", padx=(PADDING["xs"], 0))
        ctk.CTkButton(row1, text="清空", width=50, height=32, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["secondary"], hover_color="#334155", command=self._do_clear).pack(side="left", padx=(PADDING["xs"], 0))

        # 结果行
        row_result = ctk.CTkFrame(card_in, fg_color="transparent")
        row_result.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["md"]))

        self.result_label = ctk.CTkLabel(row_result, text="—", font=self._fonts["mono_big"], text_color=COLORS["accent"], anchor="w")
        self.result_label.pack(side="left", fill="x", expand=True)

        self.status_label = ctk.CTkLabel(row_result, text="等待输入...", font=self._fonts["small"], text_color=COLORS["text_muted"])
        self.status_label.pack(side="right")

        # ---- 下半部分：左右分栏 ----
        bottom = ctk.CTkFrame(main, fg_color="transparent")
        bottom.pack(fill="both", expand=True, pady=(0, 0))

        # 左侧：全部常用进制
        card_bases = ctk.CTkFrame(bottom, corner_radius=12, fg_color=COLORS["card"], border_color=COLORS["card_border"], border_width=1)
        card_bases.pack(side="left", fill="both", expand=True, padx=(0, PADDING["xs"]))

        ctk.CTkLabel(card_bases, text="📊  常用进制一览", font=self._fonts["heading"], text_color=COLORS["text"]).pack(anchor="w", padx=PADDING["md"], pady=(PADDING["md"], PADDING["xs"]))

        for label, key, base in [("二进制", "bin", "2"), ("八进制", "oct", "8"), ("十进制", "dec", "10"), ("十六进制", "hex", "16")]:
            row = ctk.CTkFrame(card_bases, fg_color="transparent")
            row.pack(fill="x", padx=PADDING["md"], pady=1)
            ctk.CTkLabel(row, text=label, width=60, anchor="w", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(side="left")
            value_label = ctk.CTkLabel(row, text="—", anchor="w", font=self._fonts["mono"])
            value_label.pack(side="left", fill="x", expand=True)
            setattr(self, f"label_{key}", value_label)

        ctk.CTkFrame(card_bases, height=6, fg_color="transparent").pack()

        # 右侧：使用说明
        card_help = ctk.CTkFrame(bottom, corner_radius=12, fg_color=COLORS["secondary"], border_color=COLORS["card_border"], border_width=1)
        card_help.pack(side="right", fill="both", expand=True, padx=(PADDING["xs"], 0))

        ctk.CTkLabel(card_help, text="💡  使用说明", font=self._fonts["heading"], text_color=COLORS["text"]).pack(anchor="w", padx=PADDING["md"], pady=(PADDING["md"], PADDING["xs"]))

        help_lines = [
            "• 支持 0-9, A-Z (不区分大小写)",
            "• 二进制: 0-1  |  八进制: 0-7",
            "• 十进制: 0-9  |  十六进制: 0-9,A-F",
            "• 三十六进制: 0-9, A-Z",
            "",
            "示例:",
            "• 255 (十进制) = FF (十六进制)",
            "• 1010 (二进制) = 10 (十进制)",
        ]
        help_text = ctk.CTkTextbox(card_help, height=120, font=self._fonts["small"], fg_color="transparent", border_width=0)
        help_text.pack(fill="both", expand=True, padx=PADDING["md"], pady=(0, PADDING["md"]))
        help_text.insert("0.0", "\n".join(help_lines))
        help_text.configure(state="disabled")

    # ==================== 逻辑 ====================

    def _do_convert(self):
        value = self.input_entry.get().strip().upper()
        if not value:
            self.result_label.configure(text="—", text_color=COLORS["accent"])
            self.status_label.configure(text="等待输入...", text_color=COLORS["text_muted"])
            for key in ("bin", "oct", "dec", "hex"):
                getattr(self, f"label_{key}").configure(text="—")
            return

        try:
            from_b = int(self.from_combo.get())
            to_b = int(self.to_combo.get())
            decimal_val = int(value, from_b)
        except ValueError:
            self.result_label.configure(text="⚠ 输入错误", text_color=COLORS["error"])
            self.status_label.configure(text=f"输入不是有效的 {from_b} 进制数", text_color=COLORS["error"])
            return

        result = convert_base(value, from_b, to_b)
        self.result_label.configure(text=result or "—", text_color=COLORS["accent"])
        self.status_label.configure(text=f"{from_b} → {to_b}  转换成功", text_color=COLORS["success"])

        for base, key in [(2, "bin"), (8, "oct"), (10, "dec"), (16, "hex")]:
            val = convert_base(str(decimal_val), 10, base)
            lbl = getattr(self, f"label_{key}")
            lbl.configure(text=val)

    def _do_clear(self):
        self.input_entry.delete(0, "end")
        self.result_label.configure(text="—", text_color=COLORS["accent"])
        self.status_label.configure(text="等待输入...", text_color=COLORS["text_muted"])
        for key in ("bin", "oct", "dec", "hex"):
            getattr(self, f"label_{key}").configure(text="—")
        self.from_combo.set("10")
        self.to_combo.set("2")
        self.input_entry.focus()


# ==================== 入口 ====================

if __name__ == "__main__":
    app = NumberBaseApp()
    app.mainloop()
