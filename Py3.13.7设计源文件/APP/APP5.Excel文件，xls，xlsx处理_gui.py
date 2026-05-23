# ==========================================
# App5. Excel 自动化处理 - GUI版本
# 功能: 读取Excel，按"部门"拆分成多个文件
# ==========================================

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

class ExcelProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel 文件处理 - GUI")
        self.root.geometry("900x650")
        self.root.configure(bg="#f0f0f0")

        # 获取脚本所在目录的上级目录（项目根目录）
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.default_file = os.path.join(script_dir, 'DATA', 'groupby_test_auto_中原工学院教职工名单.xlsx')
        self.source_file = None
        self.df = None
        self.departments = []

        # 设置默认输出目录
        self.output_dir = os.path.join(script_dir, 'DATA')

        # 创建主框架
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="Excel 文件处理",
            font=("Helvetica", 18, "bold"),
            foreground="#1E90FF"
        )
        title_label.pack(pady=15)

        # 文件选择区域
        file_frame = ttk.LabelFrame(main_frame, text="1. 选择源文件", padding="15")
        file_frame.pack(fill=tk.X, pady=10)

        self.file_label = ttk.Label(file_frame, text="未选择文件", font=("Helvetica", 10), foreground="#666666")
        self.file_label.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        browse_btn = ttk.Button(file_frame, text="浏览...", command=self.browse_file, style="Accent.TButton")
        browse_btn.pack(side=tk.RIGHT, padx=5)

        # 分组列选择
        column_frame = ttk.LabelFrame(main_frame, text="2. 选择分组列", padding="15")
        column_frame.pack(fill=tk.X, pady=10)

        ttk.Label(column_frame, text="分组列名:").pack(side=tk.LEFT, padx=5)

        self.column_var = tk.StringVar(value="部门")
        self.column_combobox = ttk.Combobox(column_frame, textvariable=self.column_var, width=20, state="readonly")
        self.column_combobox.pack(side=tk.LEFT, padx=5)

        refresh_btn = ttk.Button(column_frame, text="刷新列", command=self.refresh_columns)
        refresh_btn.pack(side=tk.LEFT, padx=5)

        # 预览区域
        preview_frame = ttk.LabelFrame(main_frame, text="3. 数据预览", padding="10")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # 统计信息
        stats_frame = ttk.Frame(preview_frame)
        stats_frame.pack(fill=tk.X, pady=5)

        self.row_count_label = ttk.Label(stats_frame, text="总行数: 0", font=("Helvetica", 10))
        self.row_count_label.pack(side=tk.LEFT, padx=10)

        self.col_count_label = ttk.Label(stats_frame, text="总列数: 0", font=("Helvetica", 10))
        self.col_count_label.pack(side=tk.LEFT, padx=10)

        self.dept_count_label = ttk.Label(stats_frame, text="分组数: 0", font=("Helvetica", 10))
        self.dept_count_label.pack(side=tk.LEFT, padx=10)

        # Treeview 显示数据
        self.tree_frame = ttk.Frame(preview_frame)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_y = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar_x = ttk.Scrollbar(self.tree_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # 操作按钮
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=15)

        process_btn = ttk.Button(button_frame, text="开始拆分", command=self.process_excel, style="Accent.TButton")
        process_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(button_frame, text="清空", command=self.clear_data)
        clear_btn.pack(side=tk.LEFT, padx=5)

        # 输出目录
        output_frame = ttk.LabelFrame(main_frame, text="输出目录", padding="10")
        output_frame.pack(fill=tk.X, pady=5)

        self.output_dir_label = ttk.Label(output_frame, text=f"当前目录: {os.getcwd()}", font=("Helvetica", 9), foreground="#666666")
        self.output_dir_label.pack(anchor=tk.W)

        change_dir_btn = ttk.Button(output_frame, text="更改输出目录", command=self.change_output_dir)
        change_dir_btn.pack(anchor=tk.E)

        # 更新输出目录标签
        self.output_dir_label.config(text=f"输出目录: {self.output_dir}", foreground="#000000")

        # 进度条
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        self.progress.pack(fill=tk.X, pady=10)

        # 状态标签
        self.status_label = ttk.Label(main_frame, text="准备就绪", font=("Helvetica", 10), foreground="#666666")
        self.status_label.pack(pady=5)

        # 配置样式
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Helvetica", 11, "bold"), padding=(15, 8))

        # 自动加载默认文件
        if os.path.exists(self.default_file):
            self.source_file = self.default_file
            self.file_label.config(text=os.path.basename(self.default_file), foreground="#000000")
            self.load_excel()

    def browse_file(self):
        """浏览选择Excel文件"""
        filetypes = [
            ("Excel文件", "*.xlsx *.xls"),
            ("所有文件", "*.*")
        ]
        filepath = filedialog.askopenfilename(
            title="选择Excel文件",
            filetypes=filetypes
        )

        if filepath:
            self.source_file = filepath
            self.file_label.config(text=os.path.basename(filepath), foreground="#000000")
            self.load_excel()

    def load_excel(self):
        """加载Excel文件"""
        try:
            self.df = pd.read_excel(self.source_file)
            self.status_label.config(text="文件加载成功", foreground="#00AA00")
            self.refresh_columns()
            self.update_preview()
            self.update_stats()
        except Exception as e:
            messagebox.showerror("错误", f"加载文件失败: {str(e)}")
            self.status_label.config(text="文件加载失败", foreground="#FF0000")

    def refresh_columns(self):
        """刷新列名列表"""
        if self.df is not None:
            columns = list(self.df.columns)
            self.column_combobox['values'] = columns
            if "部门" in columns:
                self.column_var.set("部门")
            else:
                self.column_var.set(columns[0] if columns else "")

    def update_preview(self):
        """更新预览数据"""
        if self.df is None:
            return

        # 清空树形视图
        self.tree.delete(*self.tree.get_children())

        # 设置列
        columns = list(self.df.columns)
        self.tree["columns"] = columns

        for col in columns:
            self.tree.heading(col, text=str(col))
            self.tree.column(col, width=100, anchor=tk.W)

        # 只显示前20行
        preview_data = self.df.head(20)
        for idx, row in preview_data.iterrows():
            self.tree.insert("", tk.END, values=list(row))

    def update_stats(self):
        """更新统计信息"""
        if self.df is not None:
            self.row_count_label.config(text=f"总行数: {len(self.df)}")
            self.col_count_label.config(text=f"总列数: {len(self.df.columns)}")

            group_col = self.column_var.get()
            if group_col in self.df.columns:
                self.departments = self.df[group_col].unique()
                self.dept_count_label.config(text=f"分组数: {len(self.departments)}")
            else:
                self.dept_count_label.config(text="分组数: 0")
        else:
            self.row_count_label.config(text="总行数: 0")
            self.col_count_label.config(text="总列数: 0")
            self.dept_count_label.config(text="分组数: 0")

    def change_output_dir(self):
        """更改输出目录"""
        dirpath = filedialog.askdirectory(title="选择输出目录")
        if dirpath:
            self.output_dir = dirpath
            self.output_dir_label.config(text=f"输出目录: {dirpath}", foreground="#000000")

    def process_excel(self):
        """处理Excel文件，按列分组拆分"""
        if self.df is None:
            messagebox.showwarning("警告", "请先选择Excel文件！")
            return

        group_col = self.column_var.get()
        if not group_col or group_col not in self.df.columns:
            messagebox.showwarning("警告", "请选择有效的分组列！")
            return

        try:
            self.progress_var.set(0)
            self.root.update()

            grouped = self.df.groupby(group_col)
            total = len(grouped)

            for i, (group_name, group_df) in enumerate(grouped):
                # 处理分组名称
                if pd.isna(group_name):
                    group_name = "未知"
                else:
                    group_name = str(group_name).replace('/', '_').replace('\\', '_').replace(':', '_')

                # 生成文件名
                output_filename = os.path.join(self.output_dir, f"分表_{group_name}.xlsx")
                group_df.to_excel(output_filename, index=False)

                # 更新进度
                progress = (i + 1) / total * 100
                self.progress_var.set(progress)
                self.status_label.config(text=f"正在处理: {group_name} ({i+1}/{total})", foreground="#000000")
                self.root.update()

            self.progress_var.set(100)
            self.status_label.config(text=f"拆分完成！共生成 {total} 个文件", foreground="#00AA00")
            messagebox.showinfo("完成", f"拆分完成！\n共生成 {total} 个文件\n保存在: {self.output_dir}")

        except Exception as e:
            messagebox.showerror("错误", f"处理失败: {str(e)}")
            self.status_label.config(text="处理失败", foreground="#FF0000")

    def clear_data(self):
        """清空数据"""
        self.df = None
        self.source_file = None
        self.departments = []
        self.file_label.config(text="未选择文件", foreground="#666666")
        self.column_combobox['values'] = []
        self.progress_var.set(0)
        self.status_label.config(text="准备就绪", foreground="#666666")
        self.tree.delete(*self.tree.get_children())
        self.update_stats()


def main():
    """主函数 - 独立运行时使用"""
    root = tk.Tk()
    app = ExcelProcessorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
