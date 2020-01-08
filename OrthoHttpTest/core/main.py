#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
print(rootPath)
#添加当前工程路径到系统目录
sys.path.append(rootPath)
#添加第三方库目录到系统目录
third_path = os.path.split(curPath)[0]+os.path.sep+r"ThirdPartyLib"
print(third_path)
sys.path.append(third_path)

import util.filelib
import StressTest.OrthoInterfaceTest
#import geo_tool.searchRefImg
#import network.httpService
# import json
# import requests

if __name__ == "__main__":
    #根目录路径
    #data_folder = r"D:\TestData\OrthoAlgoTestData"
    #StressTest.OrthoInterfaceTest.FuseFlowTest(data_folder)
    #StressTest.OrthoInterfaceTest.FuseFlowTest()

    url = "http://172.16.40.54:6060/ortho/api/v1/rawdata/fuse"
    refImgFolder = '/sedata/data/admin/Quanliucheng/National_2M_hubei_420000/Standard_5W_DOM'
    dataFolder = '/sedata/data/admin/Quanliucheng/Original_hubeiorchongqing_410000or500000/decompress'
    outFolder = '/sedata/data/admin/Quanliucheng/Original_hubeiorchongqing_410000or500000/out'
    #StressTest.OrthoInterfaceTest.FuseFlowTest2(url,refImgFolder,dataFolder,outFolder)
    #StressTest.OrthoInterfaceTest.ImgRgbOutput()

#   root_path = r"/home/work/PythonCodeLib"
    #用来存放所有的文件路径
    #file_list = []
    #用来存放所有的目录路径
    #dir_list = []

    #imgFile = r"D:\TestData\OrthoAlgoTestData\src\GF1_PMS1_E115.7_N38.9_20180409_L1A0003111678_FUSION_GEO.tiff"
    #imgFile = r"/sedata/data/admin/Quanliucheng/Original_hubeiorchongqing_410000or500000/decompress/GF1_PMS1_E111.5_N30.0_20190725_L1A0004140035-PAN1/GF1_PMS1_E111.5_N30.0_20190725_L1A0004140035-PAN1.tiff"
    imgFile = r"D:\TestData\parallel_test\GF\GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600\GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1.tiff"
    env = geo_tool.searchRefImg.RasterEnv()
    geo_tool.searchRefImg.GetRasterEnv(imgFile,env)
    print(env.MinX)


    #url = "http://pv.sohu.com/cityjson?ie=utf-8"
    #url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?"
    #json_data =  {"tel":"15850781443"}
    #network.httpService.PostTest(url,json_data)

    #url = "http://pv.sohu.com/cityjson?ie=utf-8"
    #network.httpService.GetTest(url)
    # url = "http://life.tenpay.com/cgi-bin/mobile/MobileQueryAttribution.cgi?"
    # json_data = {"chgmobile": "15850781443"}
    # network.httpService.PostTest(url, json_data)
    url = "http://172.16.40.54:6060/ortho/api/v1/rawdata/fuse"
    #ref = json.dumps(["/usr/seis/data/admin/Quanliucheng/langfang/REF/廊坊mos.img"])
    json_data = {
"constZ": 0,
"demPath": "/usr/seis/data/admin/Quanliucheng/langfang/DEM/langfangdem.tif",
"feedNum": 1000,
"similarParm":1,
"rpcError":5.0,
"imgFusePath":"/usr/seis/data/admin/Quanliucheng/langfang/out/7600_fuse.tiff",
"mssOrthoPath":"/usr/seis/data/admin/Quanliucheng/langfang/out/7600-MSS1.tiff",
"mssPath":"/usr/seis/data/admin/Quanliucheng/langfang/src/MSS/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1.tiff",
"orthoMssRes": 0.00008,
"orthoPanRes": 0.00002,
"orthoWKT": "",
"panOrthoPath":"/usr/seis/data/admin/Quanliucheng/langfang/out/7600-PAN1.tiff",
"panPath":"/usr/seis/data/admin/Quanliucheng/langfang/src/PAN/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-PAN1.tiff",
"panRefImgs":["/usr/seis/data/admin/Quanliucheng/langfang/REF/langfangmos.img"]
}
    #network.httpService.PostTest(url, json_data)

    # r11 = requests.post(url, data)
    # r11 = requests.post(url, json_data, headers)
    # values_json = json.dumps(json_data)
    # r11 = requests.post(url, values_json, headers)
    #r11 = requests.post(url, data=json.dumps(json_data), headers={'Content-Type': 'application/json'})
    #print(r11.text)

