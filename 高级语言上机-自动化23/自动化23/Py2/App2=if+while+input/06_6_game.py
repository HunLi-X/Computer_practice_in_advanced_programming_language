#猜字游戏编写
#目的：掌握if分支（选择）结构、while循环结构的程序设计
#大部分源程序已经给同学们，??????,xxxxx,yyyyyy,zzzzzz部分需要同学们编写
#运行可执行文件06_6_game.exe，可见设计任务（目标）
import random

number = random.randint(1,100)  #调用random模块的randint()函数，生成一个1到100的随机数
guess = 0                       #计数器，记录猜了几次
while True:
    num_input = input("请猜一个1到100的数字:")
    guess +=1                   #计数器+1，记录猜了几次
    if not num_input.isdigit():
        print ("请输入数字。")
    elif int(num_input)<0 or int(num_input)>=100:
        print ("输入的数字必须介于1到100。")
    else:
        if number??????xxxxxxx:
            print ("恭喜您，您猜对了，您总共猜了 %d 次"%guess)
            break
        elif number?????yyyyyy:
            print ("您输入的数字小了。")
        elif number?????zzzzzzz:
            print ("您输入的数字大了。")
        else:
            print ("系统发生不可预测问题，请联系管理人员进行处理。")
#请猜一个1到100的数字:50
#您输入的数字小了。
#请猜一个1到100的数字:75
#恭喜您，您猜对了，您总共猜了 2 次
input("按回车键，退出应用程序，返回操作系统")
