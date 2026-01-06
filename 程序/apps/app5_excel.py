import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

def run():
    root = tk.Toplevel()
    root.title("Excel文件处理工具")
    root.geometry("700x500")
    root.configure(bg="#f0f0f0")
    
    # 变量
    input_file = tk.StringVar()
    output_file = tk.StringVar()
    filter_column = tk.StringVar()
    filter_value = tk.StringVar()
    
    # 创建主框架
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # 标题
    title_label = ttk.Label(main_frame, text="Excel文件处理工具", 
                           font=("Helvetica", 16, "bold"), foreground="#1E90FF")
    title_label.pack(pady=10)
    
    # 文件选择区域
    file_frame = ttk.Frame(main_frame)
    file_frame.pack(fill=tk.X, pady=10)
    
    # 输入文件
    input_label = ttk.Label(file_frame, text="输入文件:", font=("Helvetica", 12))
    input_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    
    input_entry = ttk.Entry(file_frame, textvariable=input_file, font=("Helvetica", 12), width=40)
    input_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
    
    browse_input_button = ttk.Button(file_frame, text="浏览", command=lambda: browse_file(input_file))
    browse_input_button.grid(row=0, column=2, padx=5, pady=5)
    
    # 输出文件
    output_label = ttk.Label(file_frame, text="输出文件:", font=("Helvetica", 12))
    output_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    
    output_entry = ttk.Entry(file_frame, textvariable=output_file, font=("Helvetica", 12), width=40)
    output_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    
    browse_output_button = ttk.Button(file_frame, text="浏览", command=lambda: save_file(output_file))
    browse_output_button.grid(row=1, column=2, padx=5, pady=5)
    
    # 筛选条件区域
    filter_frame = ttk.Frame(main_frame)
    filter_frame.pack(fill=tk.X, pady=10)
    
    column_label = ttk.Label(filter_frame, text="筛选列名:", font=("Helvetica", 12))
    column_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    
    column_entry = ttk.Entry(filter_frame, textvariable=filter_column, font=("Helvetica", 12), width=20)
    column_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
    
    value_label = ttk.Label(filter_frame, text="筛选值:", font=("Helvetica", 12))
    value_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
    
    value_entry = ttk.Entry(filter_frame, textvariable=filter_value, font=("Helvetica", 12), width=20)
    value_entry.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
    
    # 数据预览区域
    preview_frame = ttk.Frame(main_frame)
    preview_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    
    preview_label = ttk.Label(preview_frame, text="数据预览:", font=("Helvetica", 12, "bold"))
    preview_label.pack(pady=5)
    
    preview_text = tk.Text(preview_frame, wrap=tk.WORD, font=("Helvetica", 10))
    preview_text.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=5)
    
    scrollbar = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL, command=preview_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    preview_text.config(yscrollcommand=scrollbar.set)
    
    # 浏览文件
    def browse_file(var):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel文件", "*.xlsx;*.xls"), ("所有文件", "*.*")]
        )
        if file_path:
            var.set(file_path)
            preview_data(file_path)
    
    # 保存文件
    def save_file(var):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")]
        )
        if file_path:
            var.set(file_path)
    
    # 预览数据
    def preview_data(file_path):
        try:
            df = pd.read_excel(file_path)
            preview_text.delete(1.0, tk.END)
            preview_text.insert(tk.END, "数据预览:\n")
            preview_text.insert(tk.END, "-" * 100 + "\n")
            preview_text.insert(tk.END, df.head().to_string() + "\n")
            preview_text.insert(tk.END, "-" * 100 + "\n")
            preview_text.insert(tk.END, f"总共有 {len(df)} 行数据, {len(df.columns)} 列数据\n")
        except Exception as e:
            messagebox.showerror("错误", f"预览数据失败: {str(e)}")
    
    # 处理文件
    def process_file():
        try:
            input_path = input_file.get()
            output_path = output_file.get()
            column = filter_column.get()
            value = filter_value.get()
            
            if not input_path or not output_path:
                messagebox.showwarning("警告", "请选择输入和输出文件！")
                return
            
            if not column or not value:
                messagebox.showwarning("警告", "请填写筛选条件！")
                return
            
            # 读取Excel文件
            df = pd.read_excel(input_path)
            
            # 筛选数据
            if column not in df.columns:
                messagebox.showwarning("警告", f"列 '{column}' 不存在于文件中！")
                return
            
            filtered_df = df[df[column] == value]
            
            if len(filtered_df) == 0:
                messagebox.showinfo("信息", "没有找到符合筛选条件的数据！")
                return
            
            # 保存筛选后的数据
            filtered_df.to_excel(output_path, index=False)
            
            messagebox.showinfo("成功", f"已成功筛选并保存文件！\n共筛选出 {len(filtered_df)} 行数据")
            
        except Exception as e:
            messagebox.showerror("错误", f"处理文件失败: {str(e)}")
    
    # 按钮区域
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=10)
    
    process_button = ttk.Button(button_frame, text="处理文件", command=process_file, 
                               style="Accent.TButton")
    process_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    # 配置样式
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 12), padding=10)
    style.configure("TButton", font=("Helvetica", 12), padding=5)
    
    root.mainloop()

if __name__ == "__main__":
    run()