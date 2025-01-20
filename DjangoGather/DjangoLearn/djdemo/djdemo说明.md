

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

* 创建超级密码
python manage.py createsuperuser
*库列表
pip freeze > requirements.txt

# 修改日志
# 数据库迁移生效
python manage.py makemigrations
python manage.py migrate

常见的web服务器软件:  nginx，uwsgi，gunicorn，apache，toncat，uvicon。

 

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










