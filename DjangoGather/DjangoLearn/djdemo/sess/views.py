from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse



def set_session(request):
    """设置session"""
    # session保存在服务端，所以所有关于session的操作都是由request.session来完成的
    #
    request.session["uname"] = "root"
    request.session["uid"] = 1
    return HttpResponse("设置session数据")



def get_session(request):
    """获取session"""
    print(f"uname={request.session.get('uname')}") # format string python3.6提供的
    print(f"uid={request.session.get('uid')}")
    
    # 获取session所有的键值对
    print(request.session.items())
    
    # 获取session数据的有效，默认值是：2周 ==>  60 * 60 * 24 * 7 * 2
    print(request.session.get_session_cookie_age() )
    return HttpResponse("获取session数据")


def del_session(request):
    """删除session数据"""
    # 删除单个指定名称的session
    print(" del_session ",request.session.get("uname"))



    if request.session.get("uname"):
        print(" del_session ")
        request.session.pop("uname")

    # 删除所有的session，慎用
    # request.session.clear()
    return HttpResponse("删除session数据")





