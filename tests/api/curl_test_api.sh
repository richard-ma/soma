#!/bin/bash

# 测试发送表单数据 不进行url编码
curl -d "hello=world world" -X POST http://127.0.0.1:5000/api/post_form_test

# 测试发送表单数据 不进行url编码
curl --data-urlencode "hello=hello world" http://127.0.0.1:5000/api/post_form_test

# 模拟woocommerce插件向api接口发送订单信息