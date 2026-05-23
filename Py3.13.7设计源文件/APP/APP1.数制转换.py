# ==========================================
# App1. 数制转换程序
# 支持任意进制之间的转换
# ==========================================

def convert_base(value, from_base, to_base):
    """进制转换核心函数"""
    # 将原进制字符串转为十进制整数
    try:
        decimal_value = int(value, from_base)
        # 将十进制整数转为目标进制字符串
        if to_base == 2:
            result = bin(decimal_value)[2:]
        elif to_base == 8:
            result = oct(decimal_value)[2:]
        elif to_base == 16:
            result = hex(decimal_value)[2:].upper()
        else:
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if decimal_value == 0:
                result = "0"
            else:
                result = ""
                is_negative = decimal_value < 0
                decimal_value = abs(decimal_value)
                while decimal_value > 0:
                    result = digits[decimal_value % to_base] + result
                    decimal_value = decimal_value // to_base
                if is_negative:
                    result = "-" + result
        return result
    except ValueError:
        return None

def main():
    print('=== 欢迎使用数制转换 App ===')
    print('支持任意进制之间的转换（2-36进制）')
    print()

    # 1. 获取原进制
    from_base = input('请输入原进制 (2/8/10/16/32/36，默认10): ').strip()
    if not from_base:
        from_base = 10
    else:
        from_base = int(from_base)

    # 2. 获取输入数值
    if from_base == 10:
        input_str = input(f'请输入一个十进制整数: ')
    else:
        input_str = input(f'请输入一个 {from_base} 进制数: ')

    try:
        # 3. 先转为十进制整数验证输入
        decimal_value = int(input_str, from_base)

        # 4. 输出十进制值
        print('-' * 50)
        print(f'原值 ({from_base}进制):', input_str)
        print(f'十进制 (Decimal):', decimal_value)
        print()

        # 5. 获取目标进制
        print('可选目标进制: 2(二进制) 8(八进制) 10(十进制) 16(十六进制) 32 36')
        to_base = input('请输入目标进制 (默认显示全部常用进制，留空): ').strip()

        if to_base:
            # 转换到指定进制
            to_base = int(to_base)
            result = convert_base(input_str, from_base, to_base)
            print(f'{to_base}进制: {result}')
        else:
            # 显示所有常用进制
            print('全部常用进制转换:')
            print(f'二进制  (2)  : {convert_base(str(decimal_value), 10, 2)}')
            print(f'八进制  (8)  : {convert_base(str(decimal_value), 10, 8)}')
            print(f'十进制 (10) : {decimal_value}')
            print(f'十六进制(16) : {convert_base(str(decimal_value), 10, 16)}')
            print(f'32进制 (32) : {convert_base(str(decimal_value), 10, 32)}')
            print(f'36进制 (36) : {convert_base(str(decimal_value), 10, 36)}')

        print('-' * 50)

    except ValueError as e:
        print(f'输入错误：请输入有效的 {from_base} 进制数！')
        print(f'提示：{from_base}进制只能使用 {convert_base(str(from_base-1), 10, 10)} 到 {convert_base(str(from_base-1), 10, 16)} 之间的字符')

    # 等待用户按回车键退出
    input('\n按回车键退出...')


if __name__ == '__main__':
    main()