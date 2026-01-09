# ==========================================
# App2. 猜数游戏 - GUI版本
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import random

class GuessNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("猜数游戏 - GUI")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        # 生成随机数
        self.target_number = random.randint(1, 100)
        self.guess_count = 0

        # 创建主框架
        main_frame = ttk.Frame(root, padding="30")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="猜数游戏",
            font=("Helvetica", 18, "bold"),
            foreground="#1E90FF"
        )
        title_label.pack(pady=20)

        # 游戏说明
        info_label = ttk.Label(
            main_frame,
            text="猜一个 1 到 100 之间的数字",
            font=("Helvetica", 12),
            foreground="#666666"
        )
        info_label.pack(pady=10)

        # 输入区域
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(pady=20)

        ttk.Label(input_frame, text="你的猜测:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)

        self.input_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=15)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_entry.focus()

        # 按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=15)

        guess_btn = ttk.Button(button_frame, text="猜!", command=self.guess, style="Accent.TButton")
        guess_btn.pack(side=tk.LEFT, padx=5)

        new_game_btn = ttk.Button(button_frame, text="新游戏", command=self.new_game)
        new_game_btn.pack(side=tk.LEFT, padx=5)

        # 结果显示
        self.result_label = ttk.Label(
            main_frame,
            text="",
            font=("Helvetica", 14, "bold"),
            foreground="#333333"
        )
        self.result_label.pack(pady=20)

        # 统计信息
        stats_frame = ttk.LabelFrame(main_frame, text="统计信息", padding="10")
        stats_frame.pack(fill=tk.X, pady=15)

        self.count_label = ttk.Label(stats_frame, text="猜测次数: 0", font=("Helvetica", 11))
        self.count_label.pack()

        # 配置样式
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Helvetica", 12, "bold"), padding=(15, 10))

        # 绑定回车键
        self.root.bind('<Return>', lambda e: self.guess())

    def guess(self):
        """处理猜测"""
        value = self.input_entry.get()

        if not value.isdigit():
            self.result_label.config(text="请输入有效的数字！", foreground="red")
            return

        guess_num = int(value)

        if guess_num < 1 or guess_num > 100:
            self.result_label.config(text="数字必须在 1 到 100 之间！", foreground="orange")
            return

        self.guess_count += 1
        self.count_label.config(text=f"猜测次数: {self.guess_count}")

        if guess_num == self.target_number:
            self.result_label.config(
                text=f"🎉 恭喜你猜对了！答案就是 {self.target_number}",
                foreground="#1E90FF"
            )
            messagebox.showinfo(
                "成功",
                f"恭喜你！你用了 {self.guess_count} 次猜对了数字 {self.target_number}！"
            )
            self.input_entry.config(state="disabled")
        elif guess_num < self.target_number:
            self.result_label.config(text="📈 猜小了，再大一点！", foreground="#FF8C00")
        else:
            self.result_label.config(text="📉 猜大了，再小一点！", foreground="#FF8C00")

        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()

    def new_game(self):
        """开始新游戏"""
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.count_label.config(text="猜测次数: 0")
        self.result_label.config(text="", foreground="#333333")
        self.input_entry.config(state="normal")
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()


def main():
    """主函数 - 独立运行时使用"""
    root = tk.Tk()
    app = GuessNumberApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
