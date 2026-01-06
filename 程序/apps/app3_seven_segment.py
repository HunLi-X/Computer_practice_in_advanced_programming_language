import tkinter as tk
from tkinter import ttk

def run():
    root = tk.Toplevel()
    root.title("七段数码管绘制")
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
    
    # 创建主框架
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # 标题
    title_label = ttk.Label(main_frame, text="七段数码管绘制", 
                           font=("Helvetica", 16, "bold"), foreground="#1E90FF")
    title_label.pack(pady=10)
    
    # 输入区域
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=10)
    
    input_label = ttk.Label(input_frame, text="输入数字:", font=("Helvetica", 12))
    input_label.pack(side=tk.LEFT, padx=5)
    
    input_entry = ttk.Entry(input_frame, font=("Helvetica", 12), width=20)
    input_entry.pack(side=tk.LEFT, padx=5)
    
    # 画布
    canvas_frame = ttk.Frame(main_frame)
    canvas_frame.pack(fill=tk.BOTH, expand=True, pady=20)
    
    canvas = tk.Canvas(canvas_frame, bg="white", bd=2, relief=tk.SUNKEN)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # 绘制函数
    def draw_number():
        number = input_entry.get()
        if not number.isdigit():
            result_label.config(text="请输入有效的数字！", foreground="#FF0000")
            return
        
        result_label.config(text=f"正在绘制数字: {number}", foreground="#000000")
        
        # 清空画布
        canvas.delete("all")
        
        # 获取画布尺寸
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        if canvas_width == 1:  # 处理初始化时画布宽度为1的情况
            canvas_width = canvas_frame.winfo_width()
        if canvas_height == 1:
            canvas_height = canvas_frame.winfo_height()
        
        # 计算每个数字的位置
        digit_width = canvas_width // len(number)
        digit_height = canvas_height
        # 使用更大的尺寸比例
        segment_length = min(digit_width // 2, digit_height // 3)
        segment_width = segment_length // 8
        vertical_height = segment_length * 2
        
        # 绘制每个数字
        for i, digit in enumerate(number):
            digit_x = i * digit_width + digit_width // 2
            digit_y = digit_height // 2
            
            # 绘制七段
            for segment, state in enumerate(segments.get(digit, [0]*7)):
                if state == 1:
                    draw_segment(digit_x, digit_y, segment, segment_length, segment_width, vertical_height)
    
    # 绘制单个段
    def draw_segment(x, y, segment, segment_length, segment_width, vertical_height):
        color = "#1E90FF"
        half_length = segment_length // 2
        half_vertical = vertical_height // 2
        gap = segment_width

        # 段的坐标定义（标准七段数码管布局）
        # 0:上横, 1:右上竖, 2:右下竖, 3:下横, 4:左下竖, 5:左上竖, 6:中横
        segment_positions = {
            0: ((x - half_length, y - half_vertical - gap), (x + half_length, y - half_vertical - gap)),  # 上横
            1: ((x + half_length, y - half_vertical), (x + half_length, y)),                             # 右上竖
            2: ((x + half_length, y), (x + half_length, y + half_vertical)),                               # 右下竖
            3: ((x - half_length, y + half_vertical + gap), (x + half_length, y + half_vertical + gap)),  # 下横
            4: ((x - half_length, y), (x - half_length, y + half_vertical)),                               # 左下竖
            5: ((x - half_length, y - half_vertical), (x - half_length, y)),                             # 左上竖
            6: ((x - half_length, y), (x + half_length, y))                                                # 中横
        }

        if segment in segment_positions:
            (x1, y1), (x2, y2) = segment_positions[segment]
            canvas.create_line(x1, y1, x2, y2, width=segment_width, fill=color, capstyle=tk.ROUND)
    
    # 绘制按钮
    draw_button = ttk.Button(main_frame, text="开始绘制", command=draw_number, 
                            style="Accent.TButton")
    draw_button.pack(pady=10)
    
    # 结果提示
    result_label = ttk.Label(main_frame, text="", font=("Helvetica", 12))
    result_label.pack(pady=5)
    
    # 配置样式
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 12), padding=10)
    
    root.mainloop()

if __name__ == "__main__":
    run()