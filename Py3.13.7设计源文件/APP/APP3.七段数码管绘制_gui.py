# ==========================================
# App3. 七段数码管绘制 - GUI版本
# ==========================================

import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import time

def main():
    """主函数 - 独立运行时使用"""
    root = tk.Tk()
    root.title("七段数码管绘制 - GUI")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")

    # 七段数码管定义
    segments = {
        '0': [1, 1, 1, 1, 1, 1, 0],
        '1': [0, 1, 1, 0, 0, 0, 0],
        '2': [1, 1, 0, 1, 1, 0, 1],
        '3': [1, 1, 1, 1, 0, 0, 1],
        '4': [0, 1, 1, 0, 0, 1, 1],
        '5': [1, 0, 1, 1, 0, 1, 1],
        '6': [1, 0, 1, 1, 1, 1, 1],
        '7': [1, 1, 1, 0, 0, 0, 0],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 0, 1, 1]
    }

    # 颜色变量
    segment_color = "#1E90FF"

    # 创建主框架
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # 标题
    title_label = ttk.Label(
        main_frame,
        text="七段数码管绘制",
        font=("Helvetica", 16, "bold"),
        foreground="#1E90FF"
    )
    title_label.pack(pady=10)

    # 控制面板
    control_frame = ttk.LabelFrame(main_frame, text="控制面板", padding="10")
    control_frame.pack(fill=tk.X, pady=10)

    # 第一行：输入和按钮
    row1 = ttk.Frame(control_frame)
    row1.pack(fill=tk.X, pady=5)

    ttk.Label(row1, text="输入数字:", font=("Helvetica", 11)).pack(side=tk.LEFT, padx=5)

    input_entry = ttk.Entry(row1, font=("Helvetica", 12), width=20)
    input_entry.pack(side=tk.LEFT, padx=5)
    input_entry.insert(0, "20260107")  # 默认日期

    draw_btn = ttk.Button(row1, text="绘制", command=lambda: draw_number(), style="Accent.TButton")
    draw_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = ttk.Button(row1, text="清空", command=lambda: canvas.delete("all"))
    clear_btn.pack(side=tk.LEFT, padx=5)

    # 第二行：颜色选择
    row2 = ttk.Frame(control_frame)
    row2.pack(fill=tk.X, pady=5)

    def choose_color():
        nonlocal segment_color
        color = colorchooser.askcolor(title="选择段颜色", initialcolor=segment_color)
        if color[1]:
            segment_color = color[1]
            color_btn.config(text=segment_color[:20])

    color_btn = ttk.Button(row2, text=segment_color[:20], command=choose_color)
    color_btn.pack(side=tk.LEFT, padx=5)

    ttk.Label(row2, text="点击选择段颜色").pack(side=tk.LEFT, padx=5)

    # 第三行：粗细控制
    row3 = ttk.Frame(control_frame)
    row3.pack(fill=tk.X, pady=5)

    ttk.Label(row3, text="段粗细:", font=("Helvetica", 11)).pack(side=tk.LEFT, padx=5)

    width_var = tk.IntVar(value=8)
    width_scale = ttk.Scale(row3, from_=3, to=20, variable=width_var, orient=tk.HORIZONTAL, length=150)
    width_scale.pack(side=tk.LEFT, padx=5)

    width_label = ttk.Label(row3, text="8", font=("Helvetica", 11), width=3)
    width_label.pack(side=tk.LEFT, padx=5)

    def update_width_label(*args):
        width_label.config(text=str(width_var.get()))

    width_var.trace_add('write', update_width_label)

    # 第四行：动画开关
    row4 = ttk.Frame(control_frame)
    row4.pack(fill=tk.X, pady=5)

    animate_var = tk.BooleanVar(value=True)
    animate_check = ttk.Checkbutton(row4, text="显示绘制动画", variable=animate_var)
    animate_check.pack(side=tk.LEFT, padx=5)

    speed_label = ttk.Label(row4, text="动画速度:", font=("Helvetica", 11))
    speed_label.pack(side=tk.LEFT, padx=5)

    speed_var = tk.IntVar(value=100)
    speed_scale = ttk.Scale(row4, from_=10, to=500, variable=speed_var, orient=tk.HORIZONTAL, length=100)
    speed_scale.pack(side=tk.LEFT, padx=5)

    speed_value_label = ttk.Label(row3, text="100ms", font=("Helvetica", 9))
    speed_value_label.pack(side=tk.LEFT, padx=5)

    def update_speed_label(*args):
        speed_value_label.config(text=f"{speed_var.get()}ms")

    speed_var.trace_add('write', update_speed_label)

    # 画布
    canvas_frame = ttk.LabelFrame(main_frame, text="显示区域", padding="10")
    canvas_frame.pack(fill=tk.BOTH, expand=True, pady=20)

    canvas = tk.Canvas(canvas_frame, bg="white", bd=2, relief=tk.SUNKEN)
    canvas.pack(fill=tk.BOTH, expand=True)

    # 绘制函数
    def draw_number():
        number = input_entry.get()
        if not number.isdigit():
            result_label.config(text="请输入有效的数字！", foreground="#FF0000")
            return

        result_label.config(text=f"正在绘制: {number}", foreground="#000000")

        # 清空画布
        canvas.delete("all")

        # 获取画布尺寸
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        if canvas_width == 1:
            canvas_width = canvas_frame.winfo_width()
        if canvas_height == 1:
            canvas_height = canvas_frame.winfo_height()

        # 计算尺寸
        digit_width = canvas_width // len(number)
        digit_height = canvas_height
        segment_length = min(digit_width // 2, digit_height // 3)
        segment_w = width_var.get()
        vertical_height = segment_length * 2

        # 绘制每个数字
        if animate_var.get():
            # 动画模式：逐段绘制
            segment_count = 0
            total_segments = sum(sum(segments.get(digit, [0]*7)) for digit in number)

            for i, digit in enumerate(number):
                digit_x = i * digit_width + digit_width // 2
                digit_y = digit_height // 2

                for segment, state in enumerate(segments.get(digit, [0]*7)):
                    if state == 1:
                        draw_segment(digit_x, digit_y, segment, segment_length, segment_w, vertical_height)
                        segment_count += 1
                        root.update()
                        time.sleep(speed_var.get() / 1000.0)
        else:
            # 非动画模式：一次性绘制
            for i, digit in enumerate(number):
                digit_x = i * digit_width + digit_width // 2
                digit_y = digit_height // 2

                # 绘制七段
                for segment, state in enumerate(segments.get(digit, [0]*7)):
                    if state == 1:
                        draw_segment(digit_x, digit_y, segment, segment_length, segment_w, vertical_height)

    # 绘制单个段
    def draw_segment(x, y, segment, segment_length, segment_width, vertical_height):
        half_length = segment_length // 2
        half_vertical = vertical_height // 2
        gap = segment_width

        segment_positions = {
            0: ((x - half_length, y - half_vertical - gap), (x + half_length, y - half_vertical - gap)),
            1: ((x + half_length, y - half_vertical), (x + half_length, y)),
            2: ((x + half_length, y), (x + half_length, y + half_vertical)),
            3: ((x - half_length, y + half_vertical + gap), (x + half_length, y + half_vertical + gap)),
            4: ((x - half_length, y), (x - half_length, y + half_vertical)),
            5: ((x - half_length, y - half_vertical), (x - half_length, y)),
            6: ((x - half_length, y), (x + half_length, y))
        }

        if segment in segment_positions:
            (x1, y1), (x2, y2) = segment_positions[segment]
            canvas.create_line(x1, y1, x2, y2, width=segment_width, fill=segment_color, capstyle=tk.ROUND)

    # 配置样式
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 11, "bold"), padding=(15, 8))

    # 结果提示
    result_label = ttk.Label(main_frame, text="", font=("Helvetica", 11))
    result_label.pack(pady=5)

    # 窗口大小改变时自动重绘（仅在非动画模式下）
    def on_configure(event):
        if event.widget == root and not animate_var.get():
            if input_entry.get().isdigit():
                root.after(100, draw_number)  # 延迟执行避免频繁触发

    root.bind('<Configure>', on_configure)

    root.mainloop()


if __name__ == "__main__":
    main()
