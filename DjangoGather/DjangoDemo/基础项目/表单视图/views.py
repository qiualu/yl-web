from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from urllib.parse import unquote

import urllib.parse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from 投票应用.models import Question, Choice


def 表单视图(request):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/
    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')
    return HttpResponse("表单视图 index %s" % decoded_path)

def 一个简单的表单(request,question_id):
    # request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/
    # # 解码请求路径中的 URL 编码部分
    # decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')
    # return render(request, '一个简单的表单.html' )
    # 这一行代码通过 get_object_or_404 函数从数据库中获取指定主键（pk=question_id）对应的 Question 对象。
    # 如果未找到对应的问题，它会返回一个 HTTP 404 错误页面，显示未找到相关对象。
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        print(" 一个简单的表单: 一个简单的表单.html ")
        return render(request, '一个简单的表单.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else: # 没有异常错误则运行 这里 except _ else == if else
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        print(" 一个简单的表单: 查询单个数据  ")
        return HttpResponseRedirect(reverse('查询单个数据', args=(question.id,)))


def 查询单个数据(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, '查询单个数据.html', {'question': question})




""" 

    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

    <form action="{% url 'polls:vote' question.id %}" method="post">
    {% csrf_token %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
    {% endfor %}
    <input type="submit" value="Vote" />
    </form>


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
        raise Http404("没找到该id 的数据")

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

 """




