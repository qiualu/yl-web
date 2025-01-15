


from ninja import NinjaAPI

福平台api = NinjaAPI()

@福平台api.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@福平台api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}







