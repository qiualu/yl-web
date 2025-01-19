

import uuid

from django.apps import apps
from django.db import models

from 福平台案例 import settings

# from django.contrib.auth import get_user_model

# User = get_user_model()

class CoreModel(models.Model):
    """
    核心标准抽象模型模型,可直接继承使用
    增加审计字段, 覆盖字段时, 字段名称请勿修改, 必须统一审计字段名称
    """
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    remark = models.CharField(max_length=255, verbose_name="描述", null=True, blank=True, help_text="描述")
    
    
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    
    # creator = models.ForeignKey(User, related_query_name='creator_query', null=True,
    #                             verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    
    
    modifier = models.CharField(max_length=255, null=True, blank=True, help_text="修改人", verbose_name="修改人")
    belong_dept = models.IntegerField(help_text="数据归属部门", null=True, blank=True, verbose_name="数据归属部门")
    update_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="修改时间", verbose_name="修改时间")
    create_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="创建时间",
                                           verbose_name="创建时间")
    sort = models.IntegerField(default=1, null=True, blank=True, verbose_name="显示排序", help_text="显示排序")

    class Meta:
        abstract = True
        verbose_name = '核心公共模型'
        verbose_name_plural = verbose_name

class 核心模型(models.Model):
    """
    核心标准抽象模型模型,可直接继承使用
    增加审计字段, 覆盖字段时, 字段名称请勿修改, 必须统一审计字段名称
    """
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    描述 = models.CharField(max_length=255, verbose_name="描述", null=True, blank=True, help_text="描述")
    
    创建人 = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    
    # creator = models.ForeignKey(User, related_query_name='creator_query', null=True,
    #                             verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    
    
    修改人 = models.CharField(max_length=255, null=True, blank=True, help_text="修改人", verbose_name="修改人")
    数据归属部门 = models.IntegerField(help_text="数据归属部门", null=True, blank=True, verbose_name="数据归属部门")
    修改时间 = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="修改时间", verbose_name="修改时间")
    创建时间 = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="创建时间",
                                           verbose_name="创建时间")
    显示排序 = models.IntegerField(default=1, null=True, blank=True, verbose_name="显示排序", help_text="显示排序")

    class Meta:
        abstract = True
        verbose_name = '核心模型'
        verbose_name_plural = verbose_name











