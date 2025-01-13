from django.shortcuts import render

 

# Create your views here.

from django.http import HttpResponse
from urllib.parse import unquote



def 路由功能(request):
    return HttpResponse("路由功能 默认页.   Demo 5512  Demo 5512 ")
    # return render(request, 'home.html')


def 单个匹配(request):
    data = "单个匹配"
    return HttpResponse(f"单个匹配  Demo 5512 : {data}")

 

# 在视图中使用
def 正则匹配后续所有(request):
    full_url = request.build_absolute_uri()
    decoded_name = unquote(full_url) # 路由中的中文编码转码
    # print(f"re_path 匹配后续所有 {decoded_name}  {type(decoded_name)}")
    return HttpResponse(f"re_path  Demo 5512 正则匹配后续所有/.*$ {decoded_name}")

def all(request):
    return HttpResponse("re_path  Demo 5512 路由功能 无匹配,进入匹配所有")



