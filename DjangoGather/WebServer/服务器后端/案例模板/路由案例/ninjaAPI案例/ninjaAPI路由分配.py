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
 


 