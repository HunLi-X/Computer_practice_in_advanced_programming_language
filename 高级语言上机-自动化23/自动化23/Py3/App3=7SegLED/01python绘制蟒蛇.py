#绘制蟒蛇
import turtle
turtle.speed(10) #0最快,1最慢,2,3,,5中速,,9,10快速
turtle.setup(650,350,200,200) #(宽,高,x,y像素)
turtle.penup()     #笔抬起来
turtle.fd(-250)    #海龟向前进直线
turtle.pendown()   #落笔
turtle.pensize(25) #笔尖宽度
turtle.pencolor('purple')#笔色
turtle.seth(-40)         #绝对角度-40°
for i in range(4):       #i=0,1,2,3
    turtle.circle(40,80) #圆心左，半径40，80°弧
    turtle.circle(-40,80)#圆心右，半径40，80°弧

turtle.circle(40,80/2)   #圆心左，半径40，40°弧
turtle.fd(40)            #海龟坐标前进40像素
turtle.circle(16,180)    #圆心左，半径16，180°弧
turtle.fd(40*2/3)        #海龟坐标前进40*2/3像素
turtle.done()            #

input("按回车键，退出App，返回操作系统")

