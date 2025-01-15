from ninja import Router
# # from demo.api import router

from .api import router

demo_router = Router()
# demo_router.add_router('/', router, tags=["Demo"])


# http://127.0.0.1:8000/api/demo/123
@demo_router.get("/")
def get_item(request):
    return {"message": "demo_router"}  


demo_router.add_router('/', router, tags=["Demo"])
