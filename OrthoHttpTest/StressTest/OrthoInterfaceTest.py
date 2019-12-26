#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import util.filelib

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
        print(new_pan_list)
        print(new_mss_list)