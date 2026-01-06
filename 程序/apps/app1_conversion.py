import tkinter as tk
from tkinter import ttk

def run():
    root = tk.Toplevel()
    root.title("数制转换工具")
    root.geometry("600x400")
    root.configure(bg="#f0f0f0")
    
    # 创建主框架
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # 标题
    title_label = ttk.Label(main_frame, text="数制转换", 
                           font=("Helvetica", 16, "bold"), foreground="#1E90FF")
    title_label.pack(pady=10)
    
    # 输入区域
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=10)
    
    input_label = ttk.Label(input_frame, text="输入数字:", font=("Helvetica", 12))
    input_label.pack(side=tk.LEFT, padx=5)
    
    input_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=30)
    input_entry.pack(side=tk.LEFT, padx=5)
    
    # 进制选择
    base_frame = ttk.Frame(main_frame)
    base_frame.pack(fill=tk.X, pady=10)
    
    from_label = ttk.Label(base_frame, text="源进制:", font=("Helvetica", 12))
    from_label.pack(side=tk.LEFT, padx=5)
    
    from_base = ttk.Combobox(base_frame, values=["二进制", "八进制", "十进制", "十六进制"], 
                            font=("Helvetica", 12), width=10)
    from_base.set("十进制")
    from_base.pack(side=tk.LEFT, padx=5)
    
    to_label = ttk.Label(base_frame, text="目标进制:", font=("Helvetica", 12))
    to_label.pack(side=tk.LEFT, padx=5)
    
    to_base = ttk.Combobox(base_frame, values=["二进制", "八进制", "十进制", "十六进制"], 
                          font=("Helvetica", 12), width=10)
    to_base.set("二进制")
    to_base.pack(side=tk.LEFT, padx=5)
    
    # 转换结果
    result_frame = ttk.Frame(main_frame)
    result_frame.pack(fill=tk.X, pady=10)
    
    result_label = ttk.Label(result_frame, text="转换结果:", font=("Helvetica", 12))
    result_label.pack(side=tk.LEFT, padx=5)
    
    result_entry = ttk.Entry(result_frame, font=("Helvetica", 12), width=30, state="readonly")
    result_entry.pack(side=tk.LEFT, padx=5)
    
    # 转换函数
    def convert():
        try:
            num = input_entry.get()
            from_b = from_base.get()
            to_b = to_base.get()
            
            # 转换为十进制
            if from_b == "二进制":
                dec = int(num, 2)
            elif from_b == "八进制":
                dec = int(num, 8)
            elif from_b == "十进制":
                dec = int(num)
            elif from_b == "十六进制":
                dec = int(num, 16)
            else:
                raise ValueError("不支持的进制")
            
            # 转换为目标进制
            if to_b == "二进制":
                result = bin(dec)
            elif to_b == "八进制":
                result = oct(dec)
            elif to_b == "十进制":
                result = str(dec)
            elif to_b == "十六进制":
                result = hex(dec).upper()
            else:
                raise ValueError("不支持的进制")
            
            # 显示结果
            result_entry.config(state="normal")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, result)
            result_entry.config(state="readonly")
            
        except Exception as e:
            result_entry.config(state="normal")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, f"错误: {str(e)}")
            result_entry.config(state="readonly")
    
    # 转换按钮
    convert_button = ttk.Button(main_frame, text="开始转换", command=convert, 
                               style="Accent.TButton")
    convert_button.pack(pady=20)
    
    # 配置样式
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 12), padding=10)
    
    root.mainloop()

if __name__ == "__main__":
    run()