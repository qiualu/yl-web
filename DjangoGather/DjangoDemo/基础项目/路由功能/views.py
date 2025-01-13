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
    return HttpResponse(f"单个匹配 : {data}")


def 匹配整数(request,year):
    return HttpResponse(f"匹配整数 : {year}")

def 匹配字符串(request,name):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url) # 路由中的中文编码转码
    return HttpResponse(f"  匹配字符串 : {name} <br> <br>  {decoded_name}")

def 注册自定义的路径转换器(request,name):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url) # 路由中的中文编码转码
    print(f" 注册自定义的路径转换器 {name}  {type(name)}")
    return HttpResponse(f"  注册自定义的路径转换器 : {name} <br> <br>  {decoded_name}")

def 正则首页路由(request):
    return HttpResponse("正则首页路由 默认页.")

def 正则_匹配数字(request,name=0):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url)  # 路由中的中文编码转码
    return HttpResponse(f"正则_匹配数字  {decoded_name} name: {name}")

def 正则_匹配年月(request,month,year):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url)  # 路由中的中文编码转码
    return HttpResponse(f"正则_匹配数字  {decoded_name} year: {year} month:{month}")


def 正则_匹配汉字(request):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url)  # 路由中的中文编码转码
    return HttpResponse(f"正则_匹配汉字  {decoded_name}")

def 正则_匹配英文和数字(request):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url)  # 路由中的中文编码转码
    return HttpResponse(f"正则_匹配英文和数字  {decoded_name}")


# 在视图中使用
def 正则匹配后续所有(request):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url) # 路由中的中文编码转码
    # print(f"re_path 匹配后续所有 {decoded_name}  {type(decoded_name)}")
    return HttpResponse(f"re_path 正则匹配后续所有/.*$ {decoded_name}")

def all(request):
    return HttpResponse("re_path 路由功能 无匹配,进入匹配所有")









