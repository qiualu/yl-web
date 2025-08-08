from ninja import NinjaAPI, Router 
 

相关多个的路由多层结构 = NinjaAPI()

#  /案例模板/ninjaAPI案例/相关多个的路由多层结构/ 
@相关多个的路由多层结构.get("/")
def hello(request):
    return {"message": "Hello, 相关多个的路由多层结构!"}


# 定义一个子路由
item_router = Router()
@item_router.get("/")
def item_hello(request):
    return {"message": "Hello, 相关多个的路由多层结构! 子路由 items "}



# 定义一个子路由
demo_router = Router()
@demo_router.get("/")
def demo_hello(request):
    return {"message": "Hello, 相关多个的路由多层结构! 子路由 demo "}


# 定义一个子路由 中的子路由
# 定义一个子路由
zly_router = Router()
@zly_router.get("/")
def zly_hello(request):
    return {"message": "Hello, 相关多个的路由多层结构! 子路由 的子路由 zly "}

item_router.add_router("/zly", zly_router)


# 将子路由添加到主路由  tags=["Items"]) tags 文档标识
相关多个的路由多层结构.add_router("/items", item_router,tags=["Items"])
相关多个的路由多层结构.add_router("/demo", demo_router)

# 同个路径进入多个子路由 相同匹配 则先配上为先
# 相关多个的路由多层结构.add_router("/x", item_router)
# 相关多个的路由多层结构.add_router("/x", demo_router)



