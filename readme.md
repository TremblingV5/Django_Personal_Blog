# 基于Django的个人博客

> 一款简单的基于Django的个人博客系统，仅支持个人用户建站使用
> 
> 功能比较简单，欢迎各位小伙伴提PR或者issues

## 联系方式

若部署有问题或代码有bug欢迎各位小伙伴提issue或直接给我发邮件

> E-Mail: <a href="mailto:zf.xin@qq.com">zf.xin@qq.com</a>

## 现有功能

1. 简历模块
    1. 展示个人信息
    2. 展示个人工作学习经历
    3. 展示个人技术栈
2. 博文展示模块
    1. 轮播图和最近发表文章
    2. 个人自述页面
    3. 时间线模式的博文列表
    4. 根据文章分类的博文列表
3. 管理模块 
    1. 简历页面个人信息的修改
    2. 文章管理

## 部署

### 部署方案

> docker + nginx + uwsgi + mysql + redis

### 运行

1. 安装Docker

    > <https://www.baidu.com/s?wd=docker>

2. Docker Compose

    ```shell script
    docker-compose -f docker-compose_py_dev.yml up --build -d
    ```

3. 运行完毕后，执行数据库文件```./Code/init_db.sql```添加初始化信息

4. 访问127.0.0.1

### 生产环境

1. 安装Docker（略）

2. 更改```./Code/.env```中数据库密码

3. 将ssl证书复制到```./compose/compose_py_prod/nginx/ssl```目录下，分别命名为```cert.pem```和```cert.key```

4. 修改```./Code/PersonalBlog/settings_prod.py```中的```ALLOWED_HOSTS```，添加域名或ip以便正常访问

5. Docker compose（略）

### 如何Debug

当使用docker compose启动服务后，访问域名或ip很有可能无法访问，可以考虑按照以下步骤debug，通常可以排除掉故障并正常访问到页面。

1. 解决nginx报502
    nginx报502并不意味着就一定是nginx出了问题，此时应该查看nginx的报错日志，然后考虑如何进行下一步。

    报错日志位于```./Code/compose/compose_prod/nginx/log/error.log```

    第一种错误类型：nginx配置文件的错误，由于nginx版本不一致及对配置项的修改，可能导致报错，此时应仔细阅读报错信息，并进行修改。

    第二种错误类型：日志中报连接错误，此时应该查看django的错误信息

2. 查看docker日志
   使用命令```docker ps -a```查看容器id

   然后使用命令```docker logs $CONTAINER_ID```查看容器的日志

3. 其他
    根据我个人的运行和测试，只要未对配置及部署相关的文件做较大变动，就不会有什么特别奇怪的报错，通常只是mysql相关的配置不正确，或者缺少文件等等简单的错误。若遇到难以解决的问题，欢迎**提issue**或是**给我发邮件<a href="mailto:zf.xin@qq.com">zf.xin@qq.com</a>**
