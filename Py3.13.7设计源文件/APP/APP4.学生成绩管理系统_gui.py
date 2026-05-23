# ==========================================
# App4. 学生成绩管理系统 - GUI版本（CustomTkinter 美化）
# 功能: 字典操作、数据持久化
# ==========================================

import sys
import os
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog, messagebox

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
    "success":      "#10B981",
    "danger":       "#EF4444",
    "danger_hover": "#DC2626",
    "warning":      "#F59E0B",
    "text":         "#E2E8F0",
    "text_muted":   "#64748B",
    "input_bg":     "#0F172A",
    "tree_bg":      "#0F172A",
    "tree_fg":      "#E2E8F0",
    "tree_heading":  "#1E293B",
}

# 字体参数（延迟创建，避免 RuntimeError）
FONT_PARAMS = {
    "hero":       {"family": "Microsoft YaHei", "size": 20, "weight": "bold"},
    "heading":    {"family": "Microsoft YaHei", "size": 13, "weight": "bold"},
    "body":       {"family": "Microsoft YaHei", "size": 12},
    "small":      {"family": "Microsoft YaHei", "size": 10},
}

PADING = {
    "xs": 3,
    "sm": 6,
    "md": 10,
    "lg": 14,
    "xl": 18,
}

DATA_DIR  = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "DATA")
DATA_FILE = os.path.join(DATA_DIR, "学生成绩表.xlsx")
BACKUP_FILE = os.path.join(DATA_DIR, "学生成绩表_备份.xlsx")


class StudentGradeApp(ctk.CTk):
    """学生成绩管理系统主窗口"""

    def __init__(self):
        super().__init__()
        # 延迟创建字体（此时根窗口已存在）
        self._fonts = {k: ctk.CTkFont(**v) for k, v in FONT_PARAMS.items()}
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
        self.geometry("1000x580")
        self.minsize(800, 480)
        self.configure(fg_color=COLORS["bg"])
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - 1000) // 2
        y = (self.winfo_screenheight() - 580) // 2
        self.geometry(f"+{x}+{y}")

    # ==================== 构建 UI ====================

    def _build_ui(self):
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=PADING["lg"], pady=(PADING["lg"], PADING["md"]))

        # ---- 标题区 ----
        self._build_header(main)

        # ---- 左右分栏 ----
        body = ctk.CTkFrame(main, fg_color="transparent")
        body.pack(fill="both", expand=True, pady=(PADING["md"], 0))

        # 左侧：Treeview
        self._build_tree(body)

        # 右侧：操作面板
        self._build_sidepanel(body)

    def _build_header(self, parent):
        header = ctk.CTkFrame(parent, fg_color="transparent")
        header.pack(fill="x", pady=(0, PADING["xs"]))
        ctk.CTkLabel(header, text="📊  学生成绩管理系统", font=self._fonts["hero"], text_color=COLORS["text"]).pack(side="left")
        ctk.CTkLabel(header, text="  字典操作  |  数据持久化  |  Excel 导入导出", font=self._fonts["small"], text_color=COLORS["text_muted"]).pack(side="left", padx=(PADING["sm"], 0), pady=(4, 0))

    # ---- 左侧 Treeview ----
    def _build_tree(self, parent):
        left = ctk.CTkFrame(parent, corner_radius=14, fg_color=COLORS["card"], border_color=COLORS["card_border"], border_width=1)
        left.pack(side="left", fill="both", expand=True, padx=(0, PADING["sm"]))

        # 标题
        ctk.CTkLabel(left, text="📋  成绩列表", font=self._fonts["heading"], text_color=COLORS["text"]).pack(anchor="w", padx=PADING["md"], pady=(PADING["md"], PADING["sm"]))

        # 统计标签
        self._tree_stats = ctk.CTkLabel(left, text="总人数: 0", font=self._fonts["small"], text_color=COLORS["text_muted"], anchor="w")
        self._tree_stats.pack(anchor="w", padx=PADING["md"], pady=(0, PADING["sm"]))

        # Treeview 容器
        tree_frame = ctk.CTkFrame(left, fg_color="transparent")
        tree_frame.pack(fill="both", expand=True, padx=PADING["md"], pady=(0, PADING["md"]))

        # 配置 ttk.Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=COLORS["tree_bg"], foreground=COLORS["tree_fg"], fieldbackground=COLORS["tree_bg"], borderwidth=0, rowheight=32, font=("Microsoft YaHei", 14))
        style.configure("Treeview.Heading", background=COLORS["tree_heading"], foreground=COLORS["text"], font=("Microsoft YaHei", 15, "bold"))
        style.map("Treeview", background=[("selected", COLORS["primary"])])

        # 用 ttk.Treeview（customtkinter 没有 CTkTreeview）
        self._tree = ttk.Treeview(tree_frame, columns=("name", "score"), show="headings", height=15)
        self._tree.heading("name", text="姓名")
        self._tree.heading("score", text="成绩")
        self._tree.column("name", width=140, anchor="center")
        self._tree.column("score", width=80, anchor="center")
        self._tree.pack(side="left", fill="both", expand=True)

        scroll = ctk.CTkScrollbar(tree_frame, command=self._tree.yview, width=12)
        self._tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

        self._tree.bind("<Double-Button-1>", lambda _: self._on_double_click())

    # ---- 右侧操作面板 ----
    def _build_sidepanel(self, parent):
        right = ctk.CTkFrame(parent, width=260, corner_radius=12, fg_color=COLORS["card"], border_color=COLORS["card_border"], border_width=1)
        right.pack(side="right", fill="both", padx=(PADING["sm"], 0))
        right.pack_propagate(False)

        inner = ctk.CTkScrollableFrame(right, fg_color="transparent")
        inner.pack(fill="both", expand=True)
        inner._scrollbar.configure(width=4)

        # ---- 查询 ----
        self._section(inner, "🔍 查询成绩")
        q_frame = ctk.CTkFrame(inner, fg_color="transparent")
        q_frame.pack(fill="x", padx=PADING["md"], pady=(0, PADING["xs"]))

        self._q_entry = ctk.CTkEntry(q_frame, placeholder_text="输入姓名", height=28, fg_color=COLORS["input_bg"], font=self._fonts["body"])
        self._q_entry.pack(fill="x", pady=(0, PADING["xs"]))
        ctk.CTkButton(q_frame, text="查询", height=28, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"], command=self._query).pack(fill="x")
        self._q_entry.bind("<Return>", lambda _: self._query())

        # ---- 添加/修改 ----
        self._section(inner, "✏️ 添加 / 修改")
        a_frame = ctk.CTkFrame(inner, fg_color="transparent")
        a_frame.pack(fill="x", padx=PADING["md"], pady=(0, PADING["xs"]))

        self._name_entry = ctk.CTkEntry(a_frame, placeholder_text="姓名", height=28, fg_color=COLORS["input_bg"], font=self._fonts["body"])
        self._name_entry.pack(fill="x", pady=(0, PADING["xs"]))
        self._score_entry = ctk.CTkEntry(a_frame, placeholder_text="成绩 (0-100)", height=28, fg_color=COLORS["input_bg"], font=self._fonts["body"])
        self._score_entry.pack(fill="x", pady=(0, PADING["xs"]))
        ctk.CTkButton(a_frame, text="保存", height=28, font=self._fonts["heading"], corner_radius=8, fg_color=COLORS["success"], hover_color="#059669", command=self._save).pack(fill="x")
        self._name_entry.bind("<Return>", lambda _: self._score_entry.focus())
        self._score_entry.bind("<Return>", lambda _: self._save())

        # ---- 删除 ----
        self._section(inner, "🗑️ 删除成绩")
        d_frame = ctk.CTkFrame(inner, fg_color="transparent")
        d_frame.pack(fill="x", padx=PADING["md"], pady=(0, PADING["xs"]))

        self._del_entry = ctk.CTkEntry(d_frame, placeholder_text="输入姓名", height=28, fg_color=COLORS["input_bg"], font=self._fonts["body"])
        self._del_entry.pack(fill="x", pady=(0, PADING["xs"]))
        ctk.CTkButton(d_frame, text="删除", height=28, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["danger"], hover_color=COLORS["danger_hover"], command=self._delete).pack(fill="x")
        self._del_entry.bind("<Return>", lambda _: self._delete())

        # ---- 导出 ----
        self._section(inner, "📁 导出数据")
        e_frame = ctk.CTkFrame(inner, fg_color="transparent")
        e_frame.pack(fill="x", padx=PADING["md"], pady=(0, PADING["xs"]))

        ctk.CTkButton(e_frame, text="📊 导出 Excel", height=28, font=self._fonts["body"], corner_radius=8, command=self._export_excel).pack(fill="x", pady=(0, PADING["xs"]))
        ctk.CTkButton(e_frame, text="📝 导出文本", height=28, font=self._fonts["body"], corner_radius=8, fg_color=COLORS["secondary"], hover_color="#334155", command=self._export_text).pack(fill="x")

        # ---- 统计 ----
        self._section(inner, "📈 统计信息")
        s_frame = ctk.CTkFrame(inner, fg_color="transparent")
        s_frame.pack(fill="x", padx=PADING["md"], pady=(0, PADING["md"]))

        self._lbl_count = ctk.CTkLabel(s_frame, text="总人数: 0", anchor="w", font=self._fonts["small"], text_color=COLORS["text"])
        self._lbl_count.pack(fill="x", pady=1)
        self._lbl_avg = ctk.CTkLabel(s_frame, text="平均分: —", anchor="w", font=self._fonts["small"], text_color=COLORS["text"])
        self._lbl_avg.pack(fill="x", pady=1)
        self._lbl_max = ctk.CTkLabel(s_frame, text="最高分: —", anchor="w", font=self._fonts["small"], text_color=COLORS["text"])
        self._lbl_max.pack(fill="x", pady=1)
        self._lbl_min = ctk.CTkLabel(s_frame, text="最低分: —", anchor="w", font=self._fonts["small"], text_color=COLORS["text"])
        self._lbl_min.pack(fill="x", pady=1)

    # ---- 辅助：分区标题 ----
    def _section(self, parent, text: str):
        ctk.CTkLabel(parent, text=text, font=self._fonts["heading"], text_color=COLORS["text"]).pack(anchor="w", padx=PADING["md"], pady=(PADING["md"], PADING["xs"]))

    # ==================== 数据逻辑 ====================

    def _refresh_tree(self):
        for item in self._tree.get_children():
            self._tree.delete(item)
        for name, score in sorted(self.grades.items()):
            self._tree.insert("", "end", values=(name, f"{score:.1f}"))
        self._refresh_stats()

    def _refresh_stats(self):
        n = len(self.grades)
        self._tree_stats.configure(text=f"总人数: {n}")
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

    # ---- 查询 ----
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

    # ---- 保存 ----
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

    # ---- 删除 ----
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

    # ---- 双击填充 ----
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
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel 文件", "*.xlsx")], initialfile="学生成绩表.xlsx")
        if not path:
            return
        try:
            df   = pd.DataFrame(sorted(self.grades.items()), columns=["姓名", "成绩"])
            stats = pd.DataFrame([["总人数", len(self.grades)], ["平均分", f"{sum(self.grades.values())/len(self.grades):.2f}"], ["最高分", max(self.grades.values())], ["最低分", min(self.grades.values())]], columns=["统计项", "值"])
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
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("文本文件", "*.txt")], initialfile="学生成绩表.txt")
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
