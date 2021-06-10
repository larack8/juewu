# -*- coding:utf-8 -*-
import os

os.system('taskkill /IM scrcpy.exe /F')
os.system('taskkill /IM adb.exe /F')
#       1080*2160
# mine: 1080x2400
# d 0  169     1982  100\nc\nu 0\nc\n
#              1080-y,  x
os.system("scrcpy --max-size 1080")
os.system("scrcpy --bit-rate 8M")
os.system("scrcpy --max-fps 60")
'''
以 (0,0) 为原点的 1224x1440 像素
'''
# os.system("scrcpy --crop 1224:1440:0:0")

# continue_train
# os.system("python continue_train")
