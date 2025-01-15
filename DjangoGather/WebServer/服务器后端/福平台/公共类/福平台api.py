


from ninja import NinjaAPI

福平台api = NinjaAPI(version='2.0.0')

@福平台api.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@福平台api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}



from 福平台.demo.router import demo_router

# api//hello

福平台api.add_router('/demo/', demo_router)

# C:\Users\yl\Desktop\DockerProject\yl-web\DjangoGather\WebServer\服务器后端\福平台\demo\router.py


"""

C:\Users\yl\Desktop\DockerProject\fu-admin\backend\fuadmin\settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'system',
    'demo',
    'generator',
]

C:\Users\yl\Desktop\DockerProject\fu-admin\backend\generator\template_test\model.py
C:\Users\yl\Desktop\DockerProject\fu-admin\backend\generator\test\model.py
C:\Users\yl\Desktop\DockerProject\fu-admin\backend\generator\test_demo\model.py

生成迁移文件：
python manage.py makemigrations your_app_name
查看迁移文件内容：
python manage.py sqlmigrate your_app_name 0001

应用迁移：

最后，使用以下命令应用迁移到数据库：
python manage.py migrate


"""

 
