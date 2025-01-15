# from ninja import NinjaAPI, Router, Field, ModelSchema
from ninja import NinjaAPI, Router, Field, Schema  # 注意这里使用 Schema 而不是 ModelSchema
 
class Item(Schema):
    id: int
    name: str = Field(..., max_length=100)

    class Meta:
        pass  # 这里可以添加配置，如果没有特定配置，则保持为空
 
相关多个的路由 = NinjaAPI(version='2.0.0')

# 定义一个子路由
item_router = Router()
# "GET /案例模板/ninjaAPI案例/相关多个的路由/items/123 
@item_router.get("/{item_id}")
def get_item(request, item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@item_router.post("/")
def create_item(request, item: Item):
    # 假设我们保存了项目数据
    item.id += 100 
    return item


# "GET /案例模板/ninjaAPI案例/相关多个的路由/helloXX HTTP/1.1"
@相关多个的路由.get("/helloXX")
def hello(request):
    return {"message": "HelloXX, World!"}

# "GET /案例模板/ninjaAPI案例/相关多个的路由/items/ 
# 将子路由添加到主路由
相关多个的路由.add_router("/items", item_router)


# 相关多个的路由.add_router("/items", item_router, tags=["Items"]) tags 文档标识


 
"""

import requests
import json

# 定义你的 Ninja API 服务器的 URL
# 注意：这里的 URL 是一个示例，你需要根据你的实际情况来替换它
# 假设你的 Ninja API 服务器运行在 localhost:8000 上
base_url = "http://localhost:8000/案例模板/ninjaAPI案例/相关多个的路由"

# 要发送的 POST 数据，符合 Item Schema
post_data = {
    "id": 42,  # 示例 ID
    "name": "New Item Name"  # 示例名称，不超过 100 个字符
}

# 发送 POST 请求
response = requests.post(f"{base_url}/items/", json=post_data)

# 打印响应的状态码和响应体
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")



"""