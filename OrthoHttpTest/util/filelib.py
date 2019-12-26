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
