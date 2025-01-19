# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 00:02
# @Author  : 臧成龙
# @FileName: router.py
# @Software: PyCharm

from ninja import Router
 
from system.apis.login import router as login_router
 
system_router = Router()
 
system_router.add_router('/', login_router, tags=["Login"])
 