from django.urls import path,include

from django.urls import re_path


 
 

# 路由跳转进来
# /案例模板
urlpatterns = [

 
    # ninjaAPI路由分配 
 
    # 直接跳转路由函数   生成 python manage.py makemigrations 需要注释掉不然报错
    # path('ninjaAPI案例/', include('案例模板.路由案例.ninjaAPI案例.ninjaAPI路由分配')),

    #  -- Model --

    path('福案例用户/', include('案例模板.模型案例.福案例用户.urls')),


]
 
 












