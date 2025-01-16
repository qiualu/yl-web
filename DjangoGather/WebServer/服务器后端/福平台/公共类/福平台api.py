


from ninja import NinjaAPI

福平台api = NinjaAPI(version='2.0.0')

# ** 演示 **
# api/hello
@福平台api.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@福平台api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}



from 福平台.demo.router import demo_router
from 福平台.system.router import system_router

 
# 统一处理server异常
@福平台api.exception_handler(Exception)
def a(request, exc):
    # print(" 福平台 : 异常情况 ",request,exc)
    if hasattr(exc, 'errno'):
        return 福平台api.create_response(request, data=[], msg=str(exc), code=exc.errno)
    else:
        return 福平台api.create_response(request, data=[], msg=str(exc), code=500)



福平台api.add_router('/system/', system_router)
福平台api.add_router('/demo/', demo_router)



# C:\Users\yl\Desktop\DockerProject\yl-web\DjangoGather\WebServer\服务器后端\福平台\demo\router.py


# /api/system/login HTTP/1.1" 403 2566
# router.py



