from django.urls import path,include

from django.urls import re_path

 
# from 案例模板.路由案例.ninjaAPI案例.Helloworld import HelloWorld
from .Helloworld import HelloWorld
from .相关多个的路由 import 相关多个的路由
from .相关多个的路由多层结构 import 相关多个的路由多层结构

# 跳转进来
# /案例模板/ninjaAPI案例/




urlpatterns = [

  
    # 直接跳转路由函数 
    path('HelloWorld/', HelloWorld.urls),
    path('相关多个的路由/', 相关多个的路由.urls),
    path('相关多个的路由多层结构/', 相关多个的路由多层结构.urls),
    
    path('', HelloWorld.urls),

]

 



# # 定义一个子路由
# item_router = Router()
# # "GET /案例模板/ninjaAPI案例/相关多个的路由/items/123 
# @item_router.get("/{item_id}")
# def get_item(request, item_id: int):
#     return {"item_id": item_id, "name": "Sample Item"}

# @item_router.post("/")
# def create_item(request, item: Item):
#     # 假设我们保存了项目数据
#     # print(" item_router.post: ", item) item_router.post:  id=42 name='YL Item Name'
#     item.id += 100 
#     return item


