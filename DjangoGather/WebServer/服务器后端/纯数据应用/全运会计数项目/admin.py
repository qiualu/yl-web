from django.contrib import admin

# Register your models here.
from .models import 计数记录

@admin.register(计数记录)
class 计数记录管理(admin.ModelAdmin):
    list_display = ('id', '触发时间')  # 显示ID和触发时间
    # list_filter = ('触发时间',)  # 直接使用字段名，修复过滤条件报错
    # date_hierarchy = '触发时间'  # 增加日期层级导航，便于按时间筛选
    