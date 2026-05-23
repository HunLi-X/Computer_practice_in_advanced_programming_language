# ==========================================
# App1. 数制转换 - GUI版本
# 支持任意进制之间的转换
# ==========================================

import tkinter as tk
from tkinter import ttk

def convert_base(value, from_base, to_base):
    """进制转换核心函数"""
    # 将原进制字符串转为十进制整数
    try:
        decimal_value = int(value, from_base)
        # 将十进制整数转为目标进制字符串
        if to_base == 2:
            result = bin(decimal_value)[2:]
        elif to_base == 8:
            result = oct(decimal_value)[2:]
        elif to_base == 16:
            result = hex(decimal_value)[2:].upper()
        else:
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if decimal_value == 0:
                result = "0"
            else:
                result = ""
                is_negative = decimal_value < 0
                decimal_value = abs(decimal_value)
                while decimal_value > 0:
                    result = digits[decimal_value % to_base] + result
                    decimal_value = decimal_value // to_base
                if is_negative:
                    result = "-" + result
        return result
    except ValueError:
        return None

def main():
    """主函数 - 独立运行时使用"""
    root = tk.Tk()
    root.title("数制转换 - GUI")
    root.geometry("600x700")
    root.configure(bg="#f0f0f0")

    # 创建主框架
    main_frame = ttk.Frame(root, padding="30")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # 标题
    title_label = ttk.Label(
        main_frame,
        text="数制转换器",
        font=("Helvetica", 18, "bold"),
        foreground="#1E90FF"
    )
    title_label.pack(pady=20)

    # 原进制选择区域
    from_base_frame = ttk.Frame(main_frame)
    from_base_frame.pack(fill=tk.X, pady=10)

    ttk.Label(from_base_frame, text="原进制:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)

    from_base_var = tk.StringVar(value="10")
    from_base_combo = ttk.Combobox(from_base_frame, textvariable=from_base_var,
                                    values=["2", "8", "10", "16", "32", "36"],
                                    font=("Helvetica", 11), width=8, state="readonly")
    from_base_combo.pack(side=tk.LEFT, padx=5)

    # 输入区域
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=20)

    input_label = ttk.Label(input_frame, text="输入数值:", font=("Helvetica", 12))
    input_label.pack(side=tk.LEFT, padx=5)

    input_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=30)
    input_entry.pack(side=tk.LEFT, padx=5)
    input_entry.focus()

    # 目标进制选择区域
    to_base_frame = ttk.Frame(main_frame)
    to_base_frame.pack(fill=tk.X, pady=10)

    ttk.Label(to_base_frame, text="目标进制:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)

    to_base_var = tk.StringVar(value="2")
    to_base_combo = ttk.Combobox(to_base_frame, textvariable=to_base_var,
                                 values=["2", "8", "10", "16", "32", "36"],
                                 font=("Helvetica", 11), width=8, state="readonly")
    to_base_combo.pack(side=tk.LEFT, padx=5)

    # 结果显示区域
    result_frame = ttk.LabelFrame(main_frame, text="转换结果", padding="15")
    result_frame.pack(fill=tk.BOTH, expand=True, pady=20)

    result_label_frame = ttk.Frame(result_frame)
    result_label_frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(result_label_frame, text="转换结果:", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT, padx=5)
    result_label = ttk.Label(result_label_frame, text="", font=("Helvetica", 14), foreground="#1E90FF")
    result_label.pack(side=tk.LEFT, padx=5)

    # 同时显示所有常用进制
    all_results_frame = ttk.LabelFrame(result_frame, text="全部常用进制", padding="10")
    all_results_frame.pack(fill=tk.X, pady=15)

    all_bin_frame = ttk.Frame(all_results_frame)
    all_bin_frame.pack(fill=tk.X, pady=2)
    ttk.Label(all_bin_frame, text="二进制  :", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
    all_bin_label = ttk.Label(all_bin_frame, text="", font=("Helvetica", 10), foreground="#666")
    all_bin_label.pack(side=tk.LEFT, padx=5)

    all_oct_frame = ttk.Frame(all_results_frame)
    all_oct_frame.pack(fill=tk.X, pady=2)
    ttk.Label(all_oct_frame, text="八进制  :", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
    all_oct_label = ttk.Label(all_oct_frame, text="", font=("Helvetica", 10), foreground="#666")
    all_oct_label.pack(side=tk.LEFT, padx=5)

    all_dec_frame = ttk.Frame(all_results_frame)
    all_dec_frame.pack(fill=tk.X, pady=2)
    ttk.Label(all_dec_frame, text="十进制:", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
    all_dec_label = ttk.Label(all_dec_frame, text="", font=("Helvetica", 10), foreground="#666")
    all_dec_label.pack(side=tk.LEFT, padx=5)

    all_hex_frame = ttk.Frame(all_results_frame)
    all_hex_frame.pack(fill=tk.X, pady=2)
    ttk.Label(all_hex_frame, text="十六进制:", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
    all_hex_label = ttk.Label(all_hex_frame, text="", font=("Helvetica", 10), foreground="#666")
    all_hex_label.pack(side=tk.LEFT, padx=5)

    # 转换函数
    def convert():
        value = input_entry.get().strip()
        from_base = int(from_base_var.get())
        to_base = int(to_base_var.get())

        if not value:
            error_label.config(text="请输入数值！", foreground="red")
            result_label.config(text="")
            all_bin_label.config(text="")
            all_oct_label.config(text="")
            all_dec_label.config(text="")
            all_hex_label.config(text="")
            return

        try:
            # 先转为十进制验证输入
            decimal_value = int(value, from_base)

            # 转换到目标进制
            result = convert_base(value, from_base, to_base)
            result_label.config(text=result)

            # 同时显示所有常用进制
            all_bin_label.config(text=convert_base(str(decimal_value), 10, 2))
            all_oct_label.config(text=convert_base(str(decimal_value), 10, 8))
            all_dec_label.config(text=str(decimal_value))
            all_hex_label.config(text=convert_base(str(decimal_value), 10, 16))

            error_label.config(text="", foreground="")
        except ValueError:
            error_label.config(text=f"请输入有效的 {from_base} 进制数！", foreground="red")
            result_label.config(text="")
            all_bin_label.config(text="")
            all_oct_label.config(text="")
            all_dec_label.config(text="")
            all_hex_label.config(text="")

    # 清空函数
    def clear():
        input_entry.delete(0, tk.END)
        result_label.config(text="")
        all_bin_label.config(text="")
        all_oct_label.config(text="")
        all_dec_label.config(text="")
        all_hex_label.config(text="")
        error_label.config(text="", foreground="")
        from_base_var.set("10")
        to_base_var.set("2")
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
