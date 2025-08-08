from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

# Create your views here.
from django.http import JsonResponse  # 关键：导入JsonResponse
from django.utils import timezone
from .models import 计数记录



from django.http import JsonResponse
from .models import 计数记录
 
def 触发计数(request):
    if request.method == "POST":
        计数记录.objects.create()
        总次数 = 计数记录.objects.count()
        # 添加参数确保中文正常显示
        return JsonResponse({
            "状态": "成功",
            "消息": "计数成功",
            "总次数": 总次数
        }, json_dumps_params={'ensure_ascii': False})  # 关键参数
    
    # http://127.0.0.1:8000/全运会计数/触发/?action=count
    # http://127.0.0.1:8000/全运会计数/触发/?设备编号=1&当前计数=1
    # 仅允许 GET 请求，并验证参数（例如必须包含 action=count）
    
    if request.method == "GET":
        # 获取 URL 中的参数（例如 ?action=count）
        报错状态 = True
        try:
            设备编号 = int(request.GET.get('设备编号', '0'))
            当前计数 = int(request.GET.get('当前计数', '0'))
            上传值 = int(request.GET.get('上传值', '0'))
            if 设备编号 == 0:
                报错状态 = False
        except:
            报错状态 = False
  
        if 报错状态:
            print(f"设备编号 : {设备编号}  当前计数: {当前计数} 上传值:{上传值} ")
            # 创建计数记录
            计数记录.objects.create()
            # 获取当前总次数
            总次数 = 计数记录.objects.count()
            return JsonResponse({
                "状态": "成功",
                "消息": "计数成功",
                "总次数": 总次数
            }, json_dumps_params={'ensure_ascii': False})
        else:
            # 参数错误时的响应
            return JsonResponse({
                "状态": "错误",
                "消息": "参数错误，设备编号=1&当前计数=1"
            }, status=400, json_dumps_params={'ensure_ascii': False})


    # 错误响应也需要添加
    return JsonResponse(
        {"状态": "错误", "消息": "没有匹配的请求模式"},
        status=400,
        json_dumps_params={'ensure_ascii': False}  # 关键参数
    )

# def 获取统计数据(request):
#     总次数 = 计数记录.objects.count()
#     今天 = timezone.now().date()
#     今日次数 = 计数记录.objects.filter(触发时间__date=今天).count()
#     本月开始 = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#     本月次数 = 计数记录.objects.filter(触发时间__gte=本月开始).count()
    
#     网页路径 = "http://yulu512.picp.io"

#     # 统计接口也添加参数
#     return JsonResponse({
#         "总次数": 总次数,
#         "今日次数": 今日次数,
#         "本月次数": 本月次数，
#         "网页路径": 网页路径
#     }, json_dumps_params={'ensure_ascii': False})  # 关键参数

def 获取统计数据(request):
    # 获取统计数据
    总次数 = 计数记录.objects.count()
    今天 = timezone.now().date()
    今日次数 = 计数记录.objects.filter(触发时间__date=今天).count()
    本月开始 = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    本月次数 = 计数记录.objects.filter(触发时间__gte=本月开始).count()
    
    # 网页路径配置
    网页路径 = ""  # 空的时候不用更新
    # 网页路径 = "http://yulu512.picp.io"  # 需要时启用
    
    # 获取服务器当前时间（带时区信息的ISO格式）
    服务器时间 = timezone.now().isoformat()
    
    # 返回包含时间的统计数据
    return JsonResponse({
        "总次数": 总次数,
        "今日次数": 今日次数,
        "本月次数": 本月次数,
        "网页路径": 网页路径,
        "服务器时间": 服务器时间  # 新增：返回服务器当前时间
    }, json_dumps_params={'ensure_ascii': False})


def 无定义页面(request, path=None):  # 添加path参数，设为可选
    当前时间 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"""
    <html>
        <head>
            <title>页面未找到</title>
        </head>
        <body>
            <h1>访问的路径不存在</h1>
            <p>当前时间: {当前时间}</p>
            <p>您访问的路径: {path if path else '/'}</p>  <!-- 显示访问的路径 -->
            <p>请访问以下正确的网址：</p>
            <ul>
                <li>/触发/ - 硬件按钮触发计数接口（POST）</li>
                <li>/统计/ - 获取统计数据接口（GET）</li>
            </ul>
        </body>
    </html>
    """, status=404)
