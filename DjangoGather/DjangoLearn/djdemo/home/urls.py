from django.urls import path
from home import views


# 使用路由反向解析，reverse时必须在当前路由文件中设置app_name为当前子应用的包名
app_name = "home"

urlpatterns = [
    # path('路由尾缀', 视图函数导包路径),
    path('index', views.index),
    path('index/', views.index),  # 获取请求体数据
    path('index2', views.index2), # 获取请求体数据
    path('index3', views.index3), # 获取请求头数据
    path('index4', views.index4), # 获取上传文件
    path('index5', views.index5), # 返回HTML数据
    path('index6', views.index6), # 返回Json数据
    path('index7', views.index7), # 返回图片格式信息
    path('index8', views.index8), # 提供下载压缩包
    path('index9', views.index9), # 自定义响应头
    path('index10', views.index10), # 站外跳转
    path('index11', views.index11, name="in11"), # 跳转到站内
    path('index12', views.index12, name="in12"), # 被跳转
    
    path('index13', views.index13), # postman发送到服务端的json数据

    path('login/', views.login),


]