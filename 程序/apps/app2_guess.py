import tkinter as tk
from tkinter import ttk
import random

def run():
    root = tk.Toplevel()
    root.title("猜数游戏")
    root.geometry("500x400")
    root.configure(bg="#f0f0f0")
    
    # 生成随机数
    target_number = random.randint(1, 100)
    guess_count = 0
    
    # 创建主框架
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # 标题
    title_label = ttk.Label(main_frame, text="猜数游戏", 
                           font=("Helvetica", 16, "bold"), foreground="#1E90FF")
    title_label.pack(pady=10)
    
    # 游戏说明
    instruction_label = ttk.Label(main_frame, text="我已经生成了一个1-100之间的数字，开始猜吧！", 
                                font=("Helvetica", 12))
    instruction_label.pack(pady=5)
    
    # 输入区域
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=10)
    
    input_label = ttk.Label(input_frame, text="你的猜测:", font=("Helvetica", 12))
    input_label.pack(side=tk.LEFT, padx=5)
    
    guess_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=10)
    guess_entry.pack(side=tk.LEFT, padx=5)
    
    # 结果显示
    result_label = ttk.Label(main_frame, text="", 
                           font=("Helvetica", 12, "bold"), foreground="#FF0000")
    result_label.pack(pady=20)
    
    # 猜测次数
    count_label = ttk.Label(main_frame, text="猜测次数: 0", 
                           font=("Helvetica", 12))
    count_label.pack(pady=5)
    
    # 猜测函数
    def make_guess():
        nonlocal guess_count
        try:
            guess = int(guess_entry.get())
            guess_count += 1
            count_label.config(text=f"猜测次数: {guess_count}")
            
            if guess < target_number:
                result_label.config(text="太小了，再试一次！")
            elif guess > target_number:
                result_label.config(text="太大了，再试一次！")
            else:
                result_label.config(text=f"恭喜你，猜对了！总共用了{guess_count}次尝试！", 
                                  foreground="#008000")
                guess_button.config(state=tk.DISABLED)
                reset_button.config(state=tk.NORMAL)
            
        except ValueError:
            result_label.config(text="请输入有效的数字！")
    
    # 重置游戏
    def reset_game():
        nonlocal target_number, guess_count
        target_number = random.randint(1, 100)
        guess_count = 0
        guess_entry.delete(0, tk.END)
        result_label.config(text="我已经生成了一个新的数字，开始猜吧！", 
                          foreground="#FF0000")
        count_label.config(text="猜测次数: 0")
        guess_button.config(state=tk.NORMAL)
        reset_button.config(state=tk.DISABLED)
    
    # 按钮区域
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=20)
    
    guess_button = ttk.Button(button_frame, text="提交猜测", command=make_guess, 
                             style="Accent.TButton")
    guess_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    reset_button = ttk.Button(button_frame, text="重置游戏", command=reset_game, 
                             style="TButton", state=tk.DISABLED)
    reset_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    # 配置样式
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 12), padding=10)
    
    root.mainloop()

if __name__ == "__main__":
    run()