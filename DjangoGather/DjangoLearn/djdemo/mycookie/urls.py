# mycookie子应用的子路由文件
from django.urls import path



from . import views

app_name = "mycookie"


# http://127.0.0.1:8000/cookie/set

urlpatterns = [

    path("set", views.set_cookie),
    path("get", views.get_cookie),
    path("del", views.del_cookie),

]