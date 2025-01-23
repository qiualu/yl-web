from django.shortcuts import render

# Create your views here.



from django.http.response import HttpResponse


def set_cookie(request):
    """设置/保存/更新Cookie"""
    response = HttpResponse()
    # 生成cookie
    """
    参数列表：
        key,             # 键/变量
        value='',        # 值/内容
        max_age=None,    # 设置cookie的有效时间，单位: 秒
        expires=None,    # 设置cookie的过期时间戳[时间戳表示从1970-01-01 00:00:00至今的总秒数]
                         # datetime.now().timestamp() 获取时间戳
                         # int( time.time() * 1000 )  获取毫秒时间戳
                         # datetime.now().timestamp() 获取毫秒时间戳

        path=None,       # 当前cookie是否只能在指定公共路径下使用，None表示在同一个域名下，任意路径都可以使用
        domain=None,     # 当前cookie是否只能在指定同一段域名下使用，None表示在当前服务器所在域名下使用
        secure=False,    # 当前cookie是否只能在https协议下使用，False表示在http协议下也能使用    
        httponly=False,  # 当前cookie是否只能在http协议下使用,False表示在其他协议下也可以使用
    """
    response.set_cookie("uname", "xiaoming", max_age=5)
    response.set_cookie("uid", 100, max_age=180)
    # 设置cookie信息，可以不设置过期时间，默认cookie有效期的就是浏览器关闭时自动删除
    # 会话结束时浏览器会自动删除没有设置有效的cookie，而设置了有效期的cookie则只会在到期时才删除
    response.set_cookie("is_login", True, )
    return response

def get_cookie(request):
    """通过request.COOKIES可以获取客户端发送过来的cookie"""
    print(request.COOKIES)  # 获取本次客户端发送过来的所有cookie
    print("uid=", request.COOKIES.get("uid"))  # 获取指定名称cookie
    print("uname=", request.COOKIES.get("uname"))  # 不存在的或过期的cookie不会被浏览器通过http请求头携带到服务端
    # cookie的修改，与添加一致，cookie重复的变量名会覆盖
    response = HttpResponse("OK")
    response.set_cookie("uname", "xiaohong", max_age=15)
    return response


def del_cookie(request):
    """直接删除cookie在服务端是做不到的，因为cookie保存在客户端，所以我们需要通知客户端自己去删除"""
    # 告诉浏览器，cookie过期了
    response = HttpResponse("告诉客户端，删除cookie")
    response.set_cookie("uid", "", max_age=0)  # 设置有效期为0秒，当浏览器接受响应内容时，0秒早就到了，所以会自动删除
    return response







