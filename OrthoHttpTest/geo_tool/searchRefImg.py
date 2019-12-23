#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import gdal, osr
import osgeo.gdal
osgeo.gdal.GetDriverByName

def PixelToWorld(adfGeoTransform,lCol, lRow, dblX,dblY):
    dblX = adfGeoTransform[0] + lCol * adfGeoTransform[1] + lRow * adfGeoTransform[2]
    dblY = adfGeoTransform[3] + lCol * adfGeoTransform[4] + lRow * adfGeoTransform[5]

def GetRasterEnv(imgFile):
    dataset = gdal.Open(imgFile)
#   print(imgFile, ' 宽=', dataset.RasterXSize)
    adfGeoTransform = dataset.GetGeoTransform()
    # 左上角地理坐标
    print(adfGeoTransform[0])
    print(adfGeoTransform[3])
    imgWidth = dataset.RasterXSize
    imgHeight = dataset.RasterYSize
    print(imgWidth)
    print(imgHeight)

