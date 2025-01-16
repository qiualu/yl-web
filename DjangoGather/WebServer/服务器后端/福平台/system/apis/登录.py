
from ninja import Router, ModelSchema, Query, Schema, Field


router = Router()



# @router.post("/login", response=Out, auth=None)
# def login(request, data: LoginSchema):
#     user_obj = auth.authenticate(request, **data.dict())
#     if user_obj:
#         request.user = user_obj
#         role = user_obj.role.all().values('id')
#         post = list(user_obj.post.all().values('id'))
#         role_list = []
#         post_list = []
#         for item in role:
#             role_list.append(item['id'])
#         for item in post:
#             post_list.append(item['id'])
#         user_obj_dic = model_to_dict(user_obj)
#         user_obj_dic['post'] = post_list
#         user_obj_dic['role'] = role_list
#         del user_obj_dic['password']
#         del user_obj_dic['avatar']

#         time_now = int(datetime.now().timestamp())
#         jwt = FuJwt(SECRET_KEY, user_obj_dic, valid_to=time_now + TOKEN_LIFETIME)
#         # 将生成的token加入缓存
#         # cache.set(user_obj.id, jwt.encode())
#         token = f"bearer {jwt.encode()}"
#         data = {
#             "multi_depart": 1,
#             "sysAllDictItems": "q",
#             "departs": "e",
#             'userInfo': user_obj_dic,
#             'token': token
#         }
#         save_login_log(request=request)
#         return data
#     else:
#         return FuResponse(code=500, msg="账号/密码错误")



