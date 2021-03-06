#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import gdal, osr
import osgeo.gdal
osgeo.gdal.GetDriverByName

import ctypes
from ctypes import *

import util.filelib

class Point:
      ptX = 0.0
      ptY = 0.0

# 栅格地理范围类
class RasterEnv:
    MinX = 0.0
    MinY = 0.0
    MaxX = 0.0
    MaxY = 0.0

    # 定义构造方法
    # def __init__(self, min_x, min_y, max_x,max_y):
    #     self.MinX = min_x

# def Intersects(env1,env2):
#     return env1.MinX <= env2.MaxX and env1.MaxX >= env2.MinX and env1.MinY <= env2.MaxY and env1.MaxY >= env2.MinY

def ImgIntersects(filePath1,filePath2):
    lib = ctypes.CDLL("/home/work/GeoTool/src/OutDir/centos7_x64_release/CoordinateTransform.so")
    imgPath1 = bytes(filePath1, encoding='utf-8')
    imgPath2 = bytes(filePath2, encoding='utf-8')
    return lib.IsImgIntersect(imgPath1,imgPath2)

def PixelToWorld(adfGeoTransform,lCol, lRow, pt):
    #pt = Point()
    pt.ptX = adfGeoTransform[0] + lCol * adfGeoTransform[1] + lRow * adfGeoTransform[2]
    pt.ptY = adfGeoTransform[3] + lCol * adfGeoTransform[4] + lRow * adfGeoTransform[5]

def GetRasterEnv(imgFile,env):
    #print(imgFile)
    #gdal.UseExceptions()
    dataset = gdal.Open(imgFile)

    if(dataset is None):
        print('open image file failed')
        return
#   print(imgFile, ' 宽=', dataset.RasterXSize)

    # 左上角地理坐标
    #print(adfGeoTransform[0])
    #print(adfGeoTransform[3])
    else:
        #print(dataset.GetMetadata())
        #return
        # adfGeoTransform = dataset.GetGeoTransform()
        # lWidth = dataset.RasterXSize
        # lHeight = dataset.RasterYSize
        # dbX = [0.0, 0.0, 0.0, 0.0]
        # dbY = [0.0, 0.0, 0.0, 0.0]
        # pt = Point()
        # PixelToWorld(adfGeoTransform, 0, 0, pt) # 左上角坐标
        # dbX[0] = pt.ptX
        # dbY[0] = pt.ptY
        # PixelToWorld(adfGeoTransform, lWidth, 0,pt )  #  右上角坐标
        # dbX[1] = pt.ptX
        # dbY[1] = pt.ptY
        # PixelToWorld(adfGeoTransform, lWidth, lHeight, pt) # 右下角点坐标
        # dbX[2] = pt.ptX
        # dbY[2] = pt.ptY
        # PixelToWorld(adfGeoTransform, 0, lHeight,pt) # 左下角坐标
        # dbX[3] = pt.ptX
        # dbY[3] = pt.ptY

        lib = ctypes.CDLL("D:\\work\\GeoTool\\src\\OutDir\\Debug_x64\\CoordinateTransform.dll")

        INPUT = c_double * 4
        dbX = INPUT()
        dbY = INPUT()
        for i in range(4):
            dbX[i] = 0.0
            dbY[i] = 0.0

        imgPath = bytes(imgFile, encoding='utf-8')
        lib.GetRasterEnv(imgPath, dbX, dbY)

        env.MinX = min(min(min(dbX[0], dbX[1]), dbX[2]), dbX[3])
        env.MaxX = max(max(max(dbX[0], dbX[1]), dbX[2]), dbX[3])
        env.MinY = min(min(min(dbY[0], dbY[1]), dbY[2]), dbY[3])
        env.MaxY = max(max(max(dbY[0], dbY[1]), dbY[2]), dbY[3])

#def ImgIntersects(file1,file2):
    # env1 = RasterEnv()
    # env2 = RasterEnv()
    # GetRasterEnv(file1, env1)
    # print(env1.MinX)
    # print(env1.MaxX)
    # print(env1.MinY)
    # print(env1.MaxY)
    # GetRasterEnv(file2, env2)
    # print(env2.MinX)
    # print(env2.MaxX)
    # print(env2.MinY)
    # print(env2.MaxY)
    # if(1==Intersects(env1, env2)):
    #     print('intersect')
    #     return 1
    # else:
    #     print('no intersect')
    #     return 0



#imgFile        --- 影像文件路径
#ref_folder     --- 基准文件夹
#ref_list       --- 输出参数：基准数组
# def GetRefData(imgFile,ref_folder,ref_list):
#     env = RasterEnv()
#     GetRasterEnv(imgFile, env)
#     file_ext = '.tif'
#     all_ref_list = []
#     util.filelib.traverse_folder(ref_folder, all_ref_list, file_ext)
#     if(0==len(all_ref_list)):
#          return 0
#
#     envRef = RasterEnv()
#     for i in range(0, len(all_ref_list)):
#         GetRasterEnv(all_ref_list[i], envRef)
#         if(Intersects(env,envRef)>0):
#             ref_list.append(all_ref_list[i])