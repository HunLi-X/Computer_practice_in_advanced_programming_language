# ==========================================
# App3. 七段数码管绘制程序
# 基于: App3=7SegLED.py
# 核心逻辑: Turtle绘图 + 函数封装
# ==========================================

import turtle
import time


# 1. 绘制单段线条的函数 (画一条线，然后向右转90度)
def drawLine(draw):
    # 如果 draw 为 True，就落笔画线；否则抬笔空走
    # 知识点: 01python绘制蟒蛇.py (turtle基础)
    if draw:
        turtle.pendown()
    else:
        turtle.penup()

    turtle.fd(40)  # 向前40像素
    turtle.right(90)  # 向右转90度


# 2. 绘制单个数字的函数 (核心填空部分)
# 逻辑：数码管共7段，按顺序判断该数字是否需要画这一段
def drawDigit(digit):
    # 第一步：画下半部分 (4段)
    # [填空 aaaaa] 中间横线 (2,3,4,5,6,8,9 需要)
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)

    # [填空 bbbbbb] 右下竖线 (0,1,3,4,5,6,7,8,9 需要)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)

    # [填空 ccccc] 底部横线 (0,2,3,5,6,8,9 需要)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)

    # [填空 ddddd] 左下竖线 (0,2,6,8 需要)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)

    # 转弯，准备画上半部分
    turtle.left(90)

    # 第二步：画上半部分 (3段)
    # [填空 eeeeee] 左上竖线 (0,4,5,6,8,9 需要)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)

    # [填空 ffffff] 顶部横线 (0,2,3,5,6,7,8,9 需要)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)

    # [填空 gggggg] 右上竖线 (0,1,2,3,4,7,8,9 需要)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)

    # 画完一个数字，归位并移动到下一个位置
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)  # 两个数字之间的间隔


# 3. 绘制整串日期的函数
def drawDate(date):
    for i in date:
        # eval() 将字符 '1' 转为数字 1
        drawDigit(eval(i))


# 4. 主函数
def main():
    turtle.setup(800, 350, 200, 200)  # 设置窗口大小
    turtle.penup()
    turtle.fd(-300)  # 从左边开始画
    turtle.pensize(5)  # 设置笔的粗细

    # 这里可以修改为你想要的日期，比如今天的 '20260107'
    drawDate('20260107')

    turtle.hideturtle()
    turtle.done()

    # 防止程序运行完直接关闭
    # input("按回车键，退出应用程序...")
    # (注：turtle.done() 通常会阻塞，如果窗口闪退，可以把上面这行input的注释去掉)


if __name__ == '__main__':
    main()