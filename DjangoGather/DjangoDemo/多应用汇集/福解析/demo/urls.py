




from django.urls import path

from . import views


from django.urls import re_path

# 路由功能

  

urlpatterns = [

 
    path('', views.路由功能, name='路由功能'), # ip/路由功能/
    path(r'单个匹配/', views.单个匹配),

   
    re_path(r'正则匹配后续所有/.*$', views.正则匹配后续所有),
    re_path(r'^.*$', views.all),

]