
# from typing import List

# # from demo.models import Demo
# from .models import Demo

from ninja import Field, ModelSchema, Query, Router
# from ninja.pagination import paginate

# # from utils.fu_crud import (
# #     ImportSchema,
# #     create,
# #     delete,
# #     export_data,
# #     import_data,
# #     retrieve,
# #     update,
# # )
# # from utils.fu_ninja import FuFilters, MyPagination

router = Router()


@router.get("/get_demo/")
def hello(request):
    return {"message": "HelloXX, World!"}

# 为啥这里返回的是  {"detail": [{"type": "int_parsing", "loc": ["path", "item_id"], "msg": "Input should be a valid integer, unable to parse string as an integer"}]}

# http://127.0.0.1:8000/api/demo/api/123
@router.get("/api/{item_id}")
def get_item(request, item_id: int):
    return {"router id": item_id, "name": "Sample Item"}

# 返回 是 {"router id": 123, "name": "Sample Item"}


# # 设置过滤字段
# class Filters(FuFilters):
#     name: str = Field(None, alias="name")
#     code: str = Field(None, alias="code")
#     status: int = Field(None, alias="status")
#     id: str = Field(None, alias="demo_id")


# # 设置请求接收字段
# class DemoSchemaIn(ModelSchema):
#     remark: list

#     class Config:
#         model = Demo
#         model_fields = ['name', 'code', 'sort', 'status']


# # 设置响应字段
# class DemoSchemaOut(ModelSchema):

#     class Config:
#         model = Demo
#         model_fields = ['id', 'name', 'code', 'sort', 'status', 'remark', 'create_datetime']


# # 创建Demo
# @router.post("/demo", response=DemoSchemaOut)
# def create_demo(request, data: DemoSchemaIn):
#     data.remark = ','.join(data.remark)
#     demo = create(request, data, Demo)
#     return demo


# # 删除Demo
# @router.delete("/demo/{demo_id}")
# def delete_demo(request, demo_id: int):
#     delete(demo_id, Demo)
#     return {"success": True}


# # 更新Demo
# @router.put("/demo/{demo_id}", response=DemoSchemaOut)
# def update_demo(request, demo_id: int, data: DemoSchemaIn):
#     data.remark = ','.join(data.remark)
#     demo = update(request, demo_id, data, Demo)
#     return demo


# # 获取Demo
# @router.get("/demo", response=List[DemoSchemaOut])
# @paginate(MyPagination)
# def list_demo(request, filters: Filters = Query(...)):
#     qs = retrieve(request, Demo, filters)
#     return qs


# # 导入
# @router.get("/demo/all/export")
# def export_demo(request):
#     export_fields = ['name', 'code', 'status']
#     return export_data(request, Demo, DemoSchemaOut, export_fields)


# # 导出
# @router.post("/demo/all/import")
# def import_demo(request, data: ImportSchema):
#     import_fields = ['name', 'code', 'status']
#     return import_data(request, Demo, DemoSchemaIn, data, import_fields)


# from ninja import Field, ModelSchema, Query, Router
 
 
# router = Router()
