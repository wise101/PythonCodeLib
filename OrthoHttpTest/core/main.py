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
import geo_tool.searchRefImg

if __name__ == "__main__":
    #根目录路径
    root_path = r"D:\work\PythonCodeLib"
#   root_path = r"/home/work/PythonCodeLib"
    #用来存放所有的文件路径
    file_list = []
    #用来存放所有的目录路径
    #dir_list = []
    #util.filelib.traverse_folder(root_path,file_list)
    #print(file_list)
    imgFile = r"D:\TestData\OrthoAlgoTestData\src\GF1_PMS1_E115.7_N38.9_20180409_L1A0003111678_FUSION_GEO.tiff"
    geo_tool.searchRefImg.GetRasterEnv(imgFile)

