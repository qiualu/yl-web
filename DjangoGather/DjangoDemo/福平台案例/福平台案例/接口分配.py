
from ninja import NinjaAPI, Router, Field, Schema  # 注意这里使用 Schema 而不是 ModelSchema
from 系统接口.router路由 import 系统接口路由

# from 公共文件.fu_auth import GlobalAuth
# from 公共文件.fu_ninja import FuNinjaAPI 

接口分配 = NinjaAPI()
# 接口分配 = FuNinjaAPI(auth=GlobalAuth())

# "GET /案例模板/ninjaAPI案例/相关多个的路由/helloXX HTTP/1.1"
@接口分配.get("/")
def hello(request):
    return {"message": "HelloXX, 接口分配!"}




# 统一处理server异常
@接口分配.exception_handler(Exception)
def a(request, exc):

    if hasattr(exc, 'errno'):
        return 接口分配.create_response(request, data=[], msg=str(exc), code=exc.errno)
    else:
        return 接口分配.create_response(request, data=[], msg=str(exc), code=500)



接口分配.add_router('/system/', 系统接口路由)
