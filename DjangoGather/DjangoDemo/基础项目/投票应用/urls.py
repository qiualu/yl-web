from django.urls import path

from . import views


from django.urls import re_path

urlpatterns = [
    # path('', views.index, name='index'),
    re_path(r'^.*$', views.index, name='index'),
]





