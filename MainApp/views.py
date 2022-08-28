from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import date, datetime

# Thông tin OpenWeatherMap API
key = '302073f21c30d848ba9729abb90090fe'

# Get Url
URL = 'https://api.openweathermap.org/data/2.5/onecall'


# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')


# An Giang
def angiang(request):
    # ==================DỮ LIỆU THỜI TIẾT TỈNH AN GIANG CÓ longitude: 105.125896 và latitude: 10.521584 =============
    PARAM = {'lat': '10.521584', 'lon': '105.125896',
             'exclude': 'hourly', 'appid': key, 'lang': 'vi', 'units':'metric'}
    # Chuyển sang dạng JSON
    r = requests.get(url=URL, params=PARAM)
    res = r.json()

    nhietDoHienTai = res['current']['temp']
    nhietDoCaoNhat = res['daily'][0]['temp']['max']
    nhietDoThapNhat = res['daily'][0]['temp']['min']
    tinhTrangThoiTiet = res['current']['weather'][0]['description']
    icon = res['current']['weather'][0]['icon']
    tocDoGio = res['current']['wind_speed']

    # Get dữ liệu các mảng
    icon1 = res['daily'][1]['weather'][0]['icon']
    icon2 = res['daily'][2]['weather'][0]['icon']
    icon3 = res['daily'][3]['weather'][0]['icon']
    icon4 = res['daily'][4]['weather'][0]['icon']
    icon5 = res['daily'][5]['weather'][0]['icon']
    icon6 = res['daily'][6]['weather'][0]['icon']

    nhietDo1 = res['daily'][1]['temp']['day']
    nhietDo2 = res['daily'][2]['temp']['day']
    nhietDo3 = res['daily'][3]['temp']['day']
    nhietDo4 = res['daily'][4]['temp']['day']
    nhietDo5 = res['daily'][5]['temp']['day']
    nhietDo6 = res['daily'][6]['temp']['day']

    thoiGian1 = res['daily'][1]['dt']
    thoiGian2 = res['daily'][2]['dt']
    thoiGian3 = res['daily'][3]['dt']
    thoiGian4 = res['daily'][4]['dt']
    thoiGian5 = res['daily'][5]['dt']
    thoiGian6 = res['daily'][6]['dt']

    # Chuyển đổi dữ liệu

    thoiGianHienTai = res['current']['dt']
    timeHienTai = datetime.fromtimestamp(
        thoiGianHienTai).strftime('%H:%M:%S %d-%m-%Y')

    time1 = datetime.fromtimestamp(thoiGian1).strftime('%d-%m-%Y')
    time2 = datetime.fromtimestamp(thoiGian2).strftime('%d-%m-%Y')
    time3 = datetime.fromtimestamp(thoiGian3).strftime('%d-%m-%Y')
    time4 = datetime.fromtimestamp(thoiGian4).strftime('%d-%m-%Y')
    time5 = datetime.fromtimestamp(thoiGian5).strftime('%d-%m-%Y')
    time6 = datetime.fromtimestamp(thoiGian6).strftime('%d-%m-%Y')

    time11 = datetime.fromtimestamp(thoiGian1).strftime('%d')
    time22 = datetime.fromtimestamp(thoiGian2).strftime('%d')
    time33 = datetime.fromtimestamp(thoiGian3).strftime('%d')
    time44 = datetime.fromtimestamp(thoiGian4).strftime('%d')
    time55 = datetime.fromtimestamp(thoiGian5).strftime('%d')
    time66 = datetime.fromtimestamp(thoiGian6).strftime('%d')

    # Độ ẩm
    doAmHienTai = res['current']['humidity']

    doAm1n = res['daily'][1]['humidity']
    doAm2n = res['daily'][2]['humidity']
    doAm3n = res['daily'][3]['humidity']
    doAm4n = res['daily'][4]['humidity']
    doAm5n = res['daily'][5]['humidity']
    doAm6n = res['daily'][6]['humidity']

    trong = 100 - doAmHienTai
    data = [doAmHienTai, trong]

    time5Ngay = [0, time11, time22, time33, time44, time55, time66]
    doAm5Ngay = [0, doAm1n, doAm2n, doAm3n, doAm4n, doAm5n, doAm6n]

    # Kiểm tra ngoại lệ tồn tại mưa hay không
    try:
        luongMua = res['current']['rain']['1h']
    except:
        luongMua = 0.0


    try:
        luongMua1 = res['daily'][1]['rain']
    except:
        luongMua1= 0.0
    
    try:
        luongMua2 = res['daily'][2]['rain']
    except:
        luongMua2= 0.0
        
    try:
        luongMua3 = res['daily'][3]['rain']
    except:
        luongMua3= 0.0
        
    try:
        luongMua4 = res['daily'][4]['rain']
    except:
        luongMua4= 0.0
        
    try:
        luongMua5 = res['daily'][5]['rain']
    except:
        luongMua5= 0.0
        
    try:
        luongMua6 = res['daily'][6]['rain']
    except:
        luongMua6= 0.0
        
    luongMua6Ngay = [luongMua1, luongMua2, luongMua3, luongMua4, luongMua5, luongMua6]
    time6Ngay = [time11, time22, time33, time44, time55, time66]

    # Trả dữ liệu sang giao diện
    return render(request, "MainApp/angiang.html", {
        'nhietDoHienTai': int(nhietDoHienTai),
        'nhietDoCaoNhat': int(nhietDoCaoNhat),
        'nhietDoThapNhat': int(nhietDoThapNhat),
        'tocDoGio': tocDoGio,
        'tinhTrangThoiTiet': tinhTrangThoiTiet,
        'luongMua': luongMua,
        'icon': icon,
        'timeHienTai': timeHienTai,

        'icon1': icon1,
        'icon2': icon2,
        'icon3': icon3,
        'icon4': icon4,
        'icon5': icon5,
        'icon6': icon6,

        'nhietDo1': int(nhietDo1),
        'nhietDo2': int(nhietDo2),
        'nhietDo3': int(nhietDo3),
        'nhietDo4': int(nhietDo4),
        'nhietDo5': int(nhietDo5),
        'nhietDo6': int(nhietDo6),

        'time1': time1,
        'time2': time2,
        'time3': time3,
        'time4': time4,
        'time5': time5,
        'time6': time6,

        'data': data,
        'doAmHienTai': doAmHienTai,
        'time5Ngay': time5Ngay,
        'doAm5Ngay': doAm5Ngay,
        'luongMua6Ngay': luongMua6Ngay,
        'time6Ngay': time6Ngay
    })

# Tiền Giang


def tiengiang(request):
    # ==================DỮ LIỆU THỜI TIẾT TỈNH TIỀN GIANG CÓ longitude: 106.342050 và latitude: 10.449332 =============
    PARAM = {'lat': '10.449332', 'lon': '106.342050',
             'exclude': 'hourly', 'appid': key, 'lang': 'vi', 'units':'metric'}
    # Chuyển sang dạng JSON
    r = requests.get(url=URL, params=PARAM)
    res = r.json()

    nhietDoHienTai = res['current']['temp']
    nhietDoCaoNhat = res['daily'][0]['temp']['max']
    nhietDoThapNhat = res['daily'][0]['temp']['min']
    tinhTrangThoiTiet = res['current']['weather'][0]['description']
    icon = res['current']['weather'][0]['icon']
    tocDoGio = res['current']['wind_speed']

    # Get dữ liệu các mảng
    icon1 = res['daily'][1]['weather'][0]['icon']
    icon2 = res['daily'][2]['weather'][0]['icon']
    icon3 = res['daily'][3]['weather'][0]['icon']
    icon4 = res['daily'][4]['weather'][0]['icon']
    icon5 = res['daily'][5]['weather'][0]['icon']
    icon6 = res['daily'][6]['weather'][0]['icon']

    nhietDo1 = res['daily'][1]['temp']['day']
    nhietDo2 = res['daily'][2]['temp']['day']
    nhietDo3 = res['daily'][3]['temp']['day']
    nhietDo4 = res['daily'][4]['temp']['day']
    nhietDo5 = res['daily'][5]['temp']['day']
    nhietDo6 = res['daily'][6]['temp']['day']

    thoiGian1 = res['daily'][1]['dt']
    thoiGian2 = res['daily'][2]['dt']
    thoiGian3 = res['daily'][3]['dt']
    thoiGian4 = res['daily'][4]['dt']
    thoiGian5 = res['daily'][5]['dt']
    thoiGian6 = res['daily'][6]['dt']

    # Chuyển đổi dữ liệu
    thoiGianHienTai = res['current']['dt']
    timeHienTai = datetime.fromtimestamp(
        thoiGianHienTai).strftime('%H:%M:%S %d-%m-%Y')

    time1 = datetime.fromtimestamp(thoiGian1).strftime('%d-%m-%Y')
    time2 = datetime.fromtimestamp(thoiGian2).strftime('%d-%m-%Y')
    time3 = datetime.fromtimestamp(thoiGian3).strftime('%d-%m-%Y')
    time4 = datetime.fromtimestamp(thoiGian4).strftime('%d-%m-%Y')
    time5 = datetime.fromtimestamp(thoiGian5).strftime('%d-%m-%Y')
    time6 = datetime.fromtimestamp(thoiGian6).strftime('%d-%m-%Y')

    time11 = datetime.fromtimestamp(thoiGian1).strftime('%d')
    time22 = datetime.fromtimestamp(thoiGian2).strftime('%d')
    time33 = datetime.fromtimestamp(thoiGian3).strftime('%d')
    time44 = datetime.fromtimestamp(thoiGian4).strftime('%d')
    time55 = datetime.fromtimestamp(thoiGian5).strftime('%d')
    time66 = datetime.fromtimestamp(thoiGian6).strftime('%d')

    # Độ ẩm
    doAmHienTai = res['current']['humidity']

    doAm1n = res['daily'][1]['humidity']
    doAm2n = res['daily'][2]['humidity']
    doAm3n = res['daily'][3]['humidity']
    doAm4n = res['daily'][4]['humidity']
    doAm5n = res['daily'][5]['humidity']
    doAm6n = res['daily'][6]['humidity']

    trong = 100 - doAmHienTai
    data = [doAmHienTai, trong]

    time5Ngay = [0, time11, time22, time33, time44, time55, time66]
    doAm5Ngay = [0, doAm1n, doAm2n, doAm3n, doAm4n, doAm5n, doAm6n]

    # Kiểm tra ngoại lệ tồn tại mưa hay không
    try:
        luongMua = res['current']['rain']['1h']
    except:
        luongMua = 0.0
        
        
    try:
        luongMua1 = res['daily'][1]['rain']
        luongMua2 = res['daily'][2]['rain']
        luongMua3 = res['daily'][3]['rain']
        luongMua4 = res['daily'][4]['rain']
        luongMua5 = res['daily'][5]['rain']
        luongMua6 = res['daily'][6]['rain']
    except:
        luongMua1 = luongMua2 = luongMua3 = luongMua4 = luongMua5 = luongMua6 = 0.0
        
    luongMua6Ngay = [luongMua1, luongMua2, luongMua3, luongMua4, luongMua5, luongMua6]
    time6Ngay = [time11, time22, time33, time44, time55, time66]

    return render(request, "MainApp/tiengiang.html", {
        'nhietDoHienTai': int(nhietDoHienTai),
        'nhietDoCaoNhat': int(nhietDoCaoNhat),
        'nhietDoThapNhat': int(nhietDoThapNhat),
        'tocDoGio': tocDoGio,
        'tinhTrangThoiTiet': tinhTrangThoiTiet,
        'luongMua': luongMua,
        'icon': icon,
        'timeHienTai': timeHienTai,

        'icon1': icon1,
        'icon2': icon2,
        'icon3': icon3,
        'icon4': icon4,
        'icon5': icon5,
        'icon6': icon6,

        'nhietDo1': int(nhietDo1),
        'nhietDo2': int(nhietDo2),
        'nhietDo3': int(nhietDo3),
        'nhietDo4': int(nhietDo4),
        'nhietDo5': int(nhietDo5),
        'nhietDo6': int(nhietDo6),

        'time1': time1,
        'time2': time2,
        'time3': time3,
        'time4': time4,
        'time5': time5,
        'time6': time6,

        'data': data,
        'doAmHienTai': doAmHienTai,
        'time5Ngay': time5Ngay,
        'doAm5Ngay': doAm5Ngay,
        
        'luongMua6Ngay': luongMua6Ngay,
        'time6Ngay': time6Ngay
    })


# Sóc Trăng
def soctrang(request):
    # ==================DỮ LIỆU THỜI TIẾT TỈNH SÓC TRĂNG CÓ longitude: 105.959954 và latitude: 9.600369 =============
    PARAM = {'lat': '9.600369', 'lon': '105.959954',
             'exclude': 'hourly', 'appid': key, 'lang': 'vi', 'units':'metric'}
    # Chuyển sang dạng JSON
    r = requests.get(url=URL, params=PARAM)
    res = r.json()

    nhietDoHienTai = res['current']['temp']
    nhietDoCaoNhat = res['daily'][0]['temp']['max']
    nhietDoThapNhat = res['daily'][0]['temp']['min']
    tinhTrangThoiTiet = res['current']['weather'][0]['description']
    icon = res['current']['weather'][0]['icon']
    tocDoGio = res['current']['wind_speed']

    # Get dữ liệu các mảng
    icon1 = res['daily'][1]['weather'][0]['icon']
    icon2 = res['daily'][2]['weather'][0]['icon']
    icon3 = res['daily'][3]['weather'][0]['icon']
    icon4 = res['daily'][4]['weather'][0]['icon']
    icon5 = res['daily'][5]['weather'][0]['icon']
    icon6 = res['daily'][6]['weather'][0]['icon']

    nhietDo1 = res['daily'][1]['temp']['day']
    nhietDo2 = res['daily'][2]['temp']['day']
    nhietDo3 = res['daily'][3]['temp']['day']
    nhietDo4 = res['daily'][4]['temp']['day']
    nhietDo5 = res['daily'][5]['temp']['day']
    nhietDo6 = res['daily'][6]['temp']['day']

    thoiGian1 = res['daily'][1]['dt']
    thoiGian2 = res['daily'][2]['dt']
    thoiGian3 = res['daily'][3]['dt']
    thoiGian4 = res['daily'][4]['dt']
    thoiGian5 = res['daily'][5]['dt']
    thoiGian6 = res['daily'][6]['dt']

    # Chuyển đổi dữ liệu

    thoiGianHienTai = res['current']['dt']
    timeHienTai = datetime.fromtimestamp(
        thoiGianHienTai).strftime('%H:%M:%S %d-%m-%Y')

    time1 = datetime.fromtimestamp(thoiGian1).strftime('%d-%m-%Y')
    time2 = datetime.fromtimestamp(thoiGian2).strftime('%d-%m-%Y')
    time3 = datetime.fromtimestamp(thoiGian3).strftime('%d-%m-%Y')
    time4 = datetime.fromtimestamp(thoiGian4).strftime('%d-%m-%Y')
    time5 = datetime.fromtimestamp(thoiGian5).strftime('%d-%m-%Y')
    time6 = datetime.fromtimestamp(thoiGian6).strftime('%d-%m-%Y')

    time11 = datetime.fromtimestamp(thoiGian1).strftime('%d')
    time22 = datetime.fromtimestamp(thoiGian2).strftime('%d')
    time33 = datetime.fromtimestamp(thoiGian3).strftime('%d')
    time44 = datetime.fromtimestamp(thoiGian4).strftime('%d')
    time55 = datetime.fromtimestamp(thoiGian5).strftime('%d')
    time66 = datetime.fromtimestamp(thoiGian6).strftime('%d')

    # Độ ẩm
    doAmHienTai = res['current']['humidity']

    doAm1n = res['daily'][1]['humidity']
    doAm2n = res['daily'][2]['humidity']
    doAm3n = res['daily'][3]['humidity']
    doAm4n = res['daily'][4]['humidity']
    doAm5n = res['daily'][5]['humidity']
    doAm6n = res['daily'][6]['humidity']

    trong = 100 - doAmHienTai
    data = [doAmHienTai, trong]

    time5Ngay = [0, time11, time22, time33, time44, time55, time66]
    doAm5Ngay = [0, doAm1n, doAm2n, doAm3n, doAm4n, doAm5n, doAm6n]

    # Kiểm tra ngoại lệ tồn tại mưa hay không
    try:
        luongMua = res['current']['rain']['1h']
    except:
        luongMua = 0.0


    try:
        luongMua1 = res['daily'][1]['rain']
    except:
        luongMua1= 0.0
    
    try:
        luongMua2 = res['daily'][2]['rain']
    except:
        luongMua2= 0.0
        
    try:
        luongMua3 = res['daily'][3]['rain']
    except:
        luongMua3= 0.0
        
    try:
        luongMua4 = res['daily'][4]['rain']
    except:
        luongMua4= 0.0
        
    try:
        luongMua5 = res['daily'][5]['rain']
    except:
        luongMua5= 0.0
        
    try:
        luongMua6 = res['daily'][6]['rain']
    except:
        luongMua6= 0.0
        
    luongMua6Ngay = [luongMua1, luongMua2, luongMua3, luongMua4, luongMua5, luongMua6]
    time6Ngay = [time11, time22, time33, time44, time55, time66]
    
    
    return render(request, "MainApp/soctrang.html", {
        'nhietDoHienTai': int(nhietDoHienTai),
        'nhietDoCaoNhat': int(nhietDoCaoNhat),
        'nhietDoThapNhat': int(nhietDoThapNhat),
        'tocDoGio': tocDoGio,
        'tinhTrangThoiTiet': tinhTrangThoiTiet,
        'luongMua': luongMua,
        'icon': icon,
        'timeHienTai': timeHienTai,

        'icon1': icon1,
        'icon2': icon2,
        'icon3': icon3,
        'icon4': icon4,
        'icon5': icon5,
        'icon6': icon6,

        'nhietDo1': int(nhietDo1),
        'nhietDo2': int(nhietDo2),
        'nhietDo3': int(nhietDo3),
        'nhietDo4': int(nhietDo4),
        'nhietDo5': int(nhietDo5),
        'nhietDo6': int(nhietDo6),

        'time1': time1,
        'time2': time2,
        'time3': time3,
        'time4': time4,
        'time5': time5,
        'time6': time6,

        'data': data,
        'doAmHienTai': doAmHienTai,
        'time5Ngay': time5Ngay,
        'doAm5Ngay': doAm5Ngay,
        'luongMua6Ngay': luongMua6Ngay,
        'time6Ngay': time6Ngay
    })
