# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/10


import requests, re, os


def getStation():
    #   发送请求获取所有车站名称，通过输入的站名转换为查询地址的参数
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9236'
    response = requests.get(url, verify=True)  # 请求并进行验证
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    stations = dict(stations, indent=4)
    stations = str(stations)
    write(stations)


def write(stations):
    # 写入文件
    file = open('stations.text', 'w', encoding='utf_8_sig')
    file.write(stations)
    file.close


def read():
    # 读取文件，返回文件数据
    file = open('stations.text', 'r', encoding='utf_8_sig')
    data = file.readline()
    file.close()
    return data


def isStations():
    # 判断文件是否存在
    isStations = os.path.exists('stations.text')
    return isStations
