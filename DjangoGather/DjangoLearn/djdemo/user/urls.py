from django.urls import path,re_path

from . import views


# 自定义转换器
#  在当前子应用下新建converters.py下编写的
from . import converters


# http://127.0.0.1:8000/user/session/set/

urlpatterns = [
    # path("路由url","视图函数","路由别名"),

    # path("url路径", 视图函数/视图类, name="路径别名"),
    path("index/", views.index),

    # 绑定的路由的执行上效率，使用path比re_path的效率高很多，
    # 因为path默认情况下仅仅是通过字符串比较，而re_path是使用正则匹配。

    # re_path(r"^info/(?P<参数名1>正则)/(?P<参数名2>正则).....$", views.info1),
    # http://127.0.0.1:8000/user/info/123/01
    re_path(r"^info/(?P<id>\d+)/(?P<page>0[1-9]+)$", views.info1),

    # http://127.0.0.1:8000/user/mobile/13123445678
    re_path(r"^mobile/(?P<mobile>1[3-9]\d{9})$", views.info2),


    # 路由转换器
    # 也可以叫路由验证器，有2个作用：

    # 把路由参数进行类型转换
    # 可以起到验证路由匹配的作用（让字符串路由path发挥正则路由re_path的作用）

    # 内置转换器
    # 文档：https://docs.djangoproject.com/zh-hans/4.2/topics/http/urls/#path-converters
    # 内置转换器源码：django.urls.converters，别名设置：DEFAULT_CONVERTERS
    # 常见的内置路由转换器：

    
    # str - 匹配除了 '/' 之外的非空字符串。如果表达式内不包含转换器，则会默认匹配字符串。
    # int - 匹配 0 或任何正整数。返回一个 int 。
    # slug - 匹配任意由 ASCII 字母或数字以及连字符和下划线组成的短标签。比如，building-your-1st-django_site 。
    # uuid - 匹配一个格式化的 UUID 。为了防止多个 URL 映射到同一个页面，必须包含破折号并且字符都为小写。比如，075194d3-6885-417e-a8a8-6c931e272f00。返回一个 UUID 实例。
    # path - 匹配非空字段，包括路径分隔符 '/' 。它允许你匹配完整的 URL 路径而不是像 str 那样匹配 URL 的一部分。


    # path("img/", views.img),

    path("rev/<int:num>/", views.inbuild_reverse),
    path("rev/<str:content>/", views.inbuild_reverse2),
    path("rev/<uuid:ustr>/", views.inbuild_reverse3),  # str会包含uuid的模式，str和uuid同时使用时，str必须写在后面


    # 使用自定义路由转换器 http://127.0.0.1:8000/user/sms/15123445678
    path("sms/<mob:mobile>", views.info5),

]


 