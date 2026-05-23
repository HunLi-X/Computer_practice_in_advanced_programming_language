# ==========================================
# App5. Excel 自动化处理 - GUI版本（CustomTkinter 美化）
# 功能: 读取Excel，按指定列拆分成多个文件
# ==========================================

import sys
import os
import pandas as pd
import tkinter.ttk as ttk

# ---- 依赖检查 ----
try:
    import customtkinter as ctk
    from tkinter import filedialog, messagebox
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "-q"])
    import customtkinter as ctk
    from tkinter import filedialog, messagebox

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
    "success":      "#10B981",
    "danger":       "#EF4444",
    "text":         "#E2E8F0",
    "text_muted":   "#64748B",
    "input_bg":     "#0F172A",
}

FONT_PARAMS = {
    "hero":       {"family": "Microsoft YaHei", "size": 18, "weight": "bold"},
    "heading":    {"family": "Microsoft YaHei", "size": 12, "weight": "bold"},
    "body":       {"family": "Microsoft YaHei", "size": 11},
    "small":      {"family": "Microsoft YaHei", "size": 10},
}

PADDING = {"xs": 3, "sm": 6, "md": 10, "lg": 14}

# ---- 路径常量 ----
SCRIPT_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FILE = os.path.join(SCRIPT_DIR, "DATA", "groupby_test_auto_中原工学院教职工名单.xlsx")
OUTPUT_DIR   = os.path.join(SCRIPT_DIR, "DATA")


class ExcelProcessorApp(ctk.CTk):
    """Excel 文件处理主应用"""

    def __init__(self):
        super().__init__()
        self._fonts = {k: ctk.CTkFont(**v) for k, v in FONT_PARAMS.items()}
        self.source_file = None
        self.df = None
        self.departments = []
        self.output_dir = OUTPUT_DIR
        self._setup_window()
        self._build_ui()
        self._auto_load_default()

    def _setup_window(self):
        self.title("Excel 文件处理")
        self.geometry("1000x580")
        self.minsize(800, 480)
        self.configure(fg_color=COLORS["bg"])
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 1000) // 2
        y = (self.winfo_screenheight() - 580) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        # 左侧控制栏
        sidebar = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color=COLORS["card"])
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # 右侧主区域
        right = ctk.CTkFrame(self, fg_color="transparent")
        right.pack(side="right", fill="both", expand=True)

        self._build_sidebar(sidebar)
        self._build_preview(right)

    # ---- 左侧控制栏 ----
    def _build_sidebar(self, parent):
        # 标题
        title_frame = ctk.CTkFrame(parent, fg_color="transparent")
        title_frame.pack(fill="x", padx=PADDING["md"], pady=(PADDING["md"], PADDING["sm"]))
        ctk.CTkLabel(title_frame, text="Excel 处理", font=self._fonts["hero"], text_color=COLORS["text"]).pack(anchor="w")
        ctk.CTkLabel(title_frame, text="按列拆分 .xlsx / .xls", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(anchor="w", pady=(2, 0))

        ctk.CTkFrame(parent, height=1, fg_color=COLORS["card_border"]).pack(fill="x", padx=PADDING["md"], pady=PADDING["xs"])

        inner = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=PADDING["xs"])
        inner._scrollbar.configure(width=4)

        # ---- 源文件 ----
        self._section(inner, "源文件")
        file_card = ctk.CTkFrame(inner, fg_color=COLORS["input_bg"], corner_radius=8)
        file_card.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["xs"]))
        self.file_label = ctk.CTkLabel(file_card, text="未选择文件", anchor="w", font=self._fonts["body"], text_color=COLORS["text_muted"], wraplength=220)
        self.file_label.pack(fill="x", padx=PADDING["sm"], pady=PADDING["sm"])
        ctk.CTkButton(inner, text="浏览文件", height=30, font=self._fonts["body"], corner_radius=8, command=self._browse_file).pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))

        # ---- 分组列 ----
        self._section(inner, "分组列")
        col_row = ctk.CTkFrame(inner, fg_color="transparent")
        col_row.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))
        self.column_combo = ctk.CTkComboBox(col_row, width=180, state="readonly", font=self._fonts["body"], dropdown_font=self._fonts["body"])
        self.column_combo.pack(side="left", fill="x", expand=True, padx=(0, PADDING["xs"]))
        ctk.CTkButton(col_row, text="刷新", width=50, height=28, font=self._fonts["body"], corner_radius=8, command=self._refresh_columns).pack(side="left")

        # ---- 输出目录 ----
        self._section(inner, "输出目录")
        dir_card = ctk.CTkFrame(inner, fg_color=COLORS["input_bg"], corner_radius=8)
        dir_card.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["xs"]))
        self.output_label = ctk.CTkLabel(dir_card, text=OUTPUT_DIR, anchor="w", font=self._fonts["small"], text_color=COLORS["text_muted"], wraplength=220)
        self.output_label.pack(fill="x", padx=PADDING["sm"], pady=PADDING["sm"])
        ctk.CTkButton(inner, text="更改目录", height=30, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["secondary"], hover_color="#334155", command=self._change_output_dir).pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))

        # ---- 执行 ----
        ctk.CTkFrame(inner, height=1, fg_color=COLORS["card_border"]).pack(fill="x", padx=PADDING["md"], pady=PADDING["sm"])

        ctk.CTkButton(inner, text="开始拆分", height=36, font=self._fonts["heading"], corner_radius=10, fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"], command=self._process_excel).pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["xs"]))
        ctk.CTkButton(inner, text="清空", height=30, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["secondary"], hover_color="#334155", command=self._clear_data).pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["sm"]))

        # ---- 进度 + 状态 ----
        self.progress = ctk.CTkProgressBar(parent, height=4, corner_radius=2)
        self.progress.set(0)
        self.progress.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["xs"]))

        self.status_label = ctk.CTkLabel(parent, text="准备就绪", font=self._fonts["small"], text_color=COLORS["text_muted"], anchor="w")
        self.status_label.pack(fill="x", padx=PADDING["md"], pady=(0, PADDING["md"]))

    def _section(self, parent, text):
        ctk.CTkLabel(parent, text=text, font=self._fonts["heading"], text_color=COLORS["text_muted"], anchor="w").pack(fill="x", padx=PADDING["md"], pady=(PADDING["sm"], PADDING["xs"]))

    # ---- 右侧数据预览 ----
    def _build_preview(self, parent):
        # 统计栏
        stats_bar = ctk.CTkFrame(parent, fg_color="transparent")
        stats_bar.pack(fill="x", padx=PADDING["md"], pady=(PADDING["md"], PADDING["xs"]))

        ctk.CTkLabel(stats_bar, text="数据预览", font=self._fonts["heading"], text_color=COLORS["text"]).pack(side="left")

        self.lbl_rows = ctk.CTkLabel(stats_bar, text="行: 0", font=self._fonts["small"], text_color=COLORS["text_muted"])
        self.lbl_rows.pack(side="left", padx=(PADDING["lg"], PADDING["sm"]))
        self.lbl_cols = ctk.CTkLabel(stats_bar, text="列: 0", font=self._fonts["small"], text_color=COLORS["text_muted"])
        self.lbl_cols.pack(side="left", padx=PADDING["sm"])
        self.lbl_depts = ctk.CTkLabel(stats_bar, text="分组: 0", font=self._fonts["small"], text_color=COLORS["text_muted"])
        self.lbl_depts.pack(side="left", padx=PADDING["sm"])

        # Treeview
        tree_frame = ctk.CTkFrame(parent, corner_radius=12, fg_color=COLORS["card"], border_color=COLORS["card_border"], border_width=1)
        tree_frame.pack(fill="both", expand=True, padx=PADDING["md"], pady=(0, PADDING["md"]))

        tree_inner = ctk.CTkFrame(tree_frame, fg_color="transparent")
        tree_inner.pack(fill="both", expand=True, padx=PADDING["sm"], pady=PADDING["sm"])

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=COLORS["input_bg"], foreground=COLORS["text"], fieldbackground=COLORS["input_bg"], borderwidth=0, rowheight=28, font=("Microsoft YaHei", 12))
        style.configure("Treeview.Heading", background=COLORS["secondary"], foreground=COLORS["text"], font=("Microsoft YaHei", 12, "bold"))
        style.map("Treeview", background=[("selected", COLORS["primary"])])

        self.tree = ttk.Treeview(tree_inner, show="headings", height=15)
        self.tree.pack(side="left", fill="both", expand=True)

        scroll = ctk.CTkScrollbar(tree_inner, command=self.tree.yview, width=10)
        self.tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

    # ==================== 逻辑方法 ====================

    def _auto_load_default(self):
        if os.path.exists(DEFAULT_FILE):
            self.source_file = DEFAULT_FILE
            self.file_label.configure(text=os.path.basename(DEFAULT_FILE), text_color="#1E90FF")
            self._load_excel()

    def _browse_file(self):
        path = filedialog.askopenfilename(title="选择 Excel 文件", filetypes=[("Excel 文件", "*.xlsx *.xls"), ("所有文件", "*.*")])
        if path:
            self.source_file = path
            self.file_label.configure(text=os.path.basename(path), text_color="#1E90FF")
            self._load_excel()

    def _load_excel(self):
        try:
            self.df = pd.read_excel(self.source_file)
            self.status_label.configure(text="文件加载成功", text_color=COLORS["success"])
            self._refresh_columns()
            self._update_preview()
            self._update_stats()
        except Exception as e:
            messagebox.showerror("错误", f"加载文件失败:\n{e}")
            self.status_label.configure(text="文件加载失败", text_color=COLORS["danger"])

    def _refresh_columns(self):
        if self.df is not None:
            cols = list(self.df.columns)
            self.column_combo.configure(values=cols)
            if "部门" in cols:
                self.column_combo.set("部门")
            elif cols:
                self.column_combo.set(cols[0])

    def _update_preview(self):
        if self.df is None:
            return
        for item in self.tree.get_children():
            self.tree.delete(item)
        columns = list(self.df.columns)
        self.tree.configure(columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=str(col))
            self.tree.column(col, width=100, anchor="w")
        for _, row in self.df.head(50).iterrows():
            self.tree.insert("", "end", values=list(row))

    def _update_stats(self):
        if self.df is not None:
            self.lbl_rows.configure(text=f"行: {len(self.df)}")
            self.lbl_cols.configure(text=f"列: {len(self.df.columns)}")
            col = self.column_combo.get()
            if col and col in self.df.columns:
                self.departments = self.df[col].dropna().unique().tolist()
                self.lbl_depts.configure(text=f"分组: {len(self.departments)}")
            else:
                self.lbl_depts.configure(text="分组: 0")
        else:
            self.lbl_rows.configure(text="行: 0")
            self.lbl_cols.configure(text="列: 0")
            self.lbl_depts.configure(text="分组: 0")

    def _change_output_dir(self):
        d = filedialog.askdirectory(title="选择输出目录", initialdir=self.output_dir)
        if d:
            self.output_dir = d
            self.output_label.configure(text=d)

    def _process_excel(self):
        if self.df is None:
            messagebox.showwarning("警告", "请先选择 Excel 文件！")
            return
        group_col = self.column_combo.get()
        if not group_col or group_col not in self.df.columns:
            messagebox.showwarning("警告", "请选择有效的分组列！")
            return

        try:
            self.progress.set(0)
            self.update_idletasks()

            grouped = self.df.groupby(group_col)
            total = len(grouped)

            for i, (group_name, group_df) in enumerate(grouped, 1):
                safe_name = str(group_name).replace("/", "_").replace("\\", "_").replace(":", "_")
                if pd.isna(group_name):
                    safe_name = "未知"
                out_path = os.path.join(self.output_dir, f"分表_{safe_name}.xlsx")
                group_df.to_excel(out_path, index=False)

                self.progress.set(i / total)
                self.status_label.configure(text=f"处理中: {safe_name} ({i}/{total})", text_color=COLORS["success"])
                self.update_idletasks()

            self.progress.set(1)
            self.status_label.configure(text=f"完成！共 {total} 个文件", text_color=COLORS["success"])
            messagebox.showinfo("完成", f"拆分完成！\n共生成 {total} 个文件\n保存在:\n{self.output_dir}")
        except Exception as e:
            messagebox.showerror("错误", f"处理失败:\n{e}")
            self.status_label.configure(text="处理失败", text_color=COLORS["danger"])

    def _clear_data(self):
        self.df = None
        self.source_file = None
        self.departments = []
        self.file_label.configure(text="未选择文件", text_color=COLORS["text_muted"])
        self.column_combo.configure(values=[])
        self.progress.set(0)
        self.status_label.configure(text="准备就绪", text_color=COLORS["text_muted"])
        for item in self.tree.get_children():
            self.tree.delete(item)
        self._update_stats()


# ==================== 入口 ====================

if __name__ == "__main__":
    app = ExcelProcessorApp()
    app.mainloop()
