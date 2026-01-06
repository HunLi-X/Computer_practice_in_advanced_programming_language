#用七段数码管显示年月日
#设计函数drawDigit(digit)，在aaa、bbb、ccc、ddd、eee、fff、ggg处将源程序补充完整
#运行App3=7SegLED.exe看运行效果，就是我们的设计任务
import turtle
import time

def drawLine(draw):
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)

def drawDigit(digit):
    drawLine(True) aaaaa
    drawLine(True) bbbbbb
    drawLine(True) ccccc
    drawLine(True) ddddd
    turtle.left(90)
    drawLine(True) eeeeee
    drawLine(True) ffffff
    drawLine(True) gggggg
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):
    for i in date:
        drawDigit(eval(i))

def main():
#   turtle.tracer(False) #True关闭动画效果
    turtle.tracer(True) #True开启动画效果
	
    turtle.speed(10) #0最快,1最慢,2,3,,5中速,,9,10快速
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20190420')
    turtle.hideturtle()
    turtle.done()
    
    input("按回车键，退出应用程序，返回操作系统")
main()
    
