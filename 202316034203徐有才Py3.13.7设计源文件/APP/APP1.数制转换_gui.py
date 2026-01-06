# ==========================================
# App1. 数制转换 - GUI版本
# ==========================================

import tkinter as tk
from tkinter import ttk

def main():
    """主函数 - 独立运行时使用"""
    root = tk.Tk()
    root.title("数制转换 - GUI")
    root.geometry("500x400")
    root.configure(bg="#f0f0f0")

    # 创建主框架
    main_frame = ttk.Frame(root, padding="30")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # 标题
    title_label = ttk.Label(
        main_frame,
        text="数制转换",
        font=("Helvetica", 18, "bold"),
        foreground="#1E90FF"
    )
    title_label.pack(pady=20)

    # 输入区域
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=20)

    input_label = ttk.Label(input_frame, text="请输入十进制整数:", font=("Helvetica", 12))
    input_label.pack(side=tk.LEFT, padx=5)

    input_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=20)
    input_entry.pack(side=tk.LEFT, padx=5)
    input_entry.focus()

    # 结果显示区域
    result_frame = ttk.LabelFrame(main_frame, text="转换结果", padding="15")
    result_frame.pack(fill=tk.X, pady=20)

    # 二进制
    bin_frame = ttk.Frame(result_frame)
    bin_frame.pack(fill=tk.X, pady=5)
    ttk.Label(bin_frame, text="二进制:", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT, padx=5)
    bin_label = ttk.Label(bin_frame, text="", font=("Helvetica", 11), foreground="#1E90FF")
    bin_label.pack(side=tk.LEFT, padx=5)

    # 八进制
    oct_frame = ttk.Frame(result_frame)
    oct_frame.pack(fill=tk.X, pady=5)
    ttk.Label(oct_frame, text="八进制:", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT, padx=5)
    oct_label = ttk.Label(oct_frame, text="", font=("Helvetica", 11), foreground="#1E90FF")
    oct_label.pack(side=tk.LEFT, padx=5)

    # 十六进制
    hex_frame = ttk.Frame(result_frame)
    hex_frame.pack(fill=tk.X, pady=5)
    ttk.Label(hex_frame, text="十六进制:", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT, padx=5)
    hex_label = ttk.Label(hex_frame, text="", font=("Helvetica", 11), foreground="#1E90FF")
    hex_label.pack(side=tk.LEFT, padx=5)

    # 转换函数
    def convert():
        value = input_entry.get()
        try:
            number = int(value)
            bin_label.config(text=bin(number))
            oct_label.config(text=oct(number))
            hex_label.config(text=hex(number))
            error_label.config(text="", foreground="")
        except ValueError:
            bin_label.config(text="")
            oct_label.config(text="")
            hex_label.config(text="")
            error_label.config(text="请输入有效的整数！", foreground="red")

    # 清空函数
    def clear():
        input_entry.delete(0, tk.END)
        bin_label.config(text="")
        oct_label.config(text="")
        hex_label.config(text="")
        error_label.config(text="", foreground="")
        input_entry.focus()

    # 错误提示
    error_label = ttk.Label(main_frame, text="", font=("Helvetica", 11))
    error_label.pack(pady=10)

    # 按钮区域
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=20)

    convert_btn = ttk.Button(button_frame, text="转换", command=convert, style="Accent.TButton")
    convert_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = ttk.Button(button_frame, text="清空", command=clear)
    clear_btn.pack(side=tk.LEFT, padx=5)

    # 配置样式
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 12, "bold"), padding=(20, 10))

    # 绑定回车键
    root.bind('<Return>', lambda e: convert())

    root.mainloop()


if __name__ == "__main__":
    main()
