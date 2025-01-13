from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="问题的文本内容")  # 问题的文本内容
    pub_date = models.DateTimeField(verbose_name="发布日期和时间")  # 问题发布的日期和时间
 
    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'
 
    def __str__(self):
        return self.question_text
 
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
 
 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="关联问题")  # 与Question模型相关联的外键
    choice_text = models.CharField(max_length=200, verbose_name="选项的文本内容")  # 选项的文本内容
    votes = models.IntegerField(default=0, verbose_name="票数")  # 这个选项的票数
 
    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项'
 
    def __str__(self):
        return self.choice_text


# # 定义一个问题模型
# class Question(models.Model):
#     """
#     代表一个调查问题。

#     Attributes:
#         question_text (CharField): 问题的文本，最大长度200个字符。
#         pub_date (DateTimeField): 问题发布的日期和时间，在数据库中以"date published"为列名存储。
#     """
#     question_text = models.CharField(max_length=200)  # 问题的文本内容
#     pub_date = models.DateTimeField("date published")  # 问题发布的日期和时间
#     # 向模型中添加__str__()方法很重要，这不仅是为了您在处理交互式提示时方便自己，还因为对象的表示会在整个 Django 自动生成的管理中使用。
#     def __str__(self):
#         return self.question_text

#     # 我们还向该模型添加一个自定义方法：
#     # def was_published_recently(self):
#     #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now





# # 定义一个选项模型，与问题相关联
# class Choice(models.Model):
#     """
#     代表一个针对问题的选项。

#     Attributes:
#         question (ForeignKey): 与Question模型相关联的外键，表示这个选项属于哪个问题。
#         choice_text (CharField): 选项的文本，最大长度200个字符。
#         votes (IntegerField): 这个选项获得的票数，默认为0。
#     """
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 与Question模型相关联的外键
#     choice_text = models.CharField(max_length=200)  # 选项的文本内容
#     votes = models.IntegerField(default=0)  # 这个选项的票数

#     # 向模型中添加__str__()方法很重要，这不仅是为了您在处理交互式提示时方便自己，还因为对象的表示会在整个 Django 自动生成的管理中使用。
#     def __str__(self):
#         return self.choice_text


