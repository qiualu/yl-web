from django.test import TestCase

# Create your tests here.

import datetime

from django.test import TestCase
from django.utils import timezone

from 投票应用.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        # was_published_recently() 方法用来判断问题是否是最近发布的。如果 pub_date 在当前时间的前一天内，则返回 True，否则返回 False。
        # 使用 self.assertIs() 方法断言 future_question.was_published_recently() 返回的结果是否为 False。这是为了确保 was_published_recently() 方法在处理未来日期时能够正确返回预期的值。

    # 更全面的测试¶
    # 既然我们在这里，我们可以进一步确定was_published_recently()
    # 方法；事实上，如果在修复一个错误时引入了另一个错误，那将是相当尴尬的。
    #
    # 向同一个类中添加两个测试方法，以更全面地测试该方法的行为：

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

"""

D:\Project\PyProject\DjangoGather\DjangoDemo\基础项目
工程项目下不要有 __init__.py
否则会判断主工程为一个库导致目录不一样
init_py = os.path.join(top_level, "__init__.py")


Django 测试客户端
Django 提供了一个测试Client来模拟用户在视图级别与代码交互。我们可以在 中使用它tests.py ，甚至可以在 中使用它shell。

我们将从 重新开始shell，在这里我们需要做一些在 中不需要的事情tests.py。首先是在 中设置测试环境shell：
python manage.py shell

>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()

setup_test_environment()安装模板渲染器，这将允许我们检查响应中的一些其他属性，否则这些属性 response.context将不可用。
请注意，此方法不会设置测试数据库，因此以下内容将针对现有数据库运行，并且输出可能会略有不同，具体取决于您已创建的问题。
如果您的 TIME_ZONE输入settings.py不正确，您可能会得到意外的结果。如果您不记得之前设置过它，请在继续之前检查它。


>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()

准备好之后，我们可以要求客户为我们做一些工作：

>>> # get a response from '/'
>>> response = client.get("/")
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse

>>> response = client.get(reverse("polls:index"))
>>> response = client.get(reverse("路由功能"))  

>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>

response = client.get(reverse("投票应用:index"))
response = client.get(reverse("路由功能:路由功能"))  

"""