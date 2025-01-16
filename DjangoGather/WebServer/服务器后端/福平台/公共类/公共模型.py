

from django.apps import apps
from django.db import models

# from 服务器后端 import settings
from 福平台.公共类 import 模块参数配置 as settings

# from 福平台.system.models import Users

from django.contrib.auth import get_user_model


class CoreModel(models.Model):
    """
    核心标准抽象模型, 可直接继承使用.
    增加审计字段, 覆盖字段时, 字段名称请勿修改, 必须统一审计字段名称.
    """
    
    # 主键，使用BigAutoField以适应大数据库表
    # 存储的是一个自增的数字ID
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    
    # 描述字段，用于存储文本描述
    # 存储的是文字（字符串）
    remark = models.CharField(max_length=255, verbose_name="描述", null=True, blank=True, help_text="描述")
    
    # 创建人字段（已被注释掉）
    # 如果取消注释，这将是一个外键，指向Django的用户模型（AUTH_USER_MODEL）
    # 存储的是一个数据库中的引用（实际上是存储用户ID，但Django会处理这种关系）

    # creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
    #                             verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    User = get_user_model() 
    # Your fields here
    creator = models.ForeignKey(User, related_query_name='creator_query', null=True,
                                verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)

    # 修改人字段，用于存储最后修改者的标识（这里假设是一个文本字段，可能是用户名或其他标识符）
    # 注意：通常，这里也会使用ForeignKey来指向用户模型，但这里为了简化或特殊需求使用了CharField
    # 存储的是文字（字符串）
    modifier = models.CharField(max_length=255, null=True, blank=True, help_text="修改人", verbose_name="修改人")
    
    # 数据归属部门字段，用于存储部门ID（假设是整数）
    # 存储的是数字（整数）
    belong_dept = models.IntegerField(help_text="数据归属部门", null=True, blank=True, verbose_name="数据归属部门")
    
    # 修改时间字段，自动记录每次模型保存时的时间
    # 存储的是日期和时间
    update_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="修改时间", verbose_name="修改时间")
    
    # 创建时间字段，自动记录模型首次创建时的时间
    # 存储的是日期和时间
    create_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="创建时间",
                                           verbose_name="创建时间")
    
    # 显示排序字段，用于控制数据在前端显示的顺序
    # 存储的是数字（整数）
    sort = models.IntegerField(default=1, null=True, blank=True, verbose_name="显示排序", help_text="显示排序")
 
    class Meta:
        # 声明这是一个抽象模型，不能直接创建数据库表
        abstract = True
        # 在Django admin后台显示的模型名（单数和复数形式相同）
        verbose_name = '核心模型'
        verbose_name_plural = verbose_name

 

def get_all_models_objects(model_name=None):
    """
    获取所有 models 对象
    :return: {}
    """
    settings.ALL_MODELS_OBJECTS = {}
    if not settings.ALL_MODELS_OBJECTS:
        all_models = apps.get_models()
        for item in list(all_models):
            table = {
                "tableName": item._meta.verbose_name,
                "table": item.__name__,
                "tableFields": []
            }
            for field in item._meta.fields:
                fields = {
                    "title": field.verbose_name,
                    "field": field.name
                }
                table['tableFields'].append(fields)
            settings.ALL_MODELS_OBJECTS.setdefault(item.__name__, {"table": table, "object": item})
    if model_name:
        return settings.ALL_MODELS_OBJECTS[model_name] or {}
    return settings.ALL_MODELS_OBJECTS or {}





