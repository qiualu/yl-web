


from ninja import NinjaAPI

福平台api = NinjaAPI()

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