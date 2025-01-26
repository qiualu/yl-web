

cd /DjangoGather/DjangoLearn/djdemo

* django-admin快速创建django项目
django-admin startproject djdemo


# 操作流程 
cd C:\Users\yl\Desktop\DockerProject\yl-web
docker ps
* 进入镜像
docker-compose exec -it django-gather bash
* 创建工程
django-admin startproject djdemo
* 进入工程目录
cd /DjangoGather/DjangoLearn/djdemo
* 启动服务
python manage.py runserver 0.0.0.0:8000

runserver 127.0.0.1:8000  # 只允许当前操作系统通过本地IP/域名访问
runserver 0.0.0.0:8088   # 允许其他的操作系统通过IP/域名访问

* 创建应用  创建子应用
python manage.py startapp 子应用名称（目录）
django-admin startapp 子应用名称
python manage.py startapp mycookie
* 创建超级密码
python manage.py createsuperuser
*库列表
pip freeze > requirements.txt

# 修改日志
# 数据库迁移生效
python manage.py makemigrations
python manage.py migrate

常见的web服务器软件:  nginx，uwsgi，gunicorn，apache，toncat，uvicon。

# app
home : request 基础
mycookie :  cookie 相关
sess : session 相关
user : 路由进阶的学习
tem : 模板

# MVT 设计模式

所谓的设计模式，就是前人针对解决常用业务场景所总结出来的一套解决方案【解决问题的流程】。

*Django*主要采用MVT模式。
*M-model*：模型，操作数据库功能部分。
*V-View*：视图，处理业务逻辑的位置，提取数据、获取用户数据等等操作都在这里。
*T-Template*：模版，用来展示视图操作后的数据，也可以在模版中为用户提供表单，让用户可以提交数据。

#  MVT 的交互流程 --前后端不分离开发， 后台工程师 会写前端代码（所有的， 只写模板部分）
#  MVC            前后端分离， 后台工程师 只写后台代码--json数据
1. 发请求----django框架--V--处理主业务逻辑（1.判断路由 2.解析参数 3.对接Model 4.返回数据）
2. V--获取数据--Model(交互数据库)
3. model--->V
4. V-->数据---Template-模板
5. Template--模板-数据渲染--V--展示--客户端

限制http请求

HTTP请求方法	描述
POST	添加/上传
GET	获取/下载
PUT	修改/更新，修改整体
PATCH	修改/更新，修改部分
DELETE	删除/废弃



* 随着项目的运行时间越长，用户量上来了，那么session数据也会不断增加，所以django虽然会自动删除过期的sesssion数据，但是如果用户没有正常注销的情况下，django是不会自动删除的，此时我们可以借助终端命令来进行删除。

python manage.py clearsessions






base64编码工具函数


Base64是网络上最常见的用于传输8Bit字节码的编码方式之一。
Base64就是一种基于64个可打印字符来表示二进制数据的方法。
64个可打印编码字符就是小写字母a-z、大写字母A-Z、数字0-9、符号"+"、"/"（再加上作为垫字的"="，实际上是65个字符）
base64的使用一般无非就是编码和解码：
	编码是从二进制数据流经过编码处理成base64字符的过程，可用于在HTTP环境下传递较长的标识信息。例如：图片内容
	解码是从base64字符还原到二进制字节流的过程

在python中，base64是内置常用的标准模块，我们可以直接通过import导入base64模块直接使用。

在javascript中，也内置了base64的相关函数，分别是atob与btoa。

b64demo.py，代码：


import json, base64
​
if __name__ == '__main__':
    # 要编码的原始数据
    data = {"uname":"root","uid":1}
    print(data)
    # 先转换成bytes类型数据
    data_bytes = json.dumps({"uname": "root", "uid": 1}).encode()
    print(data_bytes)
    # 编码
    base_data = base64.b64encode(data_bytes)
    print(base_data)
​
    # 解码
    str_bytes = b'eyJ1bmFtZSI6ICJyb290IiwgInVpZCI6IDF9'
    ori_data  = base64.b64decode(str_bytes).decode()
    # 字符串
    print(ori_data)
    # 变回原来的字典
    data = json.loads(ori_data)
    print(data)







