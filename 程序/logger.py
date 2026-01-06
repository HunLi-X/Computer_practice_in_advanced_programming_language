import logging
from datetime import datetime
import os

def setup_logger(name, log_file='app.log', level=logging.INFO):
    """
    设置日志记录器
    :param name: 日志记录器名称
    :param log_file: 日志文件名
    :param level: 日志级别
    :return: 日志记录器
    """
    # 创建logs目录
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # 格式化日志消息
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # 创建文件处理器
    handler = logging.FileHandler(os.path.join('logs', log_file))
    handler.setFormatter(formatter)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.addHandler(console_handler)
    
    return logger

def log_error(logger, error_message):
    """
    记录错误日志
    :param logger: 日志记录器
    :param error_message: 错误消息
    """
    logger.error(error_message)

def log_info(logger, info_message):
    """
    记录信息日志
    :param logger: 日志记录器
    :param info_message: 信息消息
    """
    logger.info(info_message)

def log_debug(logger, debug_message):
    """
    记录调试日志
    :param logger: 日志记录器
    :param debug_message: 调试消息
    """
    logger.debug(debug_message)