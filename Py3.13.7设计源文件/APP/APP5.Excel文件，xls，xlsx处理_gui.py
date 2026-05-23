# ==========================================
# App5. Excel 自动化处理 - GUI版本 (CustomTkinter 美化)
# 功能: 读取Excel，按"部门"拆分成多个文件
# ==========================================

import sys
import os
import pandas as pd

# ── 依赖检查 ──
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

# ── 路径常量 ──
SCRIPT_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FILE = os.path.join(SCRIPT_DIR, "DATA", "groupby_test_auto_中原工学院教职工名单.xlsx")
OUTPUT_DIR   = os.path.join(SCRIPT_DIR, "DATA")


class ExcelProcessorApp(ctk.CTk):
    """Excel 文件处理主应用"""

    def __init__(self):
        super().__init__()
        self.source_file = None
        self.df           = None
        self.departments = []
        self.output_dir   = OUTPUT_DIR
        self._setup_window()
        self._build_ui()
        self._auto_load_default()

    # ==================== 窗口设置 ====================

    def _setup_window(self):
        self.title("Excel 文件处理")
        self.geometry("960x720")
        self.minsize(800, 600)
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - 960) // 2
        y = (self.winfo_screenheight() - 720) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=(15, 10))

        # ── 标题 ──
        ctk.CTkLabel(
            scroll, text="📁  Excel 文件处理",
            font=ctk.CTkFont(size=26, weight="bold"),
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            scroll, text="按指定列拆分 Excel 为多个文件",
            font=ctk.CTkFont(size=13),
            text_color="gray60",
        ).pack(pady=(0, 15))

        # ── Step 1：选择文件 ──
        self._build_file_card(scroll)

        # ── Step 2：选择分组列 ──
        self._build_column_card(scroll)

        # ── Step 3：数据预览 ──
        self._build_preview_card(scroll)

        # ── Step 4：输出目录 + 执行 ──
        self._build_action_card(scroll)

    # ── Step 1 卡片 ──
    def _build_file_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="x", pady=8, padx=4)

        ctk.CTkLabel(
            card, text="📂  1. 选择源文件",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(anchor="w", padx=16, pady=(12, 8))

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", padx=16, pady=(0, 12))

        self.file_label = ctk.CTkLabel(
            row, text="未选择文件", anchor="w",
            font=ctk.CTkFont(size=12),
        )
        self.file_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

        ctk.CTkButton(
            row, text="📂  浏览...", width=120, height=34,
            command=self._browse_file,
        ).pack(side="right")

    # ── Step 2 卡片 ──
    def _build_column_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="x", pady=8, padx=4)

        ctk.CTkLabel(
            card, text="📊  2. 选择分组列",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(anchor="w", padx=16, pady=(12, 8))

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", padx=16, pady=(0, 12))

        ctk.CTkLabel(row, text="分组列", width=70, anchor="w").pack(side="left")

        self.column_combo = ctk.CTkComboBox(
            row, width=200, state="readonly",
        )
        self.column_combo.pack(side="left", padx=8)

        ctk.CTkButton(
            row, text="🔄  刷新列", width=110, height=32,
            command=self._refresh_columns,
        ).pack(side="left", padx=8)

    # ── Step 3 卡片 ──
    def _build_preview_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="both", expand=True, pady=8, padx=4)

        ctk.CTkLabel(
            card, text="📋  3. 数据预览",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(anchor="w", padx=16, pady=(12, 8))

        # 统计行
        stats = ctk.CTkFrame(card, fg_color="transparent")
        stats.pack(fill="x", padx=16, pady=(0, 6))

        self.lbl_rows    = ctk.CTkLabel(stats, text="总行数: 0", font=ctk.CTkFont(size=11))
        self.lbl_rows.pack(side="left", padx=12)

        self.lbl_cols    = ctk.CTkLabel(stats, text="总列数: 0", font=ctk.CTkFont(size=11))
        self.lbl_cols.pack(side="left", padx=12)

        self.lbl_depts   = ctk.CTkLabel(stats, text="分组数: 0", font=ctk.CTkFont(size=11))
        self.lbl_depts.pack(side="left", padx=12)

        # Treeview 容器
        tree_container = ctk.CTkFrame(card, fg_color="transparent")
        tree_container.pack(fill="both", expand=True, padx=16, pady=(0, 12))

        self.tree = ctk.CTkTreeview(
            tree_container, show="headings", height=8,
        )
        self.tree.pack(side="left", fill="both", expand=True)

        tree_scroll = ctk.CTkScrollbar(tree_container, command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        tree_scroll.pack(side="right", fill="y")

    # ── Step 4 卡片 ──
    def _build_action_card(self, parent):
        card = ctk.CTkFrame(parent, corner_radius=14)
        card.pack(fill="x", pady=(8, 4), padx=4)

        ctk.CTkLabel(
            card, text="🚀  4. 执行拆分",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(anchor="w", padx=16, pady=(12, 8))

        # 输出目录行
        dir_row = ctk.CTkFrame(card, fg_color="transparent")
        dir_row.pack(fill="x", padx=16, pady=(0, 6))

        ctk.CTkLabel(dir_row, text="输出目录", width=70, anchor="w").pack(side="left")

        self.output_label = ctk.CTkLabel(
            dir_row, text=OUTPUT_DIR, anchor="w",
            font=ctk.CTkFont(size=11), text_color="gray60",
        )
        self.output_label.pack(side="left", fill="x", expand=True, padx=8)

        ctk.CTkButton(
            dir_row, text="📁  更改", width=110, height=30,
            command=self._change_output_dir,
        ).pack(side="right")

        # 进度条
        self.progress = ctk.CTkProgressBar(
            card, height=16, corner_radius=8,
        )
        self.progress.set(0)
        self.progress.pack(fill="x", padx=16, pady=6)

        # 状态标签
        self.status_label = ctk.CTkLabel(
            card, text="准备就绪", font=ctk.CTkFont(size=11),
            text_color="gray60",
        )
        self.status_label.pack(anchor="w", padx=16, pady=(0, 6))

        # 按钮行
        btn_row = ctk.CTkFrame(card, fg_color="transparent")
        btn_row.pack(pady=(4, 12))

        ctk.CTkButton(
            btn_row, text="▶  开始拆分", width=160, height=42,
            font=ctk.CTkFont(size=15, weight="bold"),
            corner_radius=10, command=self._process_excel,
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            btn_row, text="✕  清空", width=140, height=42,
            font=ctk.CTkFont(size=14),
            fg_color="gray30", hover_color="gray40",
            corner_radius=10, command=self._clear_data,
        ).pack(side="left", padx=10)

    # ==================== 逻辑方法 ====================

    def _auto_load_default(self):
        if os.path.exists(DEFAULT_FILE):
            self.source_file = DEFAULT_FILE
            self.file_label.configure(text=os.path.basename(DEFAULT_FILE), text_color="#1E90FF")
            self._load_excel()

    def _browse_file(self):
        path = filedialog.askopenfilename(
            title="选择 Excel 文件",
            filetypes=[("Excel 文件", "*.xlsx *.xls"), ("所有文件", "*.*")],
        )
        if path:
            self.source_file = path
            self.file_label.configure(text=os.path.basename(path), text_color="#1E90FF")
            self._load_excel()

    def _load_excel(self):
        try:
            self.df = pd.read_excel(self.source_file)
            self.status_label.configure(text="文件加载成功", text_color="#4CAF50")
            self._refresh_columns()
            self._update_preview()
            self._update_stats()
        except Exception as e:
            messagebox.showerror("错误", f"加载文件失败:\n{e}")
            self.status_label.configure(text="文件加载失败", text_color="#F44336")

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
        for _, row in self.df.head(20).iterrows():
            self.tree.insert("", "end", values=list(row))

    def _update_stats(self):
        if self.df is not None:
            self.lbl_rows.configure(text=f"总行数: {len(self.df)}")
            self.lbl_cols.configure(text=f"总列数: {len(self.df.columns)}")
            col = self.column_combo.get()
            if col and col in self.df.columns:
                self.departments = self.df[col].dropna().unique().tolist()
                self.lbl_depts.configure(text=f"分组数: {len(self.departments)}")
            else:
                self.lbl_depts.configure(text="分组数: 0")
        else:
            self.lbl_rows.configure(text="总行数: 0")
            self.lbl_cols.configure(text="总列数: 0")
            self.lbl_depts.configure(text="分组数: 0")

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
            total   = len(grouped)

            for i, (group_name, group_df) in enumerate(grouped, 1):
                safe_name = str(group_name).replace("/", "_").replace("\\", "_").replace(":", "_")
                if pd.isna(group_name):
                    safe_name = "未知"
                out_path = os.path.join(self.output_dir, f"分表_{safe_name}.xlsx")
                group_df.to_excel(out_path, index=False)

                self.progress.set(i / total)
                self.status_label.configure(
                    text=f"正在处理: {safe_name} ({i}/{total})",
                    text_color="#4CAF50",
                )
                self.update_idletasks()

            self.progress.set(1)
            self.status_label.configure(
                text=f"拆分完成！共生成 {total} 个文件", text_color="#4CAF50",
            )
            messagebox.showinfo("完成", f"拆分完成！\n共生成 {total} 个文件\n保存在:\n{self.output_dir}")
        except Exception as e:
            messagebox.showerror("错误", f"处理失败:\n{e}")
            self.status_label.configure(text="处理失败", text_color="#F44336")

    def _clear_data(self):
        self.df = None
        self.source_file = None
        self.departments = []
        self.file_label.configure(text="未选择文件", text_color="gray60")
        self.column_combo.configure(values=[])
        self.progress.set(0)
        self.status_label.configure(text="准备就绪", text_color="gray60")
        for item in self.tree.get_children():
            self.tree.delete(item)
        self._update_stats()


# ==================== 入口 ====================

if __name__ == "__main__":
    ExcelProcessorApp().mainloop()
