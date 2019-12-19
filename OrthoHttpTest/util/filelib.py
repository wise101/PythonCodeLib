#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os

def get_file_path(root_path,file_list,dir_list):
    #获取该目录下所有的文件名称和目录名称
    # dir_or_files = os.listdir(root_path)
    # for dir_file in dir_or_files:
    #     #获取目录或者文件的路径
    #     dir_file_path = os.path.join(root_path,dir_file)
    #     #判断该路径为文件还是路径
    #     if os.path.isdir(dir_file_path):
    #         dir_list.append(dir_file_path)
    #         #递归获取所有文件和目录的路径
    #         get_file_path(dir_file_path,file_list,dir_list)
    #     else:
    #         file_list.append(dir_file_path)
    for root, dirs, files in os.walk(root_path):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        # use files and dirs
        for file_name in files:
            dir_file_path = os.path.join(root_path, file_name)
                #判断该路径为文件还是路径
            if os.path.isdir(dir_file_path):
                dir_list.append(dir_file_path)
                #递归获取所有文件和目录的路径
                get_file_path(dir_file_path,file_list,dir_list)
            else:
                file_list.append(dir_file_path)