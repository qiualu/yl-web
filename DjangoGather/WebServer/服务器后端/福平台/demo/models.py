from django.db import models

# Create your models here.

from 福平台.公共类.公共模型 import CoreModel

# 关于CharField：

# 它总是存储字符串（文本）。
# max_length参数定义了字符串在数据库中的最大长度。
 
# 假设CoreModel是一个已经定义好的模型基类，它可能包含了一些通用字段或方法
class Demo(CoreModel):
    # 定义一个CharField字段，用于存储项目名称
    # null=False表示该字段在数据库中不允许为空
    # max_length=64表示该字段在数据库中的最大字符长度为64
    # verbose_name用于在Django admin后台显示更友好的字段名
    # help_text提供该字段的额外说明信息
    name = models.CharField(null=False, max_length=64, verbose_name="项目名称", help_text="项目名称")
    
    # 定义一个CharField字段，用于存储项目编码
    # max_length=32表示该字段在数据库中的最大字符长度为32
    # verbose_name和help_text同上
    code = models.CharField(max_length=32, verbose_name="项目编码", help_text="项目编码")
    
    # 定义一个CharField字段，用于存储项目状态
    # max_length=64表示该字段在数据库中的最大字符长度为64
    # verbose_name和help_text同上
    status = models.CharField(max_length=64, verbose_name="项目状态", help_text="项目状态")

    # Meta类用于定义一些模型级别的元数据
    class Meta:
        # db_table指定了数据库中的表名
        db_table = "Demo"
        
        # verbose_name和verbose_name_plural用于指定在Django admin后台显示的模型名和复数形式
        # 这里都设置为'项目演示'，意味着无论是单数还是复数形式，显示的都是相同的名称
        verbose_name = '项目演示'
        verbose_name_plural = verbose_name
        
        # ordering指定了对象的默认排序方式
        # 这里使用('-create_datetime',)表示按照create_datetime字段的降序排列
        # 注意：create_datetime字段没有在Demo类中定义，可能是在CoreModel中定义的
        ordering = ('-create_datetime',)
