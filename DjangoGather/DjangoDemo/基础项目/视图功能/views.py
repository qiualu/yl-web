from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from urllib.parse import unquote

import urllib.parse

def index(request):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/
    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')
    return HttpResponse("表单视图 index %s" % decoded_path)


def detail(request, question_id):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/

    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')

    # 打印解码后的请求路径
    # print(f"请求路径: {decoded_path}")
    # 使用元组来传递所有格式化参数
    return HttpResponse("视图:  %s at question %s." % (decoded_path, question_id))
def results(request, question_id):
    response = "视图:  results of question %s."

    # 运算符来格式化一个只设计用于单个参数的
    return HttpResponse(response % question_id)
def vote(request, question_id):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/

    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')

    return HttpResponse("视图:  on question %s." % question_id)


from django.template import loader
def html_index(request):
    template = loader.get_template('html/index.html')
    context = {
            'latest_question_list': 5,
        }
    return HttpResponse(template.render(context, request))

from django.http import Http404

from 投票应用.models import Question

def html_render(request):
    latest_question_list = [0,0,0,1,5,6]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'html/index.html', context)

from django.shortcuts import get_object_or_404

def ModelID(request, question_id): 
    # 方式一
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # raise Http404("没找到该id 的数据")
        return HttpResponse("没找到该id 的数据.")
    # 方式二
    # question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'ModelID.html', {'question': question})

# 定义一个选项模型，与问题相关联

def 前五个数据(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, '前五个数据.html', context)
def 前五跳转_选项模型(request, question_id):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}


    # 方式一
    try:
        question = Question.objects.get(pk=question_id)
        choices = question.choice_set.all()  # 获取所有与该问题相关联的选项
        context = {'all_choices_list': choices}
    except Question.DoesNotExist:
        raise Http404("没找到该id 的数据")

    return render(request, '前五跳转_选项模型.html', context)


def 使用html(request):
    return render(request, '网页文件index.html')


# D:\Project\PyProject\DjangoGather\DjangoDemo\基础项目\网页文件\多路径多同名选择.html
# D:\Project\PyProject\DjangoGather\DjangoDemo\基础项目\网页文件\多路径多同名选择.html
def 多路径多同名选择(request):
    return render(request, '多路径多同名选择.html')

def 选择文件(request):
    return render(request, '选择文件.html')





