#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import json

#参考资料
#Python - 优雅而简单地完成http请求
#http://baijiahao.baidu.com/s?id=1599992188940440730&wfr=spider&for=pc
#https://www.cnblogs.com/jesseZh/p/4701266.html
#  测试参数
#  url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?"
#  json_data =  {"tel":"15850781443"}
def PostTest(url,json_data):
    # 发送post请求
    #json_data = {"user": "yunweicai", "op": "post"}
    #headers = {'content-type': 'charset=utf8'}
    #headers = {'content-type':'application/json'}
    #headers = {'content-type': 'application/octet-stream'}
    #data = json.dumps(json_data)
    #r11 = requests.post(url,json_data,headers)
    r11=requests.post(url, data=json.dumps(json_data), headers={'Content-Type': 'application/json'})
    #r11 = requests.post(url, data)
    #r11 = requests.post(url, json_data, headers)
    #values_json = json.dumps(json_data)
    #r11 = requests.post(url, values_json, headers)
    print(r11.text)

def GetTest(url):
    #发送get请求
    r11 = requests.get(url)
    print(r11.text)