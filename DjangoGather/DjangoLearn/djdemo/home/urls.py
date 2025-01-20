from django.urls import path
from home import views


urlpatterns = [
    # path('路由尾缀', 视图函数导包路径),
    path('index', views.index),
]