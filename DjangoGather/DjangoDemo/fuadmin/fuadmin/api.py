
from ninja import NinjaAPI, Router, Field, Schema  # 注意这里使用 Schema 而不是 ModelSchema
 
from system.router import system_router
from utils.fu_auth import GlobalAuth
from utils.fu_ninja import FuNinjaAPI
# from generator.router import generator_router


api = FuNinjaAPI(auth=GlobalAuth())
# api = NinjaAPI()

# "GET /案例模板/ninjaAPI案例/相关多个的路由/helloXX HTTP/1.1"
@api.get("/")
def hello(request):
    return {"message": "HelloXX, 接口分配!"}

# 统一处理server异常
@api.exception_handler(Exception)
def a(request, exc):

    if hasattr(exc, 'errno'):
        return api.create_response(request, data=[], msg=str(exc), code=exc.errno)
    else:
        return api.create_response(request, data=[], msg=str(exc), code=500)


api.add_router('/system/', system_router)  
