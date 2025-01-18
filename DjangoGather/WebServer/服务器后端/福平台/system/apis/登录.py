
from ninja import Router, ModelSchema, Query, Schema, Field

import json
from datetime import datetime
# from django.core.cache import cache

from django.contrib import auth
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404 
 
 
from 福平台.公共类.fu_response import FuResponse
from 福平台.公共类.request_util import save_login_log
from 福平台.公共类.usual import get_user_info_from_token

from 服务器后端.settings import SECRET_KEY
from 福平台.公共类.模块参数配置 import TOKEN_LIFETIME,token有效时间
from 福平台.system.models import Users, Role, MenuButton, MenuColumnField

from 福平台.公共类.令牌格式 import FuJwt

router = Router()

class SchemaOut(ModelSchema):
    homePath: str = Field(None, alias="home_path")

    class Config:
        model = Users
        model_exclude = ['password', 'role', 'post']


class LoginSchema(Schema):
    username: str = Field(None, alias="username")
    password: str = Field(None, alias="password")

class Out(Schema):
    multi_depart: str
    sysAllDictItems: str
    departs: str
    userInfo: SchemaOut
    token: str


@router.post("/login", response=Out, auth=None)
def login(request, data: LoginSchema):
    print(" ------------------------ ")
 
    user_obj = auth.authenticate(request, **data.dict())
    print(user_obj,type(user_obj))
    print(" +++++++++++++++++++++++++++++ ")
    if user_obj:
        request.user = user_obj

        print(type(user_obj),user_obj.role)

        role = user_obj.role.all().values('id')
        post = list(user_obj.post.all().values('id'))
        role_list = []
        post_list = []
        for item in role:
            role_list.append(item['id'])
        for item in post:
            post_list.append(item['id'])
        user_obj_dic = model_to_dict(user_obj)
        user_obj_dic['post'] = post_list
        user_obj_dic['role'] = role_list
        del user_obj_dic['password']
        del user_obj_dic['avatar']

        time_now = int(datetime.now().timestamp())
        jwt = FuJwt(SECRET_KEY, user_obj_dic, valid_to=time_now + TOKEN_LIFETIME)
        # 将生成的token加入缓存
        # cache.set(user_obj.id, jwt.encode())
        token = f"bearer {jwt.encode()}"
        data = {
            "multi_depart": 1,
            "sysAllDictItems": "q",
            "departs": "e",
            'userInfo': user_obj_dic,
            'token': token
        }
        save_login_log(request=request)
        return data
    else:
        return FuResponse(code=500, msg="账号/密码错误")



