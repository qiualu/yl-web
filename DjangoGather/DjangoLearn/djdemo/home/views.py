from django.shortcuts import render

# Create your views here.



from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import QueryDict


# Create your views here.
def index(request):
    print("index视图运行了")
    # print(request.method)
    # print(request.headers)
    # print(request.body)
    # print(request.path)

    """获取查询字符串"""
    """
    请求地址：http://127.0.0.1:8000/home/index
    """
    print(request.GET)  # 获取地址栏上的所有的查询字符串，组成一个QueryDict查询字典对象
    """
    打印效果：<QueryDict: {}>
    QueryDict的声明位置: from django.http import QueryDict
    QueryDict的父类MultiValueDict继承的就是dict字典,所以字典提供的方法或者操作, QueryDict都有
    之所以使用QueryDict来保存请求参数的原因时：默认的字典的键是唯一的，所以会导致如果有多个值使用了同一个键，则字典会覆盖的。
    而django内部封装的QueryDict允许多个值使用了同一个键，会自动收集所有的值保存在一个列表中作为当前键的值区寄存起来。
    QueryDict常用的方法有2个：
    get(键, 默认值)     通过指定键获取最后1个值
    getlist(键, 默认值) 通过指定键获取所有值，并以列表格式返回
    """

    """
    请求地址：http://127.0.0.1:8000/home/index?name=xiapming&pwd=123
    """
    print(request.GET) # <QueryDict: {'name': ['xiaoming'], 'pwd': ['123']}>
    print(request.GET.get("name"))
    print(request.GET.get("pwd"))
    # print(request.Get["pwd"])  # 减少使用中括号，会在没有键的情况下导致程序报错
    """
    打印效果：
        13312345678
        xiapming
        123
    """

    """
    请求地址：http://127.0.0.1:8000/home/index/?name=xiaoming&mobile=13312345678&lve=swimming&lve=shopping&lve=game
    """
    print(request.GET.get("lve"))  # game
    print(request.GET.getlist("lve"))  # ['swimming', 'shopping', 'game']
    print(request.GET.getlist("name"))  # ['xiaoming']


    return HttpResponse("<h1>index</h1>")






