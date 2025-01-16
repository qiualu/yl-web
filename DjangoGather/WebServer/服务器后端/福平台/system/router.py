
from ninja import Router


system_router = Router()


# /api/system/get   http://127.0.0.1:8000/api/system/get
@system_router.get("/get")
def hello(request):
    return {"message": "Hello, system_router!"}

# 自定义异常类
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

@system_router.get("/ys/{item_id}")
def get_item(request, item_id: int):

    if item_id == 100:
        # 触发自定义异常
        raise MyCustomError("触发自定义异常 ")

    return {"item_id": item_id, "name": "Sample Item"}
    # try:
    #     # 尝试调用可能触发异常的函数
    #     result = divide_numbers(10, 0)
    #     print(f"结果是: {result}")
    # except MyCustomError as e:
    #     # 捕获并处理自定义异常
    #     print(f"捕获到异常: {e}")


from .apis.登录 import router as login_router


system_router.add_router('/', login_router, tags=["登录"])

