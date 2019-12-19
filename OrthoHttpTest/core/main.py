#!/usr/bin/env python
# -*- coding:utf-8 -*-

# print('hello,world')

#import os,sys
#sys.path.append('...\\util')  # path为你的工程根目录的绝对路径
#sys.path.append("D:\\work\\PythonCodeLib\\OrthoHttpTest\\util")

import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import util.filelib

if __name__ == "__main__":
    #根目录路径
    root_path = r"D:\JavaProject\PIE-SDK-Clouds.git\geo-check-alg\doc"
    #用来存放所有的文件路径
    file_list = []
    #用来存放所有的目录路径
    dir_list = []
    util.filelib.get_file_path(root_path,file_list,dir_list)
    print(file_list)
#   print(dir_list)

