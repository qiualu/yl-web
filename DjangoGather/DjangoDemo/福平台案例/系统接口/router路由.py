


from ninja import Router

系统接口路由 = Router()

from 系统接口.路由接口.登录 import 路由 as 登陆路由

 
系统接口路由.add_router('/', 登陆路由, tags=["登陆路由"])



