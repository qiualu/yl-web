from django.urls import path
from . import views

urlpatterns = [
    # 硬件按钮触发计数的接口（POST请求）
    path('触发/', views.触发计数, name='触发计数'),
    # 获取统计数据的接口（GET请求）
    path('统计/', views.获取统计数据, name='获取统计数据'),


    # 匹配所有其他未定义的路径
    path('<path:path>', views.无定义页面, name='无定义页面'),
    # 处理根路径的情况
    path('', views.无定义页面, name='根路径无定义页面'),

     
 
]



"""

 
http://127.0.0.1:8000/全运会计数/触发/?设备编号=1&当前计数=1
http://127.0.0.1:8000/全运会计数/统计/

http://yulu512.picp.io/全运会计数/统计/


"""







