#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

#参考资料
#Python - 优雅而简单地完成http请求
#http://baijiahao.baidu.com/s?id=1599992188940440730&wfr=spider&for=pc
#  测试参数
#  url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?"
#  json_data =  {"tel":"15850781443"}
def PostTest(url,json_data):
    # 发送post请求
    #json_data = {"user": "yunweicai", "op": "post"}
    r11 = requests.post(url,json_data)
    print(r11.text)