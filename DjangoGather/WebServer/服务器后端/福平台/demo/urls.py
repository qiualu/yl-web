from django.urls import path

from . import views


from django.urls import re_path

# 路由功能

# 注册自定义的路径转换器
from django.urls import path, register_converter
class FourDigitYearConverter:

    # 这个属性定义了一个正则表达式，用于匹配URL中的字符串。在这个例子中，它匹配任何由四个数字组成的字符串，这通常代表一个年份。
    regex = "[0-9]{4}"

    # 用来处理匹配的字符串转换为传递到函数的类型。
    def to_python(self, value):
        print(" to_python : ",value,"  ",type(value))
        return int(value) + 5 # 可以修订修改
    # 它将处理 Python 类型转换为字符串以用于 URL 中。
    def to_url(self, value):
        print(" to_url : ", value)
        return "%04d" % value

register_converter(FourDigitYearConverter, "yyyy")



urlpatterns = [
    path('', views.路由功能, name='路由功能'), # ip/路由功能/
    path(r'单个匹配/', views.单个匹配),

    path(r'匹配整数/<int:year>', views.匹配整数),  # year 作为参数要写在 匹配整数 函数中
    path(r'匹配整数/<int:year>/', views.匹配整数),  # year 作为参数要写在 匹配整数 函数中
    path(r'匹配非空字符串/<str:name>', views.匹配字符串),  # 匹配任何非空字符串（不包括斜杠/）。
    path(r'匹配字符串/<slug:name>', views.匹配字符串),  # 匹配由小写字母、数字、下划线和连字符组成的字符串（通常用于匹配文章或对象的简洁名称）。
    path(r'匹配UUID格式字符串/<uuid:name>', views.匹配字符串),  # 匹配UUID格式的字符串。
    path(r'匹配任意字串/<name>', views.匹配字符串),  # # 匹配任何字符串（不包括斜杠/）。
    # 包括斜杠/
    path(r'匹配所有字符串/<path:name>', views.匹配字符串),  # 匹配任何非空字符串，包括斜杠/（这允许你匹配完整的URL路径）。
    #注册自定义的路径转换器
    path(r'注册自定义的路径转换器/<yyyy:name>', views.注册自定义的路径转换器),  # 匹配四位数字。


    # 它允许使用正则表达式来匹配URL路径。
    # 首页路由，匹配根URL（即'/'） ^：匹配字符串的开始。 $：匹配字符串的结束。
    re_path(r'^正则首页路由$', views.正则首页路由, name='正则首页路由'),
    # 正则案例
    re_path(r'^正则/\d+$', views.正则_匹配数字),   # 匹配数字：\d+ 完整: ^\d+$
    re_path(r'^正则传参/(\d+)$', views.正则_匹配数字),   # 匹配数字：\d+ 完整: ^\d+$
    # ?特殊的引导符 (?P...)中，P是Python正则表达式语法中用于命名捕获组的特定字符 捕获年份和月份，并将它们作为位置参数传递给视图
    re_path(r'^正则_匹配年月/(?P<year>\d{4})/(?P<month>\d{2})/$', views.正则_匹配年月), #命名捕获组的特定字符 传参
    re_path(r'^正则_匹配年月2/(\d{4})/(\d{2})/$', views.正则_匹配年月), # 按顺序传参
    re_path(r'^正则_匹配汉字/[\u4e00-\u9fa5]+$', views.正则_匹配汉字),
    re_path(r'^正则_匹配n的字符串/.{10}$', views.正则_匹配英文和数字), # ^.{n}$
    re_path(r'^正则_匹配n的字符串/.{10,50}$', views.正则_匹配英文和数字), # ^.{m,n}$


    re_path(r'正则匹配后续所有/.*$', views.正则匹配后续所有),
    re_path(r'^.*$', views.all),

]
# path(route, view, kwargs=None, name=None)
"""
path(route, view, kwargs=None, name=None)
path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name。

path() 参数： route¶
route 是一个匹配 URL 的准则（类似正则表达式）。
当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

这些准则不会匹配 GET 和 POST 参数或域名。
例如，URLconf 在处理请求 https://www.example.com/myapp/ 时，它会尝试匹配 myapp/ 。
        处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/。

path() 参数： view¶
当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。

path() 参数： name¶
为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。

route : 匹配方式 
路径转换器 <int:year>
str - 匹配除了 '/' 之外的非空字符串。如果表达式内不包含转换器，则会默认匹配字符串。
int - 匹配 0 或任何正整数。返回一个 int 。
slug - 匹配任意由 ASCII 字母或数字以及连字符和下划线组成的短标签。比如，building-your-1st-django-site 。
uuid - 匹配一个格式化的 UUID 。为了防止多个 URL 映射到同一个页面，必须包含破折号并且字符都为小写。比如，075194d3-6885-417e-a8a8-6c931e272f00。返回一个 UUID 实例。
path - 匹配非空字段，包括路径分隔符 '/' 。它允许你匹配完整的 URL 路径而不是像 str 那样匹配 URL 的一部分。

注册自定义的路径转换器

"""
# re_path(route, view, kwargs=None, name=None)
"""
它允许使用正则表达式来匹配URL路径。
re_path(route, view, kwargs=None, name=None)

1. 元字符
\b：表示单词的边界。
.：匹配除了换行符以外的任意字符。
*****：指定*前面的内容可以连续重复使用任意次（0次或多次）。
\d：匹配一位数字。
\s：匹配任意的空白符，包括空格、制表符、换行符等。
\w：匹配字母、数字、下划线或汉字。
+：匹配1个或更多（1次或多次）。
^：匹配字符串的开始。
$：匹配字符串的结束。
?：匹配零次或一次（0或1）。
{n} {n,} {n,m}：指定重复次数（左闭右闭区间）。
[]：字符类，匹配方括号中的任意字符。
()：分组，用于捕获匹配的文本或进行分组匹配。
2. 字符转义
查找元字符本身时，需要使用\来取消元字符的特殊意义。

3. 字符类
使用[]包含想要匹配的字符，如[0-9]代表匹配任意一位数字，等同于\d；[a-z0-9A-Z_]等同于\w（如果只考虑英文的话）。
4. 分枝条件
使用|进行分枝条件的匹配，注意各个条件的顺序。

5. 分组与捕获
使用()进行分组，并可以捕获匹配的文本。默认情况下，每个分组会自动拥有一个组号，从左向右以分组的左括号为标志，第一个出现的分组的组号为1，第二个为2，以此类推。
6. 零宽断言
(?=exp)：匹配exp前面的位置。
(?<=exp)：匹配exp后面的位置。
(?!exp)：匹配后面跟的不是exp的位置。
(?<!exp)：匹配前面不是exp的位置。
7. 常用模式
IgnoreCase：忽略大小写。
Multiline：多行模式，更改^和$的含义，使它们分别在任意一行的行首和行尾匹配。
Singleline：单行模式，更改.的含义，使其与每一个字符匹配（包括换行符\n）。


二、正则表达式的匹配方案
1. 匹配特定字符
匹配数字：^\d+$
匹配n位数字：^\d{n}$
匹配英文和数字：^[A-Za-z0-9]+$
匹配汉字：^[\u4e00-\u9fa5]+$
2. 匹配特定格式
匹配Email地址：^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
匹配IP地址：(\d{1,3}\.){3}\d{1,3}
匹 b配手机号码：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
匹配身份证号码：^\d{15}|\d{18}$
3. 匹配特定长度的字符串
匹配长度为n的字符串：^.{n}$
匹配长度在m到n之间的字符串：^.{m,n}$
4. 匹配复杂规则
匹配以字母开头，后面可以跟字母、数字、下划线的字符串，长度在6到18之间：^[a-zA-Z]\w{5,17}$
匹配非零开头的最多带两位小数的数字：^([1-9][0-9]*)+(\.[0-9]{1,2})?$
三、应用场景
正则表达式在多个领域都有广泛的应用，如：

数据验证：
数据验证是正则表达式最常见的应用场景之一。通过使用正则表达式，我们可以检查用户输入的数据是否符合特定的格式要求，如电子邮件地址、电话号码、身份证号码、密码强度等。
如果输入数据不符合规则，可以立即向用户反馈错误信息，要求用户重新输入，从而避免了无效数据的存储和处理。

"""


