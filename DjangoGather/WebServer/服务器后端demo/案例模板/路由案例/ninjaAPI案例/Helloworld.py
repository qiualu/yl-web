






from ninja import NinjaAPI

HelloWorld = NinjaAPI()



# /案例模板/ninjaAPI案例/HelloWorld/

@HelloWorld.get("/")
def root(request):
    return {"message": "Hello, all!"}


# "GET /案例模板/ninjaAPI案例/HelloWorld/hello

@HelloWorld.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@HelloWorld.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}













