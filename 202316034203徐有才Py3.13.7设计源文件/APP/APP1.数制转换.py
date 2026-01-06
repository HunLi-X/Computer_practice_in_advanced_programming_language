# ==========================================
# App1. 数制转换程序
# ==========================================

def main():
    print('=== 欢迎使用数制转换 App ===')

    # 1. 获取输入
    # 虽然文件里多用 a=123 这种赋值，但在App中我们用 input() 让用户自己输入
    input_str = input('请输入一个十进制整数: ')

    try:
        # 2. 数据类型转换 (强制转换)
        # 知识点来源: cast.py
        # 用法: int(变量) 把字符串或浮点数转为整数
        number = int(input_str)

        # 3. 核心计算 (调用内置函数)
        # 知识点来源: 07str_bin(x)...py [cite: 5]
        data_bin = bin(number)

        # 知识点来源: 04str_oct(x)...py [cite: 6]
        data_oct = oct(number)

        # 知识点来源: 03str_hex(x)...py [cite: 2]
        data_hex = hex(number)

        # 4. 输出结果 (使用逗号分隔法)
        # 知识点来源: 02print_逗号.py
        # 老师演示了 print('文字', 变量) 的写法
        print('-' * 30)
        print('十进制 (Decimal) :', number)
        print('二进制 (Binary)  :', data_bin)
        print('八进制 (Octal)   :', data_oct)
        print('十六进制 (Hex)   :', data_hex)
        print('-' * 30)

        # [备选] 输出结果 (使用格式化符号法)
        # 知识点来源: 01print_formate.py
        # 老师演示了 '...%s...' % 变量 的写法
        # print('十六进制(格式化显示): %s' % data_hex)

    except ValueError:
        print('输入错误：请输入纯数字！')


if __name__ == '__main__':
    main()