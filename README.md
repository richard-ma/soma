# soma

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