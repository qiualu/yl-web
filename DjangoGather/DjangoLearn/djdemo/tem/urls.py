"""tem子应用路由"""
from django.urls import path, re_path
from . import views

# http://127.0.0.1:8000/tem/index
urlpatterns = [

    path("index1", views.index1), 
    path("index2", views.index2),
    path("index3", views.index3),

    path("index4", views.index4),
    path("index5", views.index5),

    path("index6", views.index6),
]



