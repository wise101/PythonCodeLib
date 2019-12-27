#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os

#遍历文件夹搜索tiff文件
def traverse_folder(root_dir,file_list):
    #获取该目录下所有的文件名称和目录名称
    # list = os.listdir(root_dir)  # 列出文件夹下所有的目录与文件
    # for i in range(0, len(list)):
    #     path = os.path.join(root_dir, list[i])
    #     if os.path.isdir(path):
    #         if not path == '.':
    #             traverse_folder(path,file_list)
    #     if os.path.isfile(path):
    #         if not path == '.':
    #             file_list.append(path)
    for item in os.scandir(root_dir):
        if item.path == '.':
            continue
        path = os.path.join(root_dir,item.path)
        if item.is_dir():
              traverse_folder(path,file_list)
        elif item.is_file():
            if os.path.splitext(item.path)[1] == '.tiff':
              file_list.append(item.path)

#遍历文件夹查找指定的文件
#data_folder  --- 数据目录
#file_list    --- 文件数组
#filter_str   --- 过滤字符串
def SearchSpecData(data_folder,file_list,filter_str):
    for item in os.scandir(data_folder):
        if item.path == '.':
            continue
        path = os.path.join(data_folder,item.path)
        if item.is_dir():
              SearchSpecData(path,file_list,filter_str)
        elif item.is_file():
            if (-1!=item.path.find(filter_str) and (os.path.splitext(item.path)[1] == '.tiff')):
                file_list.append(item.path)
