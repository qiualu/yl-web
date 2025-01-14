FROM python:3.12

ENV PYTHONUNBUFFERED=1

# 设置工作目录  docker-compose.yml 已经设置了
# WORKDIR /DjangoGather/DjangoDemo/基础项目
# WORKDIR /DjangoGather 


# RUN ls
 

# 复制requirements.txt到容器中 requirements.txt
#COPY DjangoDemo/基础项目/requirements.txt requirements.txt
#COPY requirements.txt requirements.txt
COPY DjangoGather/DjangoDemo/基础项目/requirements.txt requirements.txt



# 安装Python依赖
RUN pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt




# CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "基础项目.asgi:application"]

