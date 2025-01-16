from django.db import models

from 福平台.公共类.公共模型 import CoreModel


class TemplateTest(CoreModel):
        
    input_text_area_2 = models.TextField(null=True, blank=True, verbose_name='文本域', help_text='文本域')    
    input_1 = models.CharField(null=True, blank=True, max_length=255, verbose_name='输入框', help_text='输入框')

    class Meta:
        db_table = 'generator_template_test'
        verbose_name = '测试1'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class Test(CoreModel):
        
    icon = models.CharField(null=True, blank=True, max_length=255, verbose_name='图标', help_text='图标')    
    sequence = models.DecimalField(null=True, blank=True, max_digits = 13, decimal_places = 4, verbose_name='排序', help_text='排序')    
    code = models.CharField(null=True, blank=True, max_length=255, verbose_name='代码', help_text='代码')    
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name='名称', help_text='名称')

    class Meta:
        db_table = 'generator_test'
        verbose_name = '模板测试'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class TestDemo(CoreModel):
        
    des = models.TextField(null=True, blank=True, verbose_name='描述', help_text='描述')    
    code = models.DecimalField(null=True, blank=True, max_digits = 13, decimal_places = 4, verbose_name='编码', help_text='编码')    
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name='名称', help_text='名称')

    class Meta:
        db_table = 'generator_test_demo'
        verbose_name = '测试案例'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    

