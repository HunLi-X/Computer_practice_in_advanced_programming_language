# ==========================================
# App4. 学生成绩管理系统 - GUI版本 (CustomTkinter 美化)
# ==========================================

import sys
import os
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog, messagebox

# ── 依赖检查 ──
try:
    import customtkinter as ctk
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "-q"])
    import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_DIR  = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "DATA")
DATA_FILE = os.path.join(DATA_DIR, "学生成绩表.xlsx")
BACKUP_FILE = os.path.join(DATA_DIR, "学生成绩表_备份.xlsx")


class StudentGradeApp(ctk.CTk):
    """学生成绩管理系统主窗口"""

    def __init__(self):
        super().__init__()
        self.grades = {}
        self._ensure_data_dir()
        self._load_data()
        self._setup_window()
        self._build_ui()
        self._refresh_tree()

    # ==================== 窗口设置 ====================

    def _ensure_data_dir(self):
        os.makedirs(DATA_DIR, exist_ok=True)

    def _setup_window(self):
        self.title("学生成绩管理系统")
        self.geometry("960x640")
        self.minsize(800, 520)
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - 960) // 2
        y = (self.winfo_screenheight() - 640) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=16, pady=(12, 8))

        # ── 标题 ──
        ctk.CTkLabel(
            main, text="📊  学生成绩管理系统",
            font=ctk.CTkFont(size=24, weight="bold"),
        ).pack(pady=(0, 4))

        ctk.CTkLabel(
            main, text="字典操作  |  数据持久化",
            font=ctk.CTkFont(size=12),
            text_color="gray60",
        ).pack(pady=(0, 10))

        # ── 左右分栏 ──
        body = ctk.CTkFrame(main, fg_color="transparent")
        body.pack(fill="both", expand=True)

        # 左侧：Treeview
        self._build_tree(body)

        # 右侧：操作面板
        self._build_sidepanel(body)

    # ── 左侧 Treeview ──
    def _build_tree(self, parent):
        left = ctk.CTkFrame(parent, corner_radius=12)
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        ctk.CTkLabel(left, text="📋  成绩列表", font=ctk.CTkFont(size=14, weight="bold")).pack(
            anchor="w", padx=12, pady=(10, 6)
        )

        # Treeview 容器（用 tk.Frame 包裹 ttk.Treeview）
        tree_frame = ctk.CTkFrame(left, fg_color="transparent")
        tree_frame.pack(fill="both", expand=True, padx=8, pady=(0, 10))

        # 用 ttk.Treeview（customtkinter 没有 CTkTreeview）
        self._tree = ttk.Treeview(
            tree_frame,
            columns=("name", "score"),
            show="headings",
            height=30,
        )
        self._tree.heading("name", text="姓名")
        self._tree.heading("score", text="成绩")
        self._tree.column("name", width=140, anchor="center")
        self._tree.column("score", width=80, anchor="center")
        self._tree.pack(side="left", fill="both", expand=True)

        scroll = ctk.CTkScrollbar(tree_frame, command=self._tree.yview)
        self._tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

        self._tree.bind("<Double-Button-1>", lambda _: self._on_double_click())

    # ── 右侧操作面板 ──
    def _build_sidepanel(self, parent):
        right = ctk.CTkScrollableFrame(parent, width=300, corner_radius=12)
        right.pack(side="right", fill="both", padx=(8, 0))
        right._scrollbar.configure(width=6)

        # ── 查询 ──
        self._section(right, "🔍  查询成绩")
        q_frame = ctk.CTkFrame(right, fg_color="transparent")
        q_frame.pack(fill="x", padx=12, pady=(0, 8))
        self._q_entry = ctk.CTkEntry(q_frame, placeholder_text="输入姓名")
        self._q_entry.pack(fill="x", pady=3)
        ctk.CTkButton(q_frame, text="查  询", height=34, command=self._query).pack(fill="x", pady=3)
        self._q_entry.bind("<Return>", lambda _: self._query())

        # ── 添加/修改 ──
        self._section(right, "✏️  添加 / 修改")
        a_frame = ctk.CTkFrame(right, fg_color="transparent")
        a_frame.pack(fill="x", padx=12, pady=(0, 8))
        self._name_entry = ctk.CTkEntry(a_frame, placeholder_text="姓名")
        self._name_entry.pack(fill="x", pady=3)
        self._score_entry = ctk.CTkEntry(a_frame, placeholder_text="成绩 (0-100)")
        self._score_entry.pack(fill="x", pady=3)
        ctk.CTkButton(a_frame, text="保  存", height=34, command=self._save).pack(fill="x", pady=3)
        self._name_entry.bind("<Return>", lambda _: self._score_entry.focus())
        self._score_entry.bind("<Return>", lambda _: self._save())

        # ── 删除 ──
        self._section(right, "🗑️  删除成绩")
        d_frame = ctk.CTkFrame(right, fg_color="transparent")
        d_frame.pack(fill="x", padx=12, pady=(0, 8))
        self._del_entry = ctk.CTkEntry(d_frame, placeholder_text="输入姓名")
        self._del_entry.pack(fill="x", pady=3)
        ctk.CTkButton(
            d_frame, text="删  除", height=34,
            fg_color="#E53935", hover_color="#C62828",
            command=self._delete,
        ).pack(fill="x", pady=3)
        self._del_entry.bind("<Return>", lambda _: self._delete())

        # ── 导出 ──
        self._section(right, "📁  导出数据")
        e_frame = ctk.CTkFrame(right, fg_color="transparent")
        e_frame.pack(fill="x", padx=12, pady=(0, 8))
        ctk.CTkButton(e_frame, text="📊  Excel", height=34, command=self._export_excel).pack(fill="x", pady=3)
        ctk.CTkButton(e_frame, text="📝  文本", height=34, command=self._export_text).pack(fill="x", pady=3)

        # ── 统计 ──
        self._section(right, "📈  统计信息")
        s_frame = ctk.CTkFrame(right, fg_color="transparent")
        s_frame.pack(fill="x", padx=12, pady=(0, 12))
        self._lbl_count = ctk.CTkLabel(s_frame, text="总人数: 0", anchor="w")
        self._lbl_count.pack(fill="x", pady=2)
        self._lbl_avg = ctk.CTkLabel(s_frame, text="平均分: —", anchor="w")
        self._lbl_avg.pack(fill="x", pady=2)
        self._lbl_max = ctk.CTkLabel(s_frame, text="最高分: —", anchor="w")
        self._lbl_max.pack(fill="x", pady=2)
        self._lbl_min = ctk.CTkLabel(s_frame, text="最低分: —", anchor="w")
        self._lbl_min.pack(fill="x", pady=2)

    # ── 辅助：分区标题 ──
    def _section(self, parent, text: str):
        ctk.CTkLabel(
            parent, text=text,
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(anchor="w", padx=12, pady=(10, 4))

    # ==================== 数据逻辑 ====================

    def _refresh_tree(self):
        for item in self._tree.get_children():
            self._tree.delete(item)
        for name, score in sorted(self.grades.items()):
            self._tree.insert("", "end", values=(name, f"{score:.1f}"))
        self._refresh_stats()

    def _refresh_stats(self):
        n = len(self.grades)
        if n == 0:
            self._lbl_count.configure(text="总人数: 0")
            self._lbl_avg.configure(text="平均分: —")
            self._lbl_max.configure(text="最高分: —")
            self._lbl_min.configure(text="最低分: —")
            return
        scores = list(self.grades.values())
        self._lbl_count.configure(text=f"总人数: {n}")
        self._lbl_avg.configure(text=f"平均分: {sum(scores)/n:.2f}")
        self._lbl_max.configure(text=f"最高分: {max(scores):.1f}")
        self._lbl_min.configure(text=f"最低分: {min(scores):.1f}")

    # ── 查询 ──
    def _query(self):
        name = self._q_entry.get().strip()
        if not name:
            messagebox.showwarning("提示", "请输入姓名")
            return
        if name in self.grades:
            messagebox.showinfo("查询结果", f"{name} 的成绩是: {self.grades[name]:.1f}")
        else:
            messagebox.showwarning("查询结果", f"未找到学生: {name}")
        self._q_entry.delete(0, "end")

    # ── 保存 ──
    def _save(self):
        name  = self._name_entry.get().strip()
        score_str = self._score_entry.get().strip()
        if not name:
            messagebox.showwarning("错误", "请输入姓名")
            return
        if not score_str:
            messagebox.showwarning("错误", "请输入成绩")
            return
        try:
            score = float(score_str)
            if not (0 <= score <= 100):
                raise ValueError
        except ValueError:
            messagebox.showerror("错误", "成绩必须是 0~100 之间的数字")
            return
        self.grades[name] = score
        self._refresh_tree()
        self._auto_save()
        messagebox.showinfo("成功", f"已保存 {name} 的成绩")
        self._name_entry.delete(0, "end")
        self._score_entry.delete(0, "end")
        self._name_entry.focus()

    # ── 删除 ──
    def _delete(self):
        name = self._del_entry.get().strip()
        if not name:
            messagebox.showwarning("错误", "请输入姓名")
            return
        if name not in self.grades:
            messagebox.showwarning("错误", f"未找到学生: {name}")
            return
        if messagebox.askyesno("确认", f"确定删除 {name} 的成绩吗？"):
            del self.grades[name]
            self._refresh_tree()
            self._auto_save()
            messagebox.showinfo("成功", f"已删除 {name}")
        self._del_entry.delete(0, "end")

    # ── 双击填充 ──
    def _on_double_click(self):
        sel = self._tree.selection()
        if not sel:
            return
        name, score = self._tree.item(sel[0], "values")
        self._name_entry.delete(0, "end")
        self._name_entry.insert(0, name)
        self._score_entry.delete(0, "end")
        self._score_entry.insert(0, score)
        self._name_entry.focus()

    # ==================== 文件 I/O ====================

    def _auto_save(self):
        self._save_to_file()

    def _load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                df = pd.read_excel(DATA_FILE)
                self.grades = dict(zip(df["姓名"].astype(str), df["成绩"].astype(float)))
            except Exception as e:
                print(f"加载失败: {e}")
                self._use_default()
        else:
            self._use_default()

    def _use_default(self):
        self.grades = {"小明": 95.0, "小智": 88.0, "小强": 60.0}

    def _save_to_file(self):
        try:
            if os.path.exists(DATA_FILE):
                if os.path.exists(BACKUP_FILE):
                    os.remove(BACKUP_FILE)
                os.rename(DATA_FILE, BACKUP_FILE)
            df = pd.DataFrame(sorted(self.grades.items()), columns=["姓名", "成绩"])
            df.to_excel(DATA_FILE, index=False)
        except Exception as e:
            messagebox.showerror("保存失败", str(e))

    def _export_excel(self):
        if not self.grades:
            messagebox.showwarning("提示", "没有数据可导出")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel 文件", "*.xlsx")],
            initialfile="学生成绩表.xlsx",
        )
        if not path:
            return
        try:
            df   = pd.DataFrame(sorted(self.grades.items()), columns=["姓名", "成绩"])
            stats = pd.DataFrame([
                ["总人数", len(self.grades)],
                ["平均分", f"{sum(self.grades.values())/len(self.grades):.2f}"],
                ["最高分", max(self.grades.values())],
                ["最低分", min(self.grades.values())],
            ], columns=["统计项", "值"])
            with pd.ExcelWriter(path, engine="openpyxl") as w:
                df.to_excel(w,   sheet_name="成绩表", index=False)
                stats.to_excel(w, sheet_name="统计信息", index=False)
            messagebox.showinfo("成功", f"已导出到:\n{path}")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def _export_text(self):
        if not self.grades:
            messagebox.showwarning("提示", "没有数据可导出")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt")],
            initialfile="学生成绩表.txt",
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("=" * 36 + "\n")
                f.write("  学生成绩管理系统  -  成绩单\n")
                f.write("=" * 36 + "\n\n")
                f.write(f"{'姓名':<12} {'成绩':<8}\n")
                f.write("-" * 36 + "\n")
                for name, score in sorted(self.grades.items()):
                    f.write(f"{name:<12} {score:<8.1f}\n")
                f.write("\n")
                n = len(self.grades)
                f.write(f"总人数: {n}\n")
                f.write(f"平均分: {sum(self.grades.values())/n:.2f}\n")
                f.write(f"最高分: {max(self.grades.values()):.1f}\n")
                f.write(f"最低分: {min(self.grades.values()):.1f}\n")
            messagebox.showinfo("成功", f"已导出到:\n{path}")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    # ==================== 关闭钩子 ====================

    def destroy(self):
        if messagebox.askyesno("退出确认", "退出前是否保存数据？"):
            self._save_to_file()
        super().destroy()


# ==================== 入口 ====================

if __name__ == "__main__":
    app = StudentGradeApp()
    app.mainloop()
