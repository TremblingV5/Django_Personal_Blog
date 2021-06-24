FROM python:3.6

# 容器内安装时使用清华源
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt update
# 安装netcat
RUN apt-get update && apt install -y netcat

MAINTAINER zhengfei.xin <zf.xin@qq.com>

# 设置 python 环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 可选：设置镜像源为国内
COPY pip.conf /root/.pip/pip.conf

# 容器内创建 Code 文件夹
ENV APP_HOME=/var/www/html/Code
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# 将当前目录加入到工作目录中（. 表示当前目录）
ADD . $APP_HOME
RUN /bin/bash ./create_resources_path.sh
RUN chmod -R 777 /var/www/html/Code/resources
RUN chmod -R 777 /var/www/html/Code/PersonalBlog/whoosh_index

# 更新pip版本
RUN /usr/local/bin/python -m pip install --upgrade pip

# 安装项目依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY six.py /usr/local/lib/python3.6/site-packages/django/utils

# 移除\r in windows
RUN sed -i 's/\r//' ./start.sh

# 给start.sh可执行权限
RUN chmod +x ./start.sh

# 数据迁移，并使用uwsgi启动服务
ENTRYPOINT /bin/bash ./start.sh