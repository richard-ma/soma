# soma

## 安装
1. 安装数据库
    1. sqlite3
        1. Ubuntu
            1. apt-get install sqlite3
    1. mysql
        1. Ubuntu
            1. apt-get install mysql-server
            1. set password for root user
            1. create soma database
            1. create soma user
            1. grant privilidge for soma user
1. 修改SQLALCHEMY_DATABASE_URI
1. 创建数据库结构
    1. flask --app soma:create_app db init
    1. flask --app soma:create_app db migrate -m 'install'
    1. flask --app soma:create_app db upgrade
1. 运行系统
    1. 测试环境
        1. flask --app soma:create_app run --debug
    1. 生产环境

## 模块划分
1. 商户管理 merchant
    1. 订单 order
    1. 购物网站 shop
1. 收款网站 executer
    1. stripe管理 stripe
1. 基础设置 settings
    1. 系统配置 system settings
    1. 汇率设置 currency exchange rate settings
    1. 个人资料 personal settings
1. 运行日志 logs
1. API Key生成算法
    1. 哈希算法
        1. md5
        1. sha
    1. 哈希参数
        1. 购物网站网址
        1. API Key生成时的时间
        1. 随机salt