import re

def is_valid_number(input_str, base=10):
    """
    验证输入字符串是否为有效的数字
    :param input_str: 输入字符串
    :param base: 进制（默认10进制）
    :return: 是否有效
    """
    if base == 2:
        pattern = r'^[01]+$'
    elif base == 8:
        pattern = r'^[0-7]+$'
    elif base == 10:
        pattern = r'^[0-9]+$'
    elif base == 16:
        pattern = r'^[0-9A-Fa-f]+$'
    else:
        return False
    
    return bool(re.match(pattern, input_str))

def validate_score(score):
    """
    验证成绩是否有效
    :param score: 成绩
    :return: 是否有效
    """
    try:
        score = int(score)
        return 0 <= score <= 100
    except ValueError:
        return False

def format_number(number, base=10):
    """
    格式化数字显示
    :param number: 数字
    :param base: 进制
    :return: 格式化后的字符串
    """
    if base == 2:
        return f"0b{bin(number)[2:]}"
    elif base == 8:
        return f"0o{oct(number)[2:]}"
    elif base == 16:
        return f"0x{hex(number)[2:].upper()}"
    else:
        return str(number)

def get_file_extension(filename):
    """
    获取文件扩展名
    :param filename: 文件名
    :return: 扩展名
    """
    return filename.split('.')[-1].lower() if '.' in filename else ""