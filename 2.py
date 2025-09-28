import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimSun']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

m = [
    [80.0, 55.0, 35.0, 72.0, 68.0, 55.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [60.0, 46.0, 40.0, 28.0, 25.0, 86.0, 55.0, 44.0, 50.0, 25.0, 60.0, 45.0, 35.0, 20.0, 0, 0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0],
    [15.0, 13.0, 15.0, 18.0, 27.0, 20.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [15.0, 10.0, 14.0, 6.0, 10.0, 12.0, 22.0, 20.0, 0, 0, 0, 0, 0, 0, 0, 0],
    [15.0, 10.0, 14.0, 6.0, 10.0, 12.0, 22.0, 20.0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
    [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
    [0.6, 0.6, 0.6, 0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.6, 0.6, 0.6, 0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]#第j种土地类型的第k块土地的面积

m = np.array(m)
w_sales = [
    57000, 21850, 22400, 33040, 9875, 170840, 132750, 71400, 30000, 12500,
    1500, 35100, 36000, 14000, 10000, 21000, 36240, 26880, 6240, 30000,
    36210, 45360, 900, 2610, 3480, 3930, 4500, 35480, 13050, 2850,
    1200, 3300, 1620, 1800, 150000, 100000, 36000, 9000, 7200, 18000, 4200
]#2023年41种农作物的产量，单位为斤
w_sales = np.array(w_sales)
a = [[1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]] #41种农作物i，能不能种在第j种土地类型上
a = np.array(a)
P = [[3.25, 0.0, 3.25, 0.0, 3.25, 0.0, 0, 0, 0, 0, 0, 0],
  [7.5, 0.0, 7.5, 0.0, 7.5, 0.0, 0, 0, 0, 0, 0, 0],
  [8.25, 0.0, 8.25, 0.0, 8.25, 0.0, 0, 0, 0, 0, 0, 0],
  [7.0, 0.0, 7.0, 0.0, 7.0, 0.0, 0, 0, 0, 0, 0, 0],
  [6.75, 0.0, 6.75, 0.0, 6.75, 0.0, 0, 0, 0, 0, 0, 0],
  [3.5, 0.0, 3.5, 0.0, 3.5, 0.0, 0, 0, 0, 0, 0, 0],
  [3.0, 0.0, 3.0, 0.0, 3.0, 0.0, 0, 0, 0, 0, 0, 0],
  [6.75, 0.0, 6.75, 0.0, 6.75, 0.0, 0, 0, 0, 0, 0, 0],
  [6.0, 0.0, 6.0, 0.0, 6.0, 0.0, 0, 0, 0, 0, 0, 0],
  [7.5, 0.0, 7.5, 0.0, 7.5, 0.0, 0, 0, 0, 0, 0, 0],
  [40.0, 0.0, 40.0, 0.0, 40.0, 0.0, 0, 0, 0, 0, 0, 0],
  [1.5, 0.0, 1.5, 0.0, 1.5, 0.0, 0, 0, 0, 0, 0, 0],
  [3.25, 0.0, 3.25, 0.0, 3.25, 0.0, 0, 0, 0, 0, 0, 0],
  [5.5, 0.0, 5.5, 0.0, 5.5, 0.0, 0, 0, 0, 0, 0, 0],
  [3.5, 0.0, 3.5, 0.0, 3.5, 0.0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 7.0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 8.0, 0, 8.0, 0, 8.0, 9.6],
  [0, 0, 0, 0, 0, 0, 6.75, 0, 6.75, 0, 6.75, 8.1],
  [0, 0, 0, 0, 0, 0, 6.5, 0, 6.5, 0, 6.5, 7.8],
  [0, 0, 0, 0, 0, 0, 3.75, 0, 3.75, 0, 3.75, 4.5],
  [0, 0, 0, 0, 0, 0, 6.25, 0, 6.25, 0, 6.25, 7.5],
  [0, 0, 0, 0, 0, 0, 5.5, 0, 5.5, 0, 5.5, 6.6],
  [0, 0, 0, 0, 0, 0, 5.75, 0, 5.75, 0, 5.75, 6.9],
  [0, 0, 0, 0, 0, 0, 5.25, 0, 5.25, 0, 5.25, 6.8],
  [0, 0, 0, 0, 0, 0, 5.5, 0, 5.5, 0, 5.5, 6.6],
  [0, 0, 0, 0, 0, 0, 6.5, 0, 6.5, 0, 6.5, 7.8],
  [0, 0, 0, 0, 0, 0, 5.0, 0, 5.0, 0, 5.0, 6.0],
  [0, 0, 0, 0, 0, 0, 5.75, 0, 5.75, 0, 5.75, 6.9],
  [0, 0, 0, 0, 0, 0, 7.0, 0, 7.0, 0, 7.0, 8.4],
  [0, 0, 0, 0, 0, 0, 5.25, 0, 5.25, 0, 5.25, 6.3],
  [0, 0, 0, 0, 0, 0, 7.25, 0, 7.25, 0, 7.25, 8.7],
  [0, 0, 0, 0, 0, 0, 4.5, 0, 4.5, 0, 4.5, 5.4],
  [0, 0, 0, 0, 0, 0, 4.5, 0, 4.5, 0, 4.5, 5.4],
  [0, 0, 0, 0, 0, 0, 4.0, 0, 4.0, 0, 4.0, 4.8],
  [0, 0, 0, 0, 0, 0, 0, 2.5, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 2.5, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 3.25, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 57.5, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 19.0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 16.0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 100.0, 0, 0]]#第i种农作物在第j种土地类型上的销售价格
P=np.array(P)
C = [[400, 0, 400, 0, 400, 0, 0, 0, 0, 0, 0, 0],
  [400, 0, 400, 0, 400, 0, 0, 0, 0, 0, 0, 0],
  [350, 0, 350, 0, 350, 0, 0, 0, 0, 0, 0, 0],
  [350, 0, 350, 0, 350, 0, 0, 0, 0, 0, 0, 0],
  [350, 0, 350, 0, 350, 0, 0, 0, 0, 0, 0, 0],
  [450, 0, 450, 0, 450, 0, 0, 0, 0, 0, 0, 0],
  [500, 0, 500, 0, 500, 0, 0, 0, 0, 0, 0, 0],
  [360, 0, 360, 0, 360, 0, 0, 0, 0, 0, 0, 0],
  [400, 0, 400, 0, 400, 0, 0, 0, 0, 0, 0, 0],
  [360, 0, 360, 0, 360, 0, 0, 0, 0, 0, 0, 0],
  [350, 0, 350, 0, 350, 0, 0, 0, 0, 0, 0, 0],
  [1000, 0, 1000, 0, 1000, 0, 0, 0, 0, 0, 0, 0],
  [2000, 0, 2000, 0, 2000, 0, 0, 0, 0, 0, 0, 0],
  [400, 0, 400, 0, 400, 0, 0, 0, 0, 0, 0, 0],
  [350, 0, 350, 0, 350, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 680, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2400, 0, 2400, 2640],
  [0, 0, 0, 0, 0, 0, 1000, 0, 1200, 0, 1200, 1320],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2400, 0, 2400, 2640],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2400, 0, 2400, 2640],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2400, 0, 2400, 2640],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2400, 0, 2400, 2640],
  [0, 0, 0, 0, 0, 0, 2300, 0, 2700, 0, 2700, 3000],
  [0, 0, 0, 0, 0, 0, 1600, 0, 2000, 0, 2000, 2200],
  [0, 0, 0, 0, 0, 0, 2400, 0, 3000, 0, 3000, 3300],
  [0, 0, 0, 0, 0, 0, 2900, 0, 3500, 0, 3500, 3850],
  [0, 0, 0, 0, 0, 0, 1600, 0, 2000, 0, 2000, 2200],
  [0, 0, 0, 0, 0, 0, 1600, 0, 2000, 0, 2000, 2200],
  [0, 0, 0, 0, 0, 0, 2900, 0, 3500, 0, 3500, 3850],
  [0, 0, 0, 0, 0, 0, 1600, 0, 2000, 0, 2000, 2200],
  [0, 0, 0, 0, 0, 0, 1000, 0, 1200, 0, 1200, 1300],
  [0, 0, 0, 0, 0, 0, 4100, 0, 5000, 0, 5000, 5500],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2500, 0, 2500, 2750],
  [0, 0, 0, 0, 0, 0, 900, 0, 1100, 0, 1100, 1200],
  [0, 0, 0, 0, 0, 0, 0, 2000, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 500, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 500, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 3000, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2000, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 0, 0]]#第i种农作物在第j种土地类型上的成本
C = np.array(C)
l = [[400, 0, 380, 0, 360, 0, 0, 0, 0, 0, 0, 0],
  [500, 0, 475, 0, 450, 0, 0, 0, 0, 0, 0, 0],
  [400, 0, 380, 0, 360, 0, 0, 0, 0, 0, 0, 0],
  [350, 0, 330, 0, 315, 0, 0, 0, 0, 0, 0, 0],
  [415, 0, 395, 0, 375, 0, 0, 0, 0, 0, 0, 0],
  [800, 0, 760, 0, 720, 0, 0, 0, 0, 0, 0, 0],
  [1000, 0, 950, 0, 900, 0, 0, 0, 0, 0, 0, 0],
  [400, 0, 380, 0, 360, 0, 0, 0, 0, 0, 0, 0],
  [630, 0, 600, 0, 570, 0, 0, 0, 0, 0, 0, 0],
  [525, 0, 500, 0, 475, 0, 0, 0, 0, 0, 0, 0],
  [110, 0, 105, 0, 100, 0, 0, 0, 0, 0, 0, 0],
  [3000, 0, 2850, 0, 2700, 0, 0, 0, 0, 0, 0, 0],
  [2200, 0, 2100, 0, 2000, 0, 0, 0, 0, 0, 0, 0],
  [420, 0, 400, 0, 380, 0, 0, 0, 0, 0, 0, 0],
  [525, 0, 500, 0, 475, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 500, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 3000, 0, 3600, 0, 3600, 3200],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2400, 0, 2400, 2200],
  [0, 0, 0, 0, 0, 0, 3000, 0, 3600, 0, 3600, 3200],
  [0, 0, 0, 0, 0, 0, 2000, 0, 2400, 0, 2400, 2200],
  [0, 0, 0, 0, 0, 0, 2400, 0, 3000, 0, 3000, 2700],
  [0, 0, 0, 0, 0, 0, 6400, 0, 8000, 0, 8000, 7200],
  [0, 0, 0, 0, 0, 0, 2700, 0, 3300, 0, 3300, 3000],
  [0, 0, 0, 0, 0, 0, 2400, 0, 3000, 0, 3000, 2700],
  [0, 0, 0, 0, 0, 0, 3300, 0, 4000, 0, 4000, 3600],
  [0, 0, 0, 0, 0, 0, 3700, 0, 4500, 0, 4500, 4100],
  [0, 0, 0, 0, 0, 0, 4100, 0, 5000, 0, 5000, 4500],
  [0, 0, 0, 0, 0, 0, 3200, 0, 4000, 0, 4000, 3600],
  [0, 0, 0, 0, 0, 0, 12000, 0, 15000, 0, 15000, 13500],
  [0, 0, 0, 0, 0, 0, 4100, 0, 5000, 0, 5000, 4500],
  [0, 0, 0, 0, 0, 0, 1600, 0, 2000, 0, 2000, 1800],
  [0, 0, 0, 0, 0, 0, 10000, 0, 12000, 0, 12000, 11000],
  [0, 0, 0, 0, 0, 0, 5000, 0, 6000, 0, 6000, 5400],
  [0, 0, 0, 0, 0, 0, 5500, 0, 6600, 0, 6600, 6000],
  [0, 0, 0, 0, 0, 0, 0, 5000, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 4000, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 3000, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 5000, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 4000, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000, 0, 0]]#第i种农作物在第j种土地类型上的亩产量，单位为亩/斤
l=np.array(l)
T = [365.0, 0.0, 619.0, 0.0, 108.0, 0.0, 109.0, 109.0, 9.6, 9.6, 2.4, 2.4]#第j种土地类型的总面积
T = np.array(T)
b = [[1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]#第j种土地类型是否有第k个编号的土地
# 读取上传的 Excel 文件，并将2023年种植情况导入粒子
file_path = '2023年作物情况.xlsx'
df_2023_planting = pd.read_excel(file_path, sheet_name='2023年的农作物种植情况')

# 初始化一个空数组来表示 2023 年的种植情况
initial_particle = np.zeros((8, 41, 12, 16))  # 8年，41个作物，12个土地类型，16个地块

# 将 2023 年的种植情况导入第一个时间步（t=0）
for index, row in df_2023_planting.iterrows():
    i = int(row['作物编号'] - 1)  # 作物编号从1开始
    j = int(row['地块类型'] - 1)  # 地块类型从1开始
    k = int(row['种植地块'] - 1)  # 地块编号从1开始
    initial_particle[0, i, j, k] = row['种植面积/亩']


# 鲁棒性函数的定义
def robust_function_l(previous_value):
    return previous_value + 0.1 * np.random.choice([-1, 1])


def robust_function_w(previous_value, i):
    if i == 5 or i == 6:
        return 1.075 * previous_value + 0.025 * np.random.choice([-1, 1])
    else:
        return previous_value + 0.05 * np.random.choice([-1, 1])


def robust_function_P(previous_value, i):
    if i in range(0, 16):
        return 1.05 * previous_value + 0.01 * np.random.choice([-1, 1])
    elif i in range(16, 37):
        return previous_value + 0.01 * np.random.choice([-1, 1])
    elif i in range(37, 40):
        return 0.97 * previous_value + 0.02 * np.random.choice([-1, 1])
    elif i == 40:
        return 0.95 * previous_value


def robust_function_C(previous_value):
    return 1.05 * previous_value + 0.01 * np.random.choice([-1, 1])


# 动态更新每个变量的函数：基于 t-1 年数据，更新 t 年数据
def update_robust_variables(t, l_prev, P_prev, w_sales_prev, C_prev):
    l_t = np.zeros_like(l_prev)
    P_t = np.zeros_like(P_prev)
    w_sales_t = np.zeros_like(w_sales_prev)
    C_t = np.zeros_like(C_prev)

    for i in range(len(l_prev)):
        for j in range(len(l_prev[i])):
            l_t[i][j] = robust_function_l(l_prev[i][j])
            P_t[i][j] = robust_function_P(P_prev[i][j], i)
            C_t[i][j] = robust_function_C(C_prev[i][j])

    for i in range(len(w_sales_prev)):
        w_sales_t[i] = robust_function_w(w_sales_prev[i], i)

    return l_t, P_t, w_sales_t, C_t

# 带惩罚项的目标函数
def robust_objective_function(x, l, P, w_sales, C, b, a,m):
    """
        计算整个八年种植方案的总利润，同时考虑跨年度的约束和惩罚项。
        """
    total_profit = 0
    penalty = 0
    yearly_profits = []  # 用于保存每年的利润
    l_t = l
    P_t = P
    w_sales_t = w_sales
    C_t = C
    # 遍历所有年份，逐年计算利润
    for t in range(8):
        yearly_profit = 0
        l_t, P_t, w_sales_t, C_t = update_robust_variables(t, l_t, P_t, w_sales_t, C_t)

        # 计算第 t 年的利润
        for i in range(41):
            for j in range(12):
                if a[i][j] == 1:
                    sales_volume = min(
                        l_t[i][j] * np.sum(a[i][j] * [b[j][k] * x[t, i, j, k] for k in range(16)]),
                        w_sales_t[i]
                    )
                    yearly_profit += P_t[i][j] * sales_volume - C_t[i][j] * np.sum(
                        a[i][j] * [b[j][k] * x[t, i, j, k] for k in range(16)]) + 0.5 * P_t[i][j] * (l_t[i][j] * np.sum(
                        a[i][j] * [b[j][k] * x[t, i, j, k] for k in range(16)]) - sales_volume)

        yearly_profits.append(yearly_profit)
        total_profit += yearly_profit

        # 第二个惩罚项约束条件检查
        for j in range(12):
            for k in range(16):
                if j in range(5) and t < 6:  # 对于粮食豆类
                    total_area_legumes = np.sum([x[_, i, j, k] for i in range(4) for _ in range(t,t+3)])  # 检查连续3年
                    if total_area_legumes < m[j][k]:
                        penalty += (m[j][k] - total_area_legumes) * 10  # 增加惩罚项
                elif j in range(6, 15) and t < 6:  # 对于蔬菜豆类
                    total_area_vegetables = np.sum([x[_, i, j, k] for i in range(16, 19) for _ in range(t,t+3)])  # 检查连续3年
                    if total_area_vegetables < m[j][k]:
                        penalty += (m[j][k] - total_area_vegetables) * 10  # 增加惩罚项

                    # 其它跨年度限制的惩罚逻辑可以在这里添加

        # 惩罚项2：最小种植面积等约束
        for j in range(12):
            for k in range(16):
                total_area = np.sum([x[t, i, j, k] for i in range(41)])  # 计算该地块的总种植面积
                if total_area < 0.8 * m[j][k]:  # 如果小于最小种植面积
                    penalty += (0.8 * m[j][k] - total_area) * 5  # 增加惩罚项
        # 不连续种植惩罚
        for i in range(41):
            for j in range(11):
                for k in range(16):
                    if b[j][k] != 0:
                        if 0 <= i <= 15 and x[t, i, j, k] == x[t - 1, i, j, k]:
                            penalty += 10
                        if 16 <= i <= 40 and j % 2 == 0 and (
                                x[t, i, j, k] == x[t, i, j + 1, k] or x[t, i, j, k] == x[t - 1, i, j + 1, k]):
                            penalty += 10
    # 返回整个八年计划的总利润减去惩罚项
    return total_profit - penalty, yearly_profits

class Particle:
    def __init__(self, dimensions, initial_particle,m, T):
        # 初始化粒子的四维位置（8年，41种作物，12种土地类型，16个地块）
        self.position = np.zeros((8, 41, 12, 16))
        self.velocity = np.zeros((8, 41, 12, 16))

        # 初始化位置和速度
        self.initialize_position(m, initial_particle)
        self.initialize_velocity(m)

        # 记录个人最佳位置和最佳适应度值
        self.best_position = np.copy(self.position)
        self.best_value = float('-inf')  # 初始化为负无穷，代表初始没有最佳值
        self.g_best = None
        # 打印 m 的值以检查是否正确传递
        self.apply_constraints(m, T)



    def initialize_position(self, m, initial_particle):
        """
        初始化粒子的位置，确保t=0时根据给定的初始粒子位置，t=1到t=7的随机生成
        """
        for t in range(1, 8):  # 确保t=0的数据固定，t=1到t=7随机初始化
            for j in range(12):
                for k in range(16):
                    for i in range(41):
                        self.position[t, i, j, k] = np.random.uniform(0, m[j][k])

        # 保证t=0的初始数据不变
        self.position[0] = initial_particle[0]

        # 确保位置大于等于0 且小于等于土地面积，通过广播调整 m 的形状
        self.position = np.clip(self.position, 0, np.array(m)[np.newaxis, np.newaxis, :, :])




    def initialize_velocity(self, m):
        """
        初始化粒子的速度，范围在[-m(j,k) * 0.3, m(j,k) * 0.3]之间
        """
        for t in range(1, 8):  # 只初始化 t=1 到 t=7 的速度，t=0 不更新
            for j in range(12):
                for k in range(16):
                    for i in range(41):
                        self.velocity[t, i, j, k] = np.random.uniform(- 0.2*m[j][k], 0.2*m[j][k])
        # 将 m 也广播处理
        v_max = np.array(m)[np.newaxis, np.newaxis, :, :]


    def update_velocity(self, p_best, g_best, w=0.8, c1=1.2, c2=1.5, t_iter=0, max_iter=200, m=m):
        """
        更新粒子的速度，随迭代次数增加，速度范围逐渐减小
        """
        r1 = np.random.rand(8, 41, 12, 16)
        r2 = np.random.rand(8, 41, 12, 16)

        # 初始最大速度范围，基于每个地块的面积 m[j][k]
        v_max_initial = np.zeros((8, 41, 12, 16))
        for t in range(1, 8):
            for j in range(12):
                for k in range(16):
                    for i in range(41):
                        v_max_initial[t, i, j, k] =  0.2*m[j][k]

        # 计算速度衰减系数
        decay_factor = 1 - (t_iter / max_iter)  # 随着迭代次数增加，速度减小
        v_max = v_max_initial * decay_factor

        # 计算新的速度
        cognitive_velocity = c1 * r1 * (p_best - self.position)  # 个体最佳位置影响
        social_velocity = c2 * r2 * (g_best - self.position)  # 全局最佳位置影响
        self.velocity = w * self.velocity + cognitive_velocity + social_velocity

        # 限制速度范围
        self.velocity = np.clip(self.velocity, -0.2*v_max, 0.2*v_max)

    def update_position(self, m):
        """
        更新粒子的当前位置，并确保 t=0 不被修改，且满足约束
        """
        for t in range(1, 8):  # t=0 不更新
            self.position[t] += self.velocity[t]

            # 确保位置在 [0, m(j,k)] 范围内
            for j in range(12):
                for k in range(16):
                    for i in range(41):
                        self.position[t, i, j, k] = np.clip(self.position[t, i, j, k], 0, m[j][k])

        # 保证 t=0 的数据不变
        self.position[0] = initial_particle[0]
        self.apply_constraints(m, T)

    def apply_constraints(self, m,T):
        """
        处理粒子的强制约束和惩罚项约束
        """
        for t in range(1, 8):
            # 第一个强制约束：种植面积不超过土地总面积
            for j in range(12):
                for j in range(12):
                    for k in range(16):
                        # 计算该地块种植的作物数量
                        planted_crops = [i for i in range(41) if self.position[t, i, j, k] > 0]

                        # 确保每种作物至少占地块面积的25%
                        for i in planted_crops:
                            if self.position[t, i, j, k] < 0.25 * m[j][k]:
                                self.position[t, i, j, k] = 0  # 面积小于25%，则不种植该作物

                        # 如果超过3种作物，保留种植面积最大的3种，其余的设为0
                        if len(planted_crops) > 3:
                            sorted_crops = sorted(planted_crops, key=lambda i: self.position[t, i, j, k], reverse=True)
                            for i in sorted_crops[3:]:  # 从第4种作物开始，将种植面积设为0
                                self.position[t, i, j, k] = 0

                    # 新的强制约束：每个作物最多选择3块地
                for i in range(41):
                    for j in range(12):
                        planted_plots = [k for k in range(16) if self.position[t, i, j, k] > 0]  # 获取该作物种植的地块编号
                        if len(planted_plots) > 3:
                            sorted_plots = sorted(planted_plots, key=lambda k: self.position[t, i, j, k], reverse=True)
                            # 保留种植面积最大的3块地块，其余设为0
                            for k in sorted_plots[3:]:
                                self.position[t, i, j, k] = 0
                for k in range(16):
                    total_area = np.sum([b[j][k]*self.position[t,:, j, k]])  # 计算该土地类型的总种植面积
                    if total_area > m[j][k]:  # 如果总种植面积超过土地总面积 T_j
                    # 按比例缩小种植面积
                        self.position[t, :, j, k] *= m[j][k] / total_area





def calculate_profit_without_penalty(t, x, l_t, P_t, w_sales_t, C_t, b, a, m):
    yearly_profit = 0
    total_area = 0  # 初始化总种植面积
    # 计算收益和总种植面积
    for i in range(41):  # 遍历作物
        for j in range(12):  # 遍历土地类型
            if a[i][j] == 1:
                        # 累加总种植面积
                total_area += np.sum(a[i][j] * [b[j][k] * x[t, i, j, k] for k in range(16)])
                        # 计算销售量
                sales_volume = min(
                        l_t[i][j] * np.sum(a[i][j] * [b[j][k] * x[t, i, j, k] for k in range(16)]),
                        w_sales_t[i])
                yearly_profit += P_t[i][j] * sales_volume - C_t[i][j] * np.sum(
                    a[i][j] * [b[j][k] * x[t, i, j, k] for k in range(16)]) + 0.5 * P_t[i][j] * (l_t[i][j] * np.sum(
                    a[i][j] * [b[j][k] * x[t, i, j, k] for k in range(16)]) - sales_volume)

    return yearly_profit, total_area


def pso_optimize_full_period(num_particles, dimensions, initial_t0, l, P, w_sales, C, b, a, m, T, iterations):
    best_position_overall = None
    best_value_overall = float('-inf')
    best_yearly_profits = []  # 保存每年的最优利润
    yearly_profits_without_penalty = []  # 保存每年无惩罚项的利润
    yearly_total_areas = []  # 保存每年的总种植面积
    fitness_values = []  # 保存每次迭代的最佳适应度

    # 初始化粒子群
    particles = [Particle(dimensions, initial_t0, m, T) for _ in range(num_particles)]

    w = 0.8  # 惯性权重
    c1 = 1.2  # 个体学习因子
    c2 = 1.5  # 全局学习因子

    for iteration in range(iterations):
        for particle in particles:
            # 使用新目标函数对整个八年的利润进行优化，并考虑跨年度惩罚项
            current_value, yearly_profits = robust_objective_function(particle.position, l, P, w_sales, C,
                                                                      b, a, m)

            # 更新粒子的个人最佳适应度
            if current_value > particle.best_value:
                particle.best_value = current_value
                particle.best_position = np.copy(particle.position)

            # 更新全局最佳适应度
            if current_value > best_value_overall:
                best_value_overall = current_value
                best_position_overall = np.copy(particle.position)
                best_yearly_profits = yearly_profits

        # 更新粒子的位置和速度
        for particle in particles:
            particle.update_velocity(best_position_overall, w, c1, c2)
            particle.update_position(m)  # 保证 t=0 的数据始终不变

        # 保存每次迭代的最佳适应度
        fitness_values.append(best_value_overall)

    # 动态更新鲁棒变量
    l_t = l
    P_t = P
    w_sales_t = w_sales
    C_t = C

    # 计算最终最优解集的每年利润和总种植面积（无惩罚项）
    print("\n最终优化解集每年的利润和总种植面积（不含惩罚项）:")
    for year in range(8):
        l_t, P_t, w_sales_t, C_t = update_robust_variables(year, l_t, P_t, w_sales_t, C_t)
        profit_without_penalty, total_area = calculate_profit_without_penalty(
            year, best_position_overall, l, P, w_sales, C, b, a, m)

        yearly_profits_without_penalty.append(profit_without_penalty)
        yearly_total_areas.append(total_area)

        print(f"Year {year + 2023}: Profit (without penalty) = {profit_without_penalty}, Total Planting Area = {total_area}")

    return best_position_overall, best_value_overall, yearly_profits_without_penalty, best_yearly_profits, yearly_total_areas, fitness_values


def save_results_to_excel(best_position_overall, yearly_profits_without_penalty, yearly_total_areas):
    # 创建一个 DataFrame，用于保存每一年的种植方案
    planting_data = []

    # 遍历八年（t 从 0 到 7 对应 2023 到 2030）
    for t in range(8):
        for i in range(41):  # 遍历作物
            for j in range(12):  # 遍历土地类型
                for k in range(16):  # 遍历地块
                    planting_area = best_position_overall[t, i, j, k]
                    if planting_area > 0 and a[i][j] == 1 and b[j][k] == 1:
                        planting_data.append([t + 2023, i + 1, j + 1, k + 1, planting_area])  # 年份从2023开始

    # 创建种植方案 DataFrame
    df_planting = pd.DataFrame(planting_data, columns=['Year', 'Crop', 'Land_Type', 'Plot', 'Planting_Area'])

    # 创建一个 DataFrame，用于保存每年的利润和总种植面积
    df_profit = pd.DataFrame({
        'Year': [2023 + i for i in range(8)],  # 8年的数据从2023年开始
        'Profit_Without_Penalty': yearly_profits_without_penalty,
        'Total_Planting_Area': yearly_total_areas  # 添加每年的总种植面积
    })

    # 保存到 Excel 文件
    with pd.ExcelWriter('optimal_planting_plan.xlsx') as writer:
        df_planting.to_excel(writer, sheet_name='Planting_Plan', index=False)
        df_profit.to_excel(writer, sheet_name='Yearly_Profits', index=False)




# 设定问题的维度和初始的 t=0 数据
dimensions = (8, 41, 12, 16)  # 8年, 41种作物, 12种土地类型, 16个地块
initial_t0 = initial_particle[0]  # t=0 的初始数据
# 使用 PSO 运行每一年独立优化的模型
# 使用 PSO 运行每一年独立优化的模型
# 运行优化模型，并计算每年不含惩罚项的利润
best_position_overall, best_value_overall, yearly_profits_without_penalty, best_yearly_profits, yearly_total_areas, fitness_values = pso_optimize_full_period(
    num_particles=50,
    dimensions=dimensions,
    initial_t0=initial_particle[0],  # t=0 的初始数据
    l=l,
    P=P,
    w_sales=w_sales,
    C=C,
    b=b,
    a=a,
    m=m,  # 传入地块面积矩阵 m
    T=T,  # 传入土地类型总面积 T
    iterations= 200 # 设置迭代次数
)

# 绘制PSO适应度的迭代图
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(fitness_values) + 1), fitness_values, marker='o', linestyle='-', color='b')
plt.title('迭代过程中全局最优适应度的变化')
plt.xlabel('迭代次数')
plt.ylabel('全局最优解的适应度')
plt.grid(True)
plt.xticks(range(1, len(fitness_values) + 1))
plt.savefig('PSO Fitness Over Iterations1.png')
plt.show()


# 保存最优种植方案、利润和种植面积到 Excel 文件
save_results_to_excel(best_position_overall, yearly_profits_without_penalty, yearly_total_areas)