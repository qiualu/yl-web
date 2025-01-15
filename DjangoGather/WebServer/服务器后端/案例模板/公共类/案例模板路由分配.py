from django.urls import path,include

from django.urls import re_path


from 案例模板.路由案例.ninjaAPI案例.Helloworld import HelloWorld

# from 案例模板.路由案例.ninjaAPI案例


# 路由跳转进来
# /案例模板
urlpatterns = [

    # path('system/', include('福解析.system.urls')),
    # path('demo/', include('福解析.demo.urls')),
    # path('generator/', include('福解析.generator.urls')),
    
 
    # 直接跳转路由函数 
    path('ninjaAPI案例Hello/', HelloWorld.urls),
    path('ninjaAPI案例/', include('案例模板.路由案例.ninjaAPI案例.ninjaAPI路由分配')),

    path('', include('案例模板.路由案例.ninjaAPI案例.ninjaAPI路由分配')),

]
 
 












