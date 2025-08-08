import logging
import urllib.parse


def 解析URL编码为中文(消息, url_起始, url_结束):
    """
    将URL中编码的中文转换为可读中文
    参数:
        消息: 原始日志消息
        url_起始: URL编码部分的起始标识（如"GET /"）
        url_结束: URL编码部分的结束标识（如" HTTP/"）
    返回:
        转换后的日志消息
    """
    # 查找URL编码部分的位置
    起始索引 = 消息.find(url_起始)
    结束索引 = 消息.find(url_结束, 起始索引)
    
    if 起始索引 != -1 and 结束索引 != -1:
        # 提取URL编码部分并解码
        url_编码部分 = 消息[起始索引 + len(url_起始) : 结束索引]
        url_解码部分 = urllib.parse.unquote(url_编码部分)  # 核心：将%XX格式转为中文
        # 替换原始消息中的编码部分
        消息 = 消息[:起始索引 + len(url_起始)] + url_解码部分 + 消息[结束索引:]
    return 消息


class UnicodeURL日志格式化器(logging.Formatter):
    """自定义日志格式化器，用于处理URL中的中文编码"""
    
    def format(self, 记录):
        """重写format方法，处理日志中的中文编码"""
        # 先调用父类方法获取原始格式化后的消息
        消息 = super().format(记录)
        
        # 处理日志记录中显式包含的"url"字段（如自定义日志中的URL参数）
        if 'url' in 记录.__dict__:
            url_编码 = 记录.__dict__['url']
            url_解码 = urllib.parse.unquote(url_编码)
            消息 = 消息.replace(url_编码, url_解码)  # 替换编码后的URL为中文
        
        # 处理HTTP请求日志（如Django服务器默认的访问日志）
        # 识别GET/POST请求的URL编码部分
        请求_GET标识 = '"GET /'
        请求_POST标识 = '"POST /'
        请求_HTTP标识 = ' HTTP/'
        
        # 对GET请求的URL进行解码
        if 请求_GET标识 in 消息 and 请求_HTTP标识 in 消息:
            消息 = 解析URL编码为中文(消息, 请求_GET标识, 请求_HTTP标识)
        # 对POST请求的URL进行解码
        elif 请求_POST标识 in 消息 and 请求_HTTP标识 in 消息:
            消息 = 解析URL编码为中文(消息, 请求_POST标识, 请求_HTTP标识)
        
        return 消息


# 实例化自定义格式化器，定义日志输出格式
中文URL日志格式 = UnicodeURL日志格式化器(
    '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s'
)

