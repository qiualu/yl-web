import logging
import urllib.parse


 
def 请求网站的编码转中文(msg,url_Start,url_end):
    # 找到 URL 编码部分的起始和结束位置
    start_index = msg.find(url_Start)
    end_index = msg.find(url_end, start_index)
    if start_index != -1 and end_index != -1:
        url_encoded = msg[start_index + len(url_Start):end_index]
        url_decoded = urllib.parse.unquote(url_encoded)  # 解码 URL 编码部分
        msg = msg[:start_index + len(url_Start)] + url_decoded + msg[end_index:]  # 替换 URL 编码部分为解码后的中文
    return msg

class UnicodeURLFormatter(logging.Formatter):
    def format(self, record):
        msg = super().format(record)
        # print("LOG 自定义入 :  ",msg,type(msg))
        # 在这里处理需要转换的部分，假设我们的消息格式为：'[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s'
        # 假设消息中有一个变量是 url，代表需要转换的 URL 编码部分
        if 'url' in record.__dict__:
            
            url_encoded = record.__dict__['url']
            url_decoded = urllib.parse.unquote(url_encoded)  # 解码 URL 编码部分

            # print("LOG 自定义 url_encoded : ", url_encoded)
            # print("LOG 自定义 url_decoded : ", url_decoded)
             
            msg = msg.replace(url_encoded, url_decoded)  # 替换日志消息中的 URL 编码部分为解码后的中文

        # 假设消息格式为：'[2024-07-02 16:43:03] INFO [django.server:212] "GET /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/1524563jjj HTTP/1.1" 200 40'
        url_GET  = '"GET /'
        url_POST = '"POST /'
        url_HTTP = ' HTTP/'
 
        if url_GET in msg and url_HTTP in msg:
            msg = 请求网站的编码转中文(msg,url_GET,url_HTTP)
        elif url_POST in msg and url_HTTP in msg:
            msg = 请求网站的编码转中文(msg,url_POST,url_HTTP)
 
 
        # print("LOG 自定义出 :  ", msg)
        return msg


# 使用自定义的 formatter
unicode_url_formatter = UnicodeURLFormatter('[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')

 




 


