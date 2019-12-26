#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import util.filelib
import requests
import json

#全色影像数组和多光谱影像数组配对
def ImagePair(orig_pan_list,orig_mss_list,new_pan_list,new_mss_list):
    for pan_file in orig_pan_list:
        str = pan_file.split('/')[1:]
        panName = str[-1].split('-')[0:]
        for mss_file in orig_mss_list:
            str = mss_file.split('/')[1:]
            mssName = str[-1].split('-')[0:]
            if(panName[0]==mssName[0]):
                new_pan_list.append(pan_file)
                new_mss_list.append(mss_file)
    if(len(new_pan_list)>0 and len(new_pan_list)==len(new_mss_list)):
        return 1
    else:
        return 0

# 搜索文件夹获取文件，包括pan文件夹和mss文件夹
# 构建单个接口的json字符串,包括构建全色数组和多光谱数组，查找相应的基准影像
# 循环调用融合接口
def FuseFlowTest():
    pan_file_list = []
    pan_floder = '/sedata/data/admin/Quanliucheng/langfang/src/PAN'
    util.filelib.traverse_folder(pan_floder, pan_file_list)
    #print(pan_file_list)
    docker_pan_folder = '/usr/seis/data/admin/Quanliucheng/langfang/src/PAN/'
    docker_pan_files = []
    for pan_file in pan_file_list:
        filename = os.path.basename(pan_file)
        docker_pan_files.append(docker_pan_folder+filename)
    print(docker_pan_files)

    mss_file_list = []
    mss_floder = '/sedata/data/admin/Quanliucheng/langfang/src/MSS'
    util.filelib.traverse_folder(mss_floder, mss_file_list)
    #print(mss_file_list)
    docker_mss_folder = '/usr/seis/data/admin/Quanliucheng/langfang/src/MSS/'
    docker_mss_files = []
    for mss_file in mss_file_list:
        filename = os.path.basename(mss_file)
        docker_mss_files.append(docker_mss_folder+filename)
    print(docker_mss_files)

    new_pan_list = []
    new_mss_list = []
    if(1==ImagePair(docker_pan_files, docker_mss_files, new_pan_list, new_mss_list)):
        #print(new_pan_list)
        #print(new_mss_list)
        #构造ortho接口json字符串
        jsonArgument = {}
        jsonArgument["constZ"] = 0
        jsonArgument["demPath"] = "/usr/seis/data/admin/Quanliucheng/langfang/DEM/langfangdem.tif"
        jsonArgument["feedNum"] = 1000
        jsonArgument["similarParm"] = 1
        jsonArgument["rpcError"] = 5.0
        #配置输出文件夹
        outFolder = "/usr/seis/data/admin/Quanliucheng/langfang/out/"
        #配置基准文件
        panRefImgs = ["/usr/seis/data/admin/Quanliucheng/langfang/REF/langfangmos.img"]
        for i in range(0, len(new_pan_list)):
            fileName = os.path.basename(new_pan_list[i])
            fuseFile = os.path.splitext(fileName)[0] + "_fuse.tiff"
            jsonArgument["imgFusePath"] = outFolder+fuseFile
            jsonArgument["panPath"] = new_pan_list[i]
            jsonArgument["panOrthoPath"] = outFolder + fileName
            mssFileName = os.path.basename(new_mss_list[i])
            jsonArgument["mssPath"] = new_mss_list[i]
            jsonArgument["mssOrthoPath"] = outFolder + mssFileName
            jsonArgument["panRefImgs"] = panRefImgs
            jsonArgument["orthoMssRes"] = 0.00008
            jsonArgument["orthoPanRes"] = 0.00002
            jsonArgument["orthoWKT"] = ""
        url = "http://172.16.40.54:6060/ortho/api/v1/rawdata/fuse"
        # 转换成json字符串
        json_str = json.dumps(jsonArgument)
        print(json_str)
        r11 = requests.post(url, data=json_str,headers={'Content-Type': 'application/json'})
        print(r11.text)
