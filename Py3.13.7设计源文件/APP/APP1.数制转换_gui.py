# ==========================================
# App1. 数制转换 - GUI版本 (CustomTkinter 美化)
# 支持任意进制之间的转换
# ==========================================

import sys
import os

# ── 依赖检查 ──
try:
    import customtkinter as ctk
except ImportError:
    print("正在安装 customtkinter...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "-q"])
    import customtkinter as ctk

# ── 进制转换核心 ──
def convert_base(value: str, from_base: int, to_base: int) -> str | None:
    """任意进制互转 (2-36)"""
    try:
        decimal_value = int(value, from_base)
        if to_base == 2:
            return bin(decimal_value)[2:]
        if to_base == 8:
            return oct(decimal_value)[2:]
        if to_base == 16:
            return hex(decimal_value)[2:].upper()
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if decimal_value == 0:
            return "0"
        is_neg = decimal_value < 0
        decimal_value = abs(decimal_value)
        result = ""
        while decimal_value:
            result = digits[decimal_value % to_base] + result
            decimal_value //= to_base
        return "-" + result if is_neg else result
    except (ValueError, TypeError):
        return None


class NumberBaseApp(ctk.CTk):
    """数制转换主应用"""

    # ── 进制选项 ──
    BASES = ["2", "8", "10", "16", "32", "36"]

    def __init__(self):
        super().__init__()
        self._setup_window()
        self._build_ui()
        self._set_defaults()

    # ==================== 窗口设置 ====================

    def _setup_window(self):
        self.title("数制转换")
        self.geometry("620x720")
        self.minsize(520, 600)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 620) // 2
        y = (self.winfo_screenheight() - 720) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        """构建全部界面"""
        # ── 主滚动容器 ──
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=(15, 10))

        # ── 标题 ──
        ctk.CTkLabel(
            scroll,
            text="🔢  数制转换器",
            font=ctk.CTkFont(size=26, weight="bold"),
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            scroll,
            text="支持 2 ~ 36 进制任意互转",
            font=ctk.CTkFont(size=13),
            text_color="gray60",
        ).pack(pady=(0, 15))

        # ── 输入卡片 ──
        self._build_input_card(scroll)

        # ── 结果卡片 ──
        self._build_result_card(scroll)

        # ── 全部进制卡片 ──
        self._build_all_bases_card(scroll)

        # ── 底部按钮 ──
        self._build_bottom_buttons(scroll)

    # ── 输入卡片 ──
    def _build_input_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="x", pady=8, padx=4)
        ctk.CTkLabel(
            card, text="📥  输入数值", font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=16, pady=(12, 6))

        # 第一行：原进制
        row1 = ctk.CTkFrame(card, fg_color="transparent")
        row1.pack(fill="x", padx=16, pady=4)
        ctk.CTkLabel(row1, text="原进制", width=70, anchor="w").pack(side="left")
        self.from_combo = ctk.CTkComboBox(
            row1, values=self.BASES, width=120, state="readonly"
        )
        self.from_combo.pack(side="left", padx=8)
        self.from_combo.set("10")

        # 第二行：输入
        row2 = ctk.CTkFrame(card, fg_color="transparent")
        row2.pack(fill="x", padx=16, pady=4)
        ctk.CTkLabel(row2, text="数值", width=70, anchor="w").pack(side="left")
        self.input_entry = ctk.CTkEntry(
            row2, placeholder_text="请输入数值，如 255 / FF / 1010 ...", height=36
        )
        self.input_entry.pack(side="left", fill="x", expand=True, padx=8)
        self.input_entry.bind("<Return>", lambda _: self._do_convert())

        # 第三行：目标进制
        row3 = ctk.CTkFrame(card, fg_color="transparent")
        row3.pack(fill="x", padx=16, pady=(4, 12))
        ctk.CTkLabel(row3, text="目标进制", width=70, anchor="w").pack(side="left")
        self.to_combo = ctk.CTkComboBox(
            row3, values=self.BASES, width=120, state="readonly"
        )
        self.to_combo.pack(side="left", padx=8)
        self.to_combo.set("2")

    # ── 结果卡片 ──
    def _build_result_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="x", pady=8, padx=4)
        ctk.CTkLabel(
            card, text="🎯  转换结果", font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=16, pady=(12, 8))

        self.result_label = ctk.CTkLabel(
            card,
            text="—",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#1E90FF",
        )
        self.result_label.pack(pady=(0, 12), padx=16)

    # ── 全部进制卡片 ──
    def _build_all_bases_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="x", pady=8, padx=4)
        ctk.CTkLabel(
            card, text="📊  全部常用进制", font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=16, pady=(12, 8))

        self._add_base_row(card, "二进制  ", "bin")
        self._add_base_row(card, "八进制  ", "oct")
        self._add_base_row(card, "十进制  ", "dec")
        self._add_base_row(card, "十六进制", "hex")

        ctk.CTkFrame(card, height=10, fg_color="transparent").pack()

    def _add_base_row(self, parent, label: str, key: str):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=16, pady=3)
        ctk.CTkLabel(row, text=label, width=90, anchor="w", text_color="gray60").pack(side="left")
        lbl = ctk.CTkLabel(row, text="—", anchor="w", font=ctk.CTkFont(size=13))
        lbl.pack(side="left", fill="x", expand=True)
        setattr(self, f"label_{key}", lbl)

    # ── 底部按钮 ──
    def _build_bottom_buttons(self, parent):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(pady=(10, 20))

        ctk.CTkButton(
            frame, text="▶  转  换", width=140, height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._do_convert,
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            frame, text="✕  清  空", width=140, height=40,
            font=ctk.CTkFont(size=14),
            fg_color="gray30", hover_color="gray40",
            command=self._do_clear,
        ).pack(side="left", padx=10)

    # ==================== 逻辑 ====================

    def _set_defaults(self):
        self.input_entry.focus()

    def _do_convert(self):
        value = self.input_entry.get().strip().upper()
        if not value:
            self.result_label.configure(text="⚠ 请输入数值", text_color="#FF8C00")
            return

        try:
            from_base = int(self.from_combo.get())
            to_base   = int(self.to_combo.get())
            decimal_val = int(value, from_base)
        except ValueError:
            self.result_label.configure(
                text=f"⚠ 输入不是有效的 {from_base} 进制数", text_color="#FF4444"
            )
            return

        result = convert_base(value, from_base, to_base)
        self.result_label.configure(text=result or "—", text_color="#1E90FF")

        # 更新全部进制
        for base, key in [(2, "bin"), (8, "oct"), (10, "dec"), (16, "hex")]:
            val = convert_base(str(decimal_val), 10, base)
            lbl = getattr(self, f"label_{key}")
            lbl.configure(text=val)

    def _do_clear(self):
        self.input_entry.delete(0, "end")
        self.result_label.configure(text="—", text_color="#1E90FF")
        for key in ("bin", "oct", "dec", "hex"):
            getattr(self, f"label_{key}").configure(text="—")
        self.from_combo.set("10")
        self.to_combo.set("2")
        self.input_entry.focus()


# ==================== 入口 ====================

if __name__ == "__main__":
    NumberBaseApp().mainloop()
