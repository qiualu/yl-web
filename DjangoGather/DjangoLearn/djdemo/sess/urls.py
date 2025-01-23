from django.urls import path,re_path

from . import views


# http://127.0.0.1:8000/sess/session/set/

urlpatterns = [
    # path("路由url","视图函数","路由别名"),

    path("session/set/", views.set_session),
    path("session/get/", views.get_session),
    path("session/del/", views.del_session),
]


 