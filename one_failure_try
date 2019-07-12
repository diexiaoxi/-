import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from math import radians, cos, sin, asin, sqrt
import json
import urllib.request
import sympy as sy
import scipy as sp
from scipy import optimize
import math

def dataProcess():
    tele_data = pd.read_csv('extract-by-190627.csv')
    print(tele_data.columns)
    latitude = np.array(tele_data['latitude'])
    longitude = np.array(tele_data['longitude'])
    altitude = np.array(tele_data['altitude'])
    lte_rsrp = np.array(tele_data['lte_rsrp'])
    lte_rssnr = np.array(tele_data['lte_rssnr'])
    speed = np.array(tele_data['avg_speed'])


    # 删除无用列
    del tele_data['id']
    del tele_data['area']
    del tele_data['base_station_id']
    del tele_data['create_date']

    # 清洗NaN的行列
    tele_data.dropna(axis=0,how='any')
    # 清洗异常数值
    tele_data = tele_data.drop(tele_data[(tele_data['lte_rsrp']>0) & (tele_data['lte_rsrp']<-180)].index)

    # 给RSRP添加等级
    tele_data['rsrp_level'] = 1
    tele_data.loc[tele_data.lte_rsrp>-65,'rsrp_level'] = '1'
    tele_data.loc[tele_data.lte_rsrp<=-65,'rsrp_level'] = '2'
    tele_data.loc[tele_data.lte_rsrp<=-75,'rsrp_level'] = '3'
    tele_data.loc[tele_data.lte_rsrp<=-85,'rsrp_level'] = '4'
    tele_data.loc[tele_data.lte_rsrp<=-95,'rsrp_level'] = '5'
    tele_data.loc[tele_data.lte_rsrp<=-105,'rsrp_level'] = '6'
    tele_data.to_csv('data_del.csv', header=True)

    #筛选CID
    cid_array = np.array(tele_data['cid'])
    # 筛选cellID
    cid_list =cid_array.tolist()
    cid_unique = np.unique(cid_array)
    cid_unique_num =[] #每次cellID出现次数
    cid_index = [] #记录第一次出现位置

    for i in range(0,len(cid_unique)):
        cid_index = np.append(cid_index,cid_list.index(cid_unique[i]))
        cid_unique_num = np.append(cid_unique_num,cid_list.count(cid_unique[i]))

    return latitude, longitude, altitude, lte_rsrp, cid_array,cid_unique,cid_index,cid_unique_num


def solve_equation(lati, lon, alt, rsrp):
    x_1, x_2, x_3 = sy.symbols("x_1 x_2 x_3")
    eq = []
    for i in range(0, len(lati)):
        lng, lat = map(radians, [lon[i], lati[i]])  # 经纬度转换成弧度
        distance = round(sqrt((2*asin(sqrt((sin((x_1 - lat)/2)**2 + cos(x_2)*cos(lat)*sin((x_2-lng)/2)**2)))*6371*1000)^2 + (alt2-alt1)^2)/1000, 3)
        eq = np.append(43-20*(math.log(distance,10)) - 20*(math.log(2000,10)) + 27.55 - rsrp[i])

    result = sy.nonlinsolve(eq, [x_1, x_2, x_3])
    print(result)

def ModelFitMethod(latitude, longitude, altitude, lte_rsrp, cid_array, cid_unique, cid_index, cid_unique_num):
    # model = 20log(distance) + 20log(frequency) - 27.55
    # 就用最简单的Free space model来匹配
    # 不知道frequency，不过影响不大，可以先假设为2000Mhz（都在这个附近）
    # ModelFitMethod:未知数，解方程
    # 43dBm

    # 保存采样点数>=3个的个数
    cid_index_solvable = []

    #for i in range(0,len(cid_unique_num)):
    for i in range(0, 5):
        if cid_unique_num[i]>2:
            cid_index_solvable = np.append(cid_index_solvable,cid_index[i])

    for j in range(0, len(cid_index_solvable)-1):
        #for k in range(cid_index_solvable[j], cid_index_solvable[j+1]-1):
        solve_equation(lat, log, alt, rsrp)


## 最简单的
#def PLRegression(latitude, longitude, altitude, lte_rsrp, cid_array, cid_unique, cid_index, cid_unique_num):
#    print('latitude:',latitude)
#    print('longitude:',longitude)
#    print('altitude:',altitude)
#    print('lte_rsrp:',lte_rsrp)
#    print('cid_array:',cid_array)
#    print('cid_unique:',cid_unique)
#    print('cid_index:',cid_index)
#    print('cid_unique_num:',cid_unique_num)


if __name__ == '__main__':
    [lat, log, alt, rsrp, cid_original, cid_uni, cid_index,cid_unique_num] = dataProcess()
    ModelFitMethod(lat, log, alt, rsrp, cid_original, cid_uni, cid_index, cid_unique_num)
    #PLRegression(lat,log,alt, rsrp, cid_original, cid_uni, cid_index,cid_unique_num)


# 直接求解
# 失败
# 坐标转换太复杂
