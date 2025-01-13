from django.urls import path

from . import views

from django.urls import re_path

urlpatterns = [
    path('', views.表单视图, name='表单视图'),
    path('一个简单的表单/<int:question_id>', views.一个简单的表单, name='一个简单的表单'),
    path('查询单个数据/<int:question_id>', views.查询单个数据, name='查询单个数据'),


    re_path(r'^.*$', views.表单视图),
]

