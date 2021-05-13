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
    
    > https://www.baidu.com/s?wd=docker
    
2. Docker Compose
    ```shell script
    docker-compose -f docker-compose_py_dev.yml up --build -d
    ```
    
3. 运行完毕后，执行数据库文件```./Code/init_db.sql```添加初始化信息

4. 访问127.0.0.1
