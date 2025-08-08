from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from urllib.parse import unquote

import urllib.parse


def 路由功能(request):
    # return HttpResponse("路由功能 默认页.")
    return render(request, 'home.html')


def 单个匹配(request):
    data = "单个匹配"
    return HttpResponse(f"单个匹配 : {data} Xend")


def 匹配整数(request,year):
    return HttpResponse(f"匹配整数 : {year}")
 

# 在视图中使用
def 正则匹配后续所有(request):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url) # 路由中的中文编码转码
    # print(f"re_path 匹配后续所有 {decoded_name}  {type(decoded_name)}")
    return HttpResponse(f"re_path 正则匹配后续所有/.*$ {decoded_name}")


# http://127.0.0.1:8000/案例模板/福案例用户/23

def all(request):
    return HttpResponse("re_path 案例模板.公共类.案例模板路由分配 无匹配,进入匹配所有")









