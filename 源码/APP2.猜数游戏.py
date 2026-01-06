# ==========================================
# App2. 猜数游戏 (Guessing Game)
# 源程序修改自: 06_6_game.py
# ==========================================

import random

# 1. 生成随机数 (1-100)
# 知识点来源: 06_6_game.py
number = random.randint(1, 100)

guess = 0  # 计数器，记录猜了几次

print("=== 猜数游戏已启动 (1-100) ===")

# 2. 循环结构 (Game Loop)
# 知识点来源: 06_1while.py [cite: 6]
while True:
    num_input = input("请猜一个1到100的数字: ")
    guess += 1  # 计数器+1

    # 3. 输入有效性检查 (老师代码自带)
    if not num_input.isdigit():
        print("输入错误：请输入纯数字。")
    elif int(num_input) < 0 or int(num_input) > 100:
        print("输入错误：数字必须介于1到100之间。")
    else:
        # === 下面是填空完成的核心逻辑 ===
        # 知识点来源: 054_if_elif_else.py

        # 填空1: 判断相等
        if number == int(num_input):
            print("恭喜您，您猜对了！您总共猜了 %d 次" % guess)
            break  # 猜对后退出循环

        # 填空2: 提示"猜小了" -> 说明 目标值 > 输入值
        elif number > int(num_input):
            print("您输入的数字小了。 (再大一点)")

        # 填空3: 提示"猜大了" -> 说明 目标值 < 输入值
        elif number < int(num_input):
            print("您输入的数字大了。 (再小一点)")

        else:
            print("系统发生不可预测问题。")

input("按回车键退出程序...")