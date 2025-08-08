"""
URL configuration for 服务器后端 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


# from 福平台.公共类.福平台api import 福平台api
# from 案例模板.路由案例.ninjaAPI案例.Helloworld import HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls), 


    # 路由跳转 文件
    path('案例模板/', include('案例模板.公共类.案例模板路由分配')), 
    # path('api/', 福平台api.urls),
    # path('HelloWorld/', HelloWorld.urls),

 
    path('', include('案例模板.公共类.案例模板路由分配')), 

]
 

 
