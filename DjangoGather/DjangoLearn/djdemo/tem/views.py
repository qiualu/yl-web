from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.http.response import HttpResponse
from django.template.loader import render_to_string


import os.path
from django.conf import settings




def index1(request):
    """显示模板"""
    # render函数实现3个功能：
    # 1. 识别查找模板目录下对应的HTML文件
    # 2. 读取HTML文件内容，替换特殊的模板语法
    # 3. 实例化response对象
    response = render(request, "index.html")
    # print(response)  # <HttpResponse status_code=200, "text/html; charset=utf-8">
    # print(response.content.decode())  # render读取模板文件以后，生成的HTML文档内容
    return response


def index2(request):
    """视图中传递数据到模板中显示"""
    title = "我的网页标题"
    author = "moluo"
    # 模板引擎可以把HTML模板中的特殊变量语法替换成真实数据，真实数据通过视图中的context传递进去
    # response = render(request, "index.html",  context={"title": title,"author": author})
    response = render(request, "index.html",  locals())
    # print(response.content.decode())
    return response


# Create your views here.
def index3(request):
    """模板引擎的基本使用"""
    data = {}
    title = "模板引擎的基本使用"
    data["title"] = title 
    data["author"] = "moluo_index3"
    # return render(request, "tem/index.html", context={"title":title})
    # return render(request, "tem/index.html", data)
    # return render(request, "index.html", data)
    # 1. 初始化模板,读取模板内容,实例化模板对象
    # 基于settings.py中配置的模板引擎获取DIRS配置的模板文件，转换成Template模板对象
    # get_template会从项目配置中找到模板目录，我们需要填写的参数就是补全模板文件的路径
    template = get_template("index.html")
    # 调用模板对象提供的render函数，把本次客户端的请求对象和视图中数据data传参到模板文件中，进行渲染
    # 将来如果要对模板中的内容进行数据缓存[cache]，可以对content进行保存起来，将来如果直接读取content的话，
    # 则django就不需要操作数据库或者进行数据渲染，因为模板渲染的过程就是正则替换的过程。
    # 2. 识别context内容, 和模板内容里面的标记[标签]替换,针对复杂的内容,进行正则的替换
    # render中完成了变量替换成变量值的过程，这个过程使用了正则。
    content = template.render(data, request)
    # 3. 通过response响应对象,把替换了数据的模板内容返回给客户端
    return HttpResponse(content)

# render_to_string 是工作中，经常用于缓存优化的工具函数，非常重要，但是少用
def index4(request):
    # 要显示到客户端的数据
    name = "hello DTL!"
    # render_to_string 在工作中，有时候可用于缓存优化。
    tpl_content = render_to_string('index.html', {"author":name})
    return HttpResponse(tpl_content)


# Create your views here.
def index5(request):
    """在视图中调用模板引擎提供的渲染函数实现前后端不分离"""
    # data = {"name": "杨戬", "age": 1500}
    # # return render(request, template_name="index.html", context=data)
    # return render(request, "index.html", data)

    # name = "杨戬"
    # age = 16
    # return render(request, "index.html", locals())

    name = "杨戬"
    age = 16

    # 判断是否有缓存页面，如果有缓存页面，就加载缓存页面
    from django.template.loader import get_template
    template_name = "index.html"
    if os.path.isfile(str(settings.BASE_DIR / "cache" / template_name)):
        with open(f"cache/{template_name}", "r") as f:
            content = f.read()
    else:
        print("走了数据库！")
        # 获取模板引擎对象
        template = get_template("index.html")
        # 使用模板引擎对象的渲染函数来对模板进行渲染
        content = template.render(locals(), request)
        with open(f"cache/{template_name}", "w") as f:
            f.write(str(content))
    return HttpResponse(content)




def index6(request):
    """模板引擎的语法"""
    from django.conf import settings
    import time
    num1 = 100
    num2 = 3.14
    name = "xiaoming"
    data1 = {1,2,3}
    data2 = (1,2,3,4)
    data3 = [1,2,3,4]
    data4 = {"name":"xiaohui","age": 17}
    data5 = settings
    book_list = [
        {"id": 10, "price": 9.90, "name": "python3天入门到挣扎", },
        {"id": 11, "price": 19.90, "name": "python7天入门到垂死挣扎", },
    ]
    return render(request, "index2.html", locals())







