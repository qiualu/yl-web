from django.shortcuts import render

# Create your views here.



from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import QueryDict

# http://127.0.0.1:8000/home/index
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
    print("home index : ",request.GET) # <QueryDict: {'name': ['xiaoming'], 'pwd': ['123']}>
    print("home index : ",request.GET.get("name"))
    print("home index : ",request.GET.get("pwd"))
    # print("home index : ",request.Get["pwd"])  # 减少使用中括号，会在没有键的情况下导致程序报错
    """
    打印效果：
        13312345678
        xiapming
        123
    """

    """
    请求地址：http://127.0.0.1:8000/home/index/?name=xiaoming&mobile=13312345678&lve=swimming&lve=shopping&lve=game
    """
    print("home index : ",request.GET.get("lve"))  # game
    print("home index : ",request.GET.getlist("lve"))  # ['swimming', 'shopping', 'game']
    print("home index : ",request.GET.getlist("name"))  # ['xiaoming']


    return HttpResponse("<h1>index</h1>")


# 让用户发送POST才能访问的页面
from django.views.decorators.http import require_http_methods


# 需要注释 settings -> 'django.middleware.csrf.CsrfViewMiddleware',
# http://127.0.0.1:8000/home/login/
@require_http_methods(["POST"])  # 注意，中括号中的请求方法名务必大写！！！否则无法正常显示
def login(request):

    print("home login : ",request.POST.getlist("name"))  # ['xiaoming']


    return HttpResponse("登录成功！")



# @require_http_methods(["POST", "PUT"])  # 注意，中括号中的请求方法名务必大写！！！否则无法正常显示
def index2(request):
    """获取请求体数据"""
    """
    访问地址：http://127.0.0.1:8000/home/index2
    请求体：不设置请求体
    """
    print("home index2 : ",request.POST)
    """
    request.POST获取的结果也是QueryDict查询字典对象
    <QueryDict: {}>
    """

    """
    访问地址：http://127.0.0.1:8000/home/index2
    请求体：name=xiaoming&age=16
    """
    print("home index2 : ",request.POST)

    """
    打印效果：
    <QueryDict: {'name': ['xiaoming'], 'age': ['16']}>
    """
    print("home index2 : ",request.POST.get("name"))


    """
    访问地址：http://127.0.0.1:8000/home/index2
    请求体：name=xiaoming&age=16&citys=["北京", "上海", "天津]
    """
    """
    打印效果：
    <QueryDict: {'name': ['xiaoming'], 'age': ['16'], 'citys': ['北京', '上海', '天津']}>
    """
    #
    print("home index2 : ",request.POST)  # ['北京', '上海', '天津']
    print("home index2 : ",request.POST.getlist("citys"))
    print("home index2 : ",request.POST.get("citys"))  # 天津


    """接收原生请求体中的json数据"""
    """
    请求地址：http://127.0.0.1:8000/home/index2
    请求体为json：'{"name": "xiaobai","age": 16}'
    """
    print("home index2 : ",request.POST)  # <QueryDict: {}>
    print("home index2 body: ",request.body)    # b'{\n    "name": "xiaobai",\n    "age": 16\n}'
    # import json
    # print("home index2 : ",json.loads(request.body))  # {'name': 'xiaobai', 'age': 16}

    

    return HttpResponse("index2！")


def index3(request):
    """接收请求体参数"""
    print(request.META) # 获取当前项目相关的服务器与客户端环境信息，也包含了请求头信息，以及服务端所在的系统的环境变量
    """
    {
        'LANG': 'zh_CN.UTF-8',    # 服务端系统的默认语言
        'USER': 'moluo',          # 服务端运行的系统用户名
        'HOME': '/home/moluo',    # 服务端运行的系统用户家目录路径
        'DJANGO_SETTINGS_MODULE': 'djdemo.settings',  # 只有在django下才有的，当前django框架运行时加载的配置文件导包路径
        'SERVER_NAME': 'ubuntu',             # 服务端系统名称
        'SERVER_PORT': '8000',               # 服务端的运行端口
        'REMOTE_HOST': '',                   # 客户端的所在IP地址，有时候可能是域名
        'SCRIPT_NAME': '',                   # 客户端本次请求时，服务端执行的程序所在路径
        'SERVER_PROTOCOL': 'HTTP/1.1',       # 服务端运行的协议
        'SERVER_SOFTWARE': 'WSGIServer/0.2', # 服务端运行web服务器的软件打印信息
        'REQUEST_METHOD': 'POST',            # 客户端本次请求时的http请求方法
        'PATH_INFO': '/home/index3/',        # 客户端本次请求时的url路径
        'QUERY_STRING': '',                  # 客户端本次请求时的查询字符串
        'REMOTE_ADDR': '127.0.0.1',          # 客户端的所在IP地址
        'CONTENT_TYPE': 'application/json',  # 客户端本次请求时的数据MIME格式
        'HTTP_USER_AGENT': 'PostmanRuntime/7.26.10', # 客户端本次请求时，所使用的网络代理软件提示信息
        'HTTP_ACCEPT': '*/*',          # 客户端期望服务端返回的数据MIME格式格式
        'HTTP_HOST': '127.0.0.1:8000', # 客户端本次请求时，所使用服务端地址
        'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', # 客户端期望服务端返回的数据的压缩格式
        'HTTP_CONNECTION': 'keep-alive', # 客户端支持的服务端协议的链接类型,keep-alive 表示客户端支持http的长连接
    }
    """
    print(request.headers)  # 获取HTTP请求头
    """
    {
        'Content-Length': '601',     // 客户端本次请求的内容大小
        'Content-Type': 'multipart/form-data;',   # 客户端本次请求的内容MIME类型
        'User-Agent': 'PostmanRuntime/7.26.10',   # 客户端本次请求的代理软件打印信息
        'Accept': '*/*',   
        'Host': '127.0.0.1:8000',    # 客户端本次请求的服务端地址
        'Accept-Encoding': 'gzip, deflate, br', 
        'Connection': 'keep-alive',
        # 以下就是自定义请求头了
        'Company': 'baidu', 
        'Num': '1000', 
    }
    """
    print("Content-Type=", request.META.get("CONTENT_TYPE"))
    print("自定义请求头，Num=", request.META.get("HTTP_NUM"))
    print("自定义请求头，Company=", request.META.get("HTTP_COMPANY"))

    print("Content-Type=", request.headers.get("Content-Type"))
    print("自定义请求头，Num=", request.headers.get("Num"))
    print("自定义请求头，Company=", request.headers.get("Company"))

    import os 
    print("自定义请求头os =", os.path.dirname(__file__))
    data = os.path.join(os.path.dirname(__file__),"data")
    print("自定义请求头data =", data)

    return HttpResponse("接收请求体")


# SERVER_NAME，  服务端系统名称
# SERVER_PORT，   服务端的运行端口
# REMOTE_ADDR，客户端的所在IP地址
# SERVER_SOFTWARE，服务端运行web服务器的软件打印信息
# PATH_INFO，客户端本次请求时的url路径

# 接收上传文件 python 请求端
"""
import requests

# 目标URL
url = 'http://127.0.0.1:8000/home/index4'

# 要上传的文件路径
file_path = r'D:\Project\PyProject\ScriptGather\lisi\p.2.jpg'

# 创建一个文件对象
with open(file_path, 'rb') as f:
    # 发送POST请求，包含文件数据
    response = requests.post(url, files={'avatar': f})

# 打印响应内容（这里假设服务器返回的是一个MultiValueDict对象的内容）
# 实际上，服务器返回的内容可能是一个JSON、HTML或其他格式，需要根据实际情况处理
# 这里只是为了模拟你提到的打印效果
print(f"<MultiValueDict: {{'avatar': [{response.text.strip()}]}}>")
# 注意：上面的print语句只是为了模拟输出格式，实际使用时应该根据响应内容调整

# 更实际的处理方式可能是检查响应状态码和解析响应内容
if response.status_code == 200:
    # 如果服务器返回的是JSON数据，可以这样解析
    # data = response.json()
    # print(data)

    # 或者直接打印响应文本（适用于HTML或其他文本格式）
    print(response.text)
else:
    print(f"请求失败，状态码：{response.status_code}")

"""

# 接收上传文件
def index4(request):
    """接收上传文件"""
    # print(request.FILES)
    """
    POST  http://127.0.0.1:8000/home/index4
    打印效果：
    <MultiValueDict: {'avatar': [<InMemoryUploadedFile: 1.jpg (image/jpeg)>]}>
    """

    # print(request.FILES.get("avatar"))      # 获取本次客户端上传的指定name值对应的一个文件上传处理对象
    # print(request.FILES.getlist("avatar"))  # 获取本次客户端上传的指定name值对应的多个文件上传处理对象

    """
    django在解析http协议的时候，针对上传文件，会自动实例化一个内存保存文件的文件上传处理对象InMemoryUploadedFile
    from django.core.files.uploadedfile import InMemoryUploadedFile
    """
    # read() 从文件上传处理对象读取文件的内容(bytes格式内容)
    import os
    # # 处理一个上传文件[不仅是图片，任何内容都可以这样处理]
    # file = request.FILES.get('avatar')
    # with open(f"{os.path.dirname(__file__)}/{file.name}", "wb") as f:
    #     f.write(file.read())

    # 处理多个一次性上传文件
    for file in request.FILES.getlist("avatar"):
        # with open(f"{os.path.dirname(__file__)}/{file.name}", "wb") as f:
        #     f.write(file.read())
        with open(f"{os.path.join(os.path.dirname(__file__),"data")}/{file.name}", "wb") as f:
            f.write(file.read())

    return HttpResponse("接收客户端的上传文件")



# 返回HTML数据
def index5(request):
    """响应对象"""
    """
    return HttpResponse(content="正文内容",content_type="内容格式",status="http响应状态码")
    content      响应内容
    content_type 内容格式,默认是 text/html
    status       响应状态码,默认是 200
    headers      响应头，字典格式
    """

    """返回html内容"""
    return HttpResponse("<h1>你好，django</h1>")


# 返回Json数据
def index6(request):
    """响应对象：响应json数据"""
    # 返回字典数据作为json给客户端
    """
    import json
    data = {"name":"xiaoming", "age":16, "sex": True}
    return HttpResponse(json.dumps(data), content_type="application/json;charset=utf-8")
    """

    # 原生返回json数据，太麻烦了
    # 因此django提供了一个HttpResponse的子类JsonResponse，转换提供给我们返回json数据的
    # from django.http.response import JsonResponse
    # data = {"name": "xiaoming", "age": 16, "sex": True}
    # return JsonResponse(data)

    # JsonResponse返回的数据如果不是字典，则必须要加上safe参数声明，并且值为False
    # 返回列表数据给客户端
    from django.http.response import JsonResponse
    data = [
        {"id":1, "name": "小明", "age": 16},
        {"id":3, "name": "小火", "age": 15},
    ]

    return JsonResponse(data, safe=False)
    # return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False})  # 不推荐使用



# 返回图片格式信息

def index7(request):
    """返回图片格式"""
    import os
    with open(f"{os.path.dirname(__file__)}/data/d12.jpg", "rb") as f:
        content = f.read()
        return HttpResponse(content, content_type="image/jpeg")

# 提供下载压缩包

def index8(request):
    """返回压缩包格式"""
    import os
    with open(f"{os.path.dirname(__file__)}/data/d12.zip", "rb") as f:
        content = f.read()
        return HttpResponse(content, content_type="application/zip")


# 自定义响应头
def index9(request):
    """返回数据的过程中设置响应头"""
    response = HttpResponse("ok")
    # 自定义响应头[值和属性都不能是多字节]
    response["company"] = "baidu"
    return response

# 站外跳转
def index10(request):
    """跳转到站外"""
    # 1. 基于django提供的Response对象也可以进行页面跳转
    # from django.http.response import HttpResponse
    # response = HttpResponse(status=301)
    # response["Location"] = "https://www.tmall.com"
    # return response

    # # 2. 基于django提供的Response对象的原生写法[HttpResponseRedirect与HttpResponsePermanentRedirect都是HttpResponse的子类]
    # from django.http.response import HttpResponseRedirect    # 临时重定向
    # # from django.http.response import HttpResponsePermanentRedirect  # 永久重定向
    # return HttpResponseRedirect("https://www.qq.com")

    # 2. 基于django提供快捷函数（简写函数, shortcuts）来完成[常用]
    from django.shortcuts import redirect
    return redirect("http://www.baidu.com")

# 站内跳转
# 在站内跳转时,如果使用django.urls.reverse函数进行路由反转解析（可以根据路由的别名反向生成路由的URL地址）,
# 则必须在总路由文件和子路由文件中，对路由的前缀和子路由后缀进行别名绑定，步骤如下：



# 跳转到站内
def index11(request):
    """跳转到站内"""
    from django.shortcuts import redirect  # 根据指定的url地址，进行页面跳转

    # # 直接基于redirect跳转
    # return redirect("/home/index12")

    # # 基于reverse+redirect对路由别名进行反向解析进行跳转
    from django.urls import reverse  # 根据路由别名，反向解析生成url地址
    url = reverse("home:in12")
    print(url)
    return redirect(url)


def index12(request):
    return HttpResponse("ok, index12")


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
 

# 使用django提供的视图和路由接收postman发送到服务端的json数据
@csrf_exempt  # 如果您不打算使用 CSRF 保护，可以使用此装饰器（注意：在生产环境中通常不推荐这样做）
def index13(request):
    print("home index13 : ",request.GET) # <QueryDict: {'name': ['xiaoming'], 'pwd': ['123']}>
    if request.method == 'GET':
        # 处理 GET 请求
        query_params = request.GET
        print("home index13 GET request: ", query_params)
        return HttpResponse("ok, index13 (GET request)")
    elif request.method == 'POST':
        # 处理 POST 请求
        # 注意：如果客户端发送的是 JSON 数据，Django 默认不会将其解析到 request.POST 中
        # 您需要从 request.body 中读取原始数据并解析它
        import json
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            print("home index13 POST request JSON data: ", json_data)
            # 这里可以返回 JSON 响应
            return JsonResponse({"status": "ok", "received_data": json_data})
        except json.JSONDecodeError:
            # 如果解析 JSON 失败，可以返回一个错误响应
            return HttpResponse("Invalid JSON data", status=400)
    else:
        # 处理其他 HTTP 方法（如 PUT, DELETE 等），这里简单返回 405 方法不允许
        return HttpResponse("Method Not Allowed", status=405)



# 操作到   会话控制技术

