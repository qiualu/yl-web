"""
URL configuration for 基础项目 project.

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
# 初始代码
# from django.contrib import admin
# from django.urls import path
# 下面添加 include
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path("admin/", admin.site.urls),
    path('投票应用/', include('投票应用.urls')),
    path('路由功能/', include('路由功能.urls')),
    path('模型功能/', include('模型功能.urls')),
    path('视图功能/', include('视图功能.urls')),
    path('表单视图/', include('表单视图.urls')),



    path('', include('路由功能.urls')),
]

"""
# E:\ProgramFiles\Tool\Git/.ssh/id_rsa


"""
