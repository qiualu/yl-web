from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

def index(request):
    return HttpResponse("OK")


def info1(request, id, page):
    print(f"id={id}, page={page}")
    return HttpResponse("OK")


def info2(request, mobile):
    print(f"mobile={mobile}")
    return HttpResponse("OK")





"""路由转换器[了解]"""
def inbuild_reverse(request, num):
    """"内置路由转换器"""
    return HttpResponse(f"num={num}")

def inbuild_reverse2(request, content):
    """"内置路由转换器"""
    return HttpResponse(f"content={content}")

def inbuild_reverse3(request, ustr):
    """"内置路由转换器"""
    return HttpResponse(f"ustr={ustr}")



def info5(request, mobile):
    print(f"mobile={mobile}")
    return HttpResponse("ok, info5")

