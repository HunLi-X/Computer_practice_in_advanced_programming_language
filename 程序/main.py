import tkinter as tk
from tkinter import ttk
from apps import app1_conversion, app2_guess, app3_seven_segment, app4_score, app5_excel

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("高级语言上机实习项目")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # 创建主框架
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建标题
        title_label = ttk.Label(main_frame, text="高级语言上机实习项目", 
                              font=("Helvetica", 20, "bold"), foreground="#1E90FF")
        title_label.pack(pady=20)
        
        # 创建应用按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # 应用按钮配置
        apps = [
            ("数制转换", app1_conversion.run),
            ("猜数游戏", app2_guess.run),
            ("七段数码管绘制", app3_seven_segment.run),
            ("学生成绩管理", app4_score.run),
            ("Excel文件处理", app5_excel.run)
        ]
        
        # 创建按钮
        for i, (app_name, app_func) in enumerate(apps):
            button = ttk.Button(button_frame, text=app_name, command=app_func, 
                               style="App.TButton", width=20)
            button.grid(row=i//2, column=i%2, padx=20, pady=15)
        
        # 配置样式
        style = ttk.Style()
        style.configure("App.TButton", font=("Helvetica", 12), padding=10)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()