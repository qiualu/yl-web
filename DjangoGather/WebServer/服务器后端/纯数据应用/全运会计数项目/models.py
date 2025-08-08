# 纯数据应用/全运会计数项目/models.py

from django.db import models
from django.utils import timezone

class 计数记录(models.Model):
    触发时间 = models.DateTimeField(default=timezone.now, verbose_name="触发时间")

    class Meta:
        verbose_name = "计数记录"
        verbose_name_plural = "计数记录"
        ordering = ['-触发时间']
        app_label = '全运会计数项目'  # 明确指定所属应用（与settings.py中注册的名称一致）

    def __str__(self):
        return self.触发时间.strftime("%Y-%m-%d %H:%M:%S")