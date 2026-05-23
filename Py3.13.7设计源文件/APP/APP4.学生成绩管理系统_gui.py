# ==========================================
# App4. 学生成绩管理系统 - GUI版本
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import os

class StudentGradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("学生成绩管理系统 - GUI")
        self.root.geometry("900x600")
        self.root.minsize(800, 500)
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")

        # 获取数据文件路径
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_file = os.path.join(script_dir, 'DATA', '学生成绩表.xlsx')
        self.backup_file = os.path.join(script_dir, 'DATA', '学生成绩表_备份.xlsx')

        # 确保DATA目录存在
        if not os.path.exists(os.path.dirname(self.data_file)):
            os.makedirs(os.path.dirname(self.data_file))

        # 初始化成绩单
        self.grades = {}
        self.load_from_file()  # 启动时自动加载数据

        # 创建主框架
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="学生成绩管理系统",
            font=("Helvetica", 18, "bold"),
            foreground="#1E90FF"
        )
        title_label.pack(pady=15)

        # 创建左右分栏
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # 左侧：成绩列表
        left_frame = ttk.LabelFrame(content_frame, text="成绩列表", padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # 创建Treeview容器（用于放置滚动条）
        tree_container = ttk.Frame(left_frame)
        tree_container.pack(fill=tk.BOTH, expand=True)

        # 滚动条
        scrollbar = ttk.Scrollbar(tree_container, orient=tk.VERTICAL)

        # 创建 Treeview
        columns = ("name", "score")
        self.tree = ttk.Treeview(
            tree_container,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set
        )
        self.tree.heading("name", text="姓名")
        self.tree.heading("score", text="成绩")
        self.tree.column("name", width=150)
        self.tree.column("score", width=80)

        # 配置滚动条
        scrollbar.config(command=self.tree.yview)

        # 布局：Treeview在左，滚动条在右
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 右侧：操作面板
        right_frame = ttk.LabelFrame(content_frame, text="操作面板", padding="0")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5)

        # 创建操作面板的滚动容器
        right_scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL)
        right_canvas = tk.Canvas(right_frame, yscrollcommand=right_scrollbar.set, highlightthickness=0)
        right_scrollbar.config(command=right_canvas.yview)

        # 内容框架
        right_content = ttk.Frame(right_canvas, padding="15")

        # 配置滚动布局
        right_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        right_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        right_canvas.create_window((0, 0), window=right_content, anchor="nw")

        # 绑定事件：当内容改变时更新滚动区域
        def on_right_frame_configure(event):
            right_canvas.configure(scrollregion=right_canvas.bbox("all"))
        right_content.bind("<Configure>", on_right_frame_configure)

        # 鼠标滚轮支持
        def on_mouse_wheel(event):
            right_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        right_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        # 查询功能
        ttk.Label(right_content, text="查询成绩", font=("Helvetica", 11, "bold")).pack(pady=(10, 5))
        query_frame = ttk.Frame(right_content)
        query_frame.pack(pady=5)
        ttk.Label(query_frame, text="姓名:").pack(side=tk.LEFT, padx=5)
        self.query_entry = ttk.Entry(query_frame, width=15)
        self.query_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(query_frame, text="查询", command=self.query_student, style="Accent.TButton").pack(side=tk.LEFT, padx=5)

        # 添加/修改功能
        ttk.Label(right_content, text="添加/修改成绩", font=("Helvetica", 11, "bold")).pack(pady=(20, 5))
        add_frame = ttk.Frame(right_content)
        add_frame.pack(pady=5)
        ttk.Label(add_frame, text="姓名:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(add_frame, width=15)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(add_frame, text="成绩:").grid(row=1, column=0, padx=5, pady=5)
        self.score_entry = ttk.Entry(add_frame, width=15)
        self.score_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(add_frame, text="保存", command=self.add_modify_student, style="Accent.TButton").grid(row=2, column=0, columnspan=2, pady=10)

        # 删除功能
        ttk.Label(right_content, text="删除成绩", font=("Helvetica", 11, "bold")).pack(pady=(20, 5))
        delete_frame = ttk.Frame(right_content)
        delete_frame.pack(pady=5)
        ttk.Label(delete_frame, text="姓名:").pack(side=tk.LEFT, padx=5)
        self.delete_entry = ttk.Entry(delete_frame, width=15)
        self.delete_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(delete_frame, text="删除", command=self.delete_student).pack(side=tk.LEFT, padx=5)

        # 导出功能
        export_frame = ttk.LabelFrame(right_content, text="导出数据", padding=10)
        export_frame.pack(fill=tk.X, pady=(10, 5))
        ttk.Button(export_frame, text="📊 导出Excel", command=self.export_excel, style="Accent.TButton").pack(fill=tk.X, pady=3)
        ttk.Button(export_frame, text="📝 导出文本", command=self.export_text).pack(fill=tk.X, pady=3)

        # 统计信息
        stats_frame = ttk.LabelFrame(right_content, text="统计信息", padding=10)
        stats_frame.pack(fill=tk.X, pady=(10, 0))
        self.count_label = ttk.Label(stats_frame, text="总人数: 0", font=("Helvetica", 10))
        self.count_label.pack(anchor=tk.W, pady=2)
        self.avg_label = ttk.Label(stats_frame, text="平均分: 0", font=("Helvetica", 10))
        self.avg_label.pack(anchor=tk.W, pady=2)
        self.max_label = ttk.Label(stats_frame, text="最高分: 0", font=("Helvetica", 10))
        self.max_label.pack(anchor=tk.W, pady=2)
        self.min_label = ttk.Label(stats_frame, text="最低分: 0", font=("Helvetica", 10))
        self.min_label.pack(anchor=tk.W, pady=2)

        # 配置样式
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Helvetica", 10, "bold"), padding=(10, 5))

        # 刷新数据
        self.refresh_data()

        # 绑定双击事件
        self.tree.bind("<Double-1>", self.on_double_click)

        # 绑定窗口关闭事件，自动保存数据
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def refresh_data(self):
        """刷新树形视图和统计信息"""
        # 清空树形视图
        for item in self.tree.get_children():
            self.tree.delete(item)

        # 重新填充数据
        for name, score in sorted(self.grades.items()):
            self.tree.insert("", tk.END, values=(name, score))

        # 更新统计信息
        count = len(self.grades)
        if count > 0:
            scores = [float(s) for s in self.grades.values()]
            avg = sum(scores) / count
            max_score = max(scores)
            min_score = min(scores)
        else:
            avg = 0
            max_score = 0
            min_score = 0

        self.count_label.config(text=f"总人数: {count}")
        self.avg_label.config(text=f"平均分: {avg:.1f}")
        self.max_label.config(text=f"最高分: {max_score}")
        self.min_label.config(text=f"最低分: {min_score}")

    def query_student(self):
        """查询学生成绩"""
        name = self.query_entry.get()
        if name in self.grades:
            messagebox.showinfo("查询结果", f"{name} 的成绩是: {self.grades[name]}")
        else:
            messagebox.showwarning("查询结果", f"找不到学生: {name}")
        self.query_entry.delete(0, tk.END)

    def add_modify_student(self):
        """添加或修改学生成绩"""
        name = self.name_entry.get().strip()
        score = self.score_entry.get().strip()

        if not name:
            messagebox.showwarning("输入错误", "请输入学生姓名！")
            return

        if not score:
            messagebox.showwarning("输入错误", "请输入成绩！")
            return

        try:
            score = float(score)
            if score < 0 or score > 100:
                messagebox.showwarning("输入错误", "成绩必须在 0 到 100 之间！")
                return
        except ValueError:
            messagebox.showwarning("输入错误", "成绩必须是数字！")
            return

        self.grades[name] = score
        self.refresh_data()
        self.auto_save()  # 自动保存到文件
        messagebox.showinfo("成功", f"已成功保存 {name} 的成绩！\n数据已自动保存到DATA目录")
        self.name_entry.delete(0, tk.END)
        self.score_entry.delete(0, tk.END)

    def delete_student(self):
        """删除学生成绩"""
        name = self.delete_entry.get().strip()

        if not name:
            messagebox.showwarning("输入错误", "请输入要删除的学生姓名！")
            return

        if name in self.grades:
            if messagebox.askyesno("确认删除", f"确定要删除 {name} 的成绩吗？"):
                del self.grades[name]
                self.refresh_data()
                self.auto_save()  # 自动保存到文件
                messagebox.showinfo("成功", f"已成功删除 {name} 的成绩！\n数据已自动保存到DATA目录")
            self.delete_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("删除失败", f"找不到学生: {name}")

    def on_double_click(self, event):
        """双击树形视图中的项，填充到编辑框"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            name, score = self.tree.item(item, "values")
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.score_entry.delete(0, tk.END)
            self.score_entry.insert(0, score)

    def load_from_file(self):
        """从DATA目录加载学生成绩数据"""
        if os.path.exists(self.data_file):
            try:
                df = pd.read_excel(self.data_file)
                self.grades = dict(zip(df['姓名'].astype(str), df['成绩'].astype(float)))
                print(f"已从 {os.path.basename(self.data_file)} 加载 {len(self.grades)} 条记录")
            except Exception as e:
                print(f"加载数据失败: {e}")
                # 使用默认数据
                self.grades = {
                    '小明': 95.0,
                    '小智': 88.0,
                    '小强': 60.0
                }
        else:
            print(f"数据文件不存在，使用默认数据")
            self.grades = {
                '小明': 95.0,
                '小智': 88.0,
                '小强': 60.0
            }

    def save_to_file(self):
        """保存学生成绩数据到DATA目录"""
        try:
            # 确保DATA目录存在
            data_dir = os.path.dirname(self.data_file)
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)

            # 备份现有文件
            if os.path.exists(self.data_file):
                if os.path.exists(self.backup_file):
                    os.remove(self.backup_file)
                os.rename(self.data_file, self.backup_file)

            # 保存新数据
            df = pd.DataFrame(list(self.grades.items()), columns=["姓名", "成绩"])
            df = df.sort_values('姓名')  # 按姓名排序
            df.to_excel(self.data_file, index=False)
            print(f"数据已保存到 {self.data_file}")
            print(f"已保存 {len(self.grades)} 条学生记录")
            return True
        except Exception as e:
            messagebox.showerror("保存失败", f"保存数据到文件失败:\n{str(e)}")
            return False

    def auto_save(self):
        """自动保存（每次修改后调用）"""
        self.save_to_file()

    def on_closing(self):
        """窗口关闭时的处理"""
        if messagebox.askyesno("退出确认", "退出前是否保存数据？"):
            if self.save_to_file():
                self.root.destroy()
        else:
            self.root.destroy()

    def export_excel(self):
        """导出成绩为Excel文件"""
        if not self.grades:
            messagebox.showwarning("警告", "没有数据可导出！")
            return

        filetypes = [
            ("Excel文件", "*.xlsx"),
            ("所有文件", "*.*")
        ]
        filepath = filedialog.asksaveasfilename(
            title="导出为Excel",
            defaultextension=".xlsx",
            filetypes=filetypes,
            initialfile="学生成绩表.xlsx"
        )

        if filepath:
            try:
                # 创建DataFrame
                df = pd.DataFrame(list(self.grades.items()), columns=["姓名", "成绩"])

                # 计算统计信息并添加到表格
                count = len(self.grades)
                scores = [float(s) for s in self.grades.values()]
                stats_data = [
                    ["总人数", count],
                    ["平均分", f"{sum(scores) / count:.2f}"],
                    ["最高分", max(scores)],
                    ["最低分", min(scores)]
                ]
                df_stats = pd.DataFrame(stats_data, columns=["统计项", "值"])

                # 保存到两个sheet
                with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name="成绩表", index=False)
                    df_stats.to_excel(writer, sheet_name="统计信息", index=False)

                messagebox.showinfo("成功", f"数据已导出到:\n{filepath}")
            except Exception as e:
                messagebox.showerror("错误", f"导出失败: {str(e)}")

        if filepath:
            try:
                # 创建DataFrame
                df = pd.DataFrame(list(self.grades.items()), columns=["姓名", "成绩"])

                # 计算统计信息并添加到表格
                stats_data = [
                    ["总人数", len(self.grades)],
                    ["平均分", f"{sum(int(s) for s in self.grades.values()) / len(self.grades):.2f}"],
                    ["最高分", max(int(s) for s in self.grades.values())],
                    ["最低分", min(int(s) for s in self.grades.values())]
                ]
                df_stats = pd.DataFrame(stats_data, columns=["统计项", "值"])

                # 保存到两个sheet
                with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name="成绩表", index=False)
                    df_stats.to_excel(writer, sheet_name="统计信息", index=False)

                messagebox.showinfo("成功", f"数据已导出到:\n{filepath}")
            except Exception as e:
                messagebox.showerror("错误", f"导出失败: {str(e)}")

    def export_text(self):
        """导出成绩为文本文件"""
        if not self.grades:
            messagebox.showwarning("警告", "没有数据可导出！")
            return

        filetypes = [
            ("文本文件", "*.txt"),
            ("所有文件", "*.*")
        ]
        filepath = filedialog.asksaveasfilename(
            title="导出为文本",
            defaultextension=".txt",
            filetypes=filetypes,
            initialfile="学生成绩表.txt"
        )

        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write("=" * 40 + "\n")
                    f.write("学生成绩管理系统 - 成绩单\n")
                    f.write("=" * 40 + "\n\n")

                    # 写入成绩表
                    f.write("【成绩表】\n")
                    f.write("-" * 40 + "\n")
                    f.write(f"{'姓名':<15} {'成绩':<10}\n")
                    f.write("-" * 40 + "\n")
                    for name, score in sorted(self.grades.items()):
                        f.write(f"{name:<15} {score:<10}\n")

                    # 写入统计信息
                    f.write("\n【统计信息】\n")
                    f.write("-" * 40 + "\n")
                    count = len(self.grades)
                    scores = [float(s) for s in self.grades.values()]
                    f.write(f"总人数: {count}\n")
                    f.write(f"平均分: {sum(scores) / count:.2f}\n")
                    f.write(f"最高分: {max(scores)}\n")
                    f.write(f"最低分: {min(scores)}\n")

                messagebox.showinfo("成功", f"数据已导出到:\n{filepath}")
            except Exception as e:
                messagebox.showerror("错误", f"导出失败: {str(e)}")


def main():
    """主函数 - 独立运行时使用"""
    root = tk.Tk()
    app = StudentGradeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
