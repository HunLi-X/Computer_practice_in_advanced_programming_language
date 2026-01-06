import tkinter as tk
from tkinter import ttk, messagebox

def run():
    root = tk.Toplevel()
    root.title("学生成绩管理系统")
    root.geometry("600x500")
    root.configure(bg="#f0f0f0")
    
    # 初始化学生成绩数据
    scores = {
        "张三": 95,
        "李四": 88,
        "王五": 76,
        "赵六": 92,
        "钱七": 85
    }
    
    # 创建主框架
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # 标题
    title_label = ttk.Label(main_frame, text="学生成绩管理系统", 
                           font=("Helvetica", 16, "bold"), foreground="#1E90FF")
    title_label.pack(pady=10)
    
    # 输入区域
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=10)
    
    name_label = ttk.Label(input_frame, text="学生姓名:", font=("Helvetica", 12))
    name_label.pack(side=tk.LEFT, padx=5)
    
    name_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=20)
    name_entry.pack(side=tk.LEFT, padx=5)
    
    score_label = ttk.Label(input_frame, text="成绩:", font=("Helvetica", 12))
    score_label.pack(side=tk.LEFT, padx=5, pady=5)
    
    score_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=10)
    score_entry.pack(side=tk.LEFT, padx=5)
    
    # 结果区域
    result_frame = ttk.Frame(main_frame)
    result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    
    result_text = tk.Text(result_frame, wrap=tk.WORD, font=("Helvetica", 12))
    result_text.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=5)
    
    scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=result_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    result_text.config(yscrollcommand=scrollbar.set)
    
    # 显示所有学生成绩
    def show_all():
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "学生成绩列表:\n")
        result_text.insert(tk.END, "-" * 30 + "\n")
        for name, score in scores.items():
            result_text.insert(tk.END, f"{name}: {score}\n")
    
    # 查询学生成绩
    def query_score():
        name = name_entry.get().strip()
        if not name:
            messagebox.showwarning("警告", "请输入学生姓名！")
            return
        
        if name in scores:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"查询结果:\n")
            result_text.insert(tk.END, "-" * 30 + "\n")
            result_text.insert(tk.END, f"{name}的成绩是: {scores[name]}\n")
        else:
            messagebox.showinfo("信息", "未找到该学生的成绩！")
    
    # 删除学生成绩
    def delete_score():
        name = name_entry.get().strip()
        if not name:
            messagebox.showwarning("警告", "请输入学生姓名！")
            return
        
        if name in scores:
            del scores[name]
            messagebox.showinfo("成功", f"已删除{name}的成绩！")
            show_all()
        else:
            messagebox.showinfo("信息", "未找到该学生的成绩！")
    
    # 修改学生成绩
    def modify_score():
        name = name_entry.get().strip()
        if not name:
            messagebox.showwarning("警告", "请输入学生姓名！")
            return
        
        score_text = score_entry.get().strip()
        if not score_text:
            messagebox.showwarning("警告", "请输入成绩！")
            return
        
        try:
            score = int(score_text)
            if score < 0 or score > 100:
                messagebox.showwarning("警告", "成绩必须在0-100之间！")
                return
            
            if name in scores:
                scores[name] = score
                messagebox.showinfo("成功", f"已修改{name}的成绩为: {score}！")
                show_all()
            else:
                messagebox.showinfo("信息", "未找到该学生的成绩！")
        except ValueError:
            messagebox.showwarning("警告", "请输入有效的数字成绩！")
    
    # 按钮区域
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=10)
    
    query_button = ttk.Button(button_frame, text="查询成绩", command=query_score)
    query_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    delete_button = ttk.Button(button_frame, text="删除成绩", command=delete_score)
    delete_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    modify_button = ttk.Button(button_frame, text="修改成绩", command=modify_score)
    modify_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    show_button = ttk.Button(button_frame, text="显示全部", command=show_all)
    show_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    # 显示初始数据
    show_all()
    
    # 配置样式
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)
    
    root.mainloop()

if __name__ == "__main__":
    run()