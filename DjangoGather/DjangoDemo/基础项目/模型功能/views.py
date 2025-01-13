from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from urllib.parse import unquote

import urllib.parse



def 模型功能(request):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/
    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')
    # 打印解码后的请求路径
    print(f"请求路径: {decoded_path}")
    return HttpResponse("Hello, world. 模型功能.")
