

from typing import Any, List

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from ninja import Field, ModelSchema, NinjaAPI, Query, Router, Schema
from ninja.orm.metaclass import ModelSchemaMetaclass
from ninja.pagination import PaginationBase
from ninja.types import DictStrAny


def 账户认证():
    print("账户认证 Hello World")


def 账户认证5512():
    print("账户认证 5512  1111 ")


class FuNinjaAPI(NinjaAPI):
    def create_response(
            self, request: HttpRequest, data: Any, *, status: int = 200, code: int = 2000, msg: str = "success",
            temporal_response: HttpResponse = None,
    ) -> HttpResponse:
        std_data = {
            "code": code,
            "result": data,
            "message": msg,
            "success": True
        }
        content = self.renderer.render(request, std_data, response_status=status)
        content_type = "{}; charset={}".format(
            self.renderer.media_type, self.renderer.charset
        )

        return HttpResponse(content, status=status, content_type=content_type)






