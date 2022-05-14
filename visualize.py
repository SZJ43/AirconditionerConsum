# --coding:utf-8 --
import matplotlib.pyplot as plt
import pandas as pd
from pandas import concat

'''读入文件，打不开的文件已被删除'''
r_201a_jul = pd.read_csv('AirConditioner/R201aJul-Oct.csv')
r_201a_may = pd.read_csv('AirConditioner/R201aMay-Jul.csv')
r_201a_oct = pd.read_csv('AirConditioner/R201aOct-Dec.csv')
r_201b_jul = pd.read_csv('AirConditioner/R201bJul-Oct.csv')
r_201b_may = pd.read_csv('AirConditioner/R201bMay-Jul.csv')
r_201b_oct = pd.read_csv('AirConditioner/R201bOct-Dec.csv')
r_201c_jul = pd.read_csv('AirConditioner/R201cJul-Oct.csv')
r_201c_may = pd.read_csv('AirConditioner/R201cMay-Jul.csv')
r_201c_oct = pd.read_csv('AirConditioner/R201cOct-Dec.csv')
r_201d_jul = pd.read_csv('AirConditioner/R201dJul-Oct.csv')
r_201d_may = pd.read_csv('AirConditioner/R201dMay-Jul.csv')
r_201d_oct = pd.read_csv('AirConditioner/R201dOct-Dec.csv')
r_202a_jul = pd.read_csv('AirConditioner/R202aJul-Oct.csv')
r_202a_may = pd.read_csv('AirConditioner/R202aMay-Jul.csv')
r_202a_oct = pd.read_csv('AirConditioner/R202aOct-Dec.csv')

# 进行预处理，将同一个房间5-12月的数据合并
r_201a_sum = concat([r_201a_may, r_201a_jul, r_201a_oct], axis=0)
r_201b_sum = concat([r_201b_may, r_201b_jul, r_201b_oct], axis=0)
r_201c_sum = concat([r_201c_may, r_201c_jul, r_201c_oct], axis=0)
r_202a_sum = concat([r_202a_may, r_202a_jul, r_202a_oct], axis=0)

# 拼接完成后会发现七月、十月的数据是重复的，所以删除重复项
r_201a_sum.drop_duplicates()
r_201b_sum.drop_duplicates()
r_201c_sum.drop_duplicates()
r_202a_sum.drop_duplicates()

# 生成四张拼接表
r_201a_sum.to_csv('subtotal/R201aMay-Dec.csv')
r_201b_sum.to_csv('subtotal/R201bMay-Dec.csv')
r_201c_sum.to_csv('subtotal/R201cMay-Dec.csv')
r_202a_sum.to_csv('subtotal/R202aMay-Dec.csv')

'''接下来将每个房间5-12月的耗能情况进行可视化'''
# 计算完Room201a, 201b, 201c, 202a每个月的均值后进行折线图绘制
x = [5, 6, 7, 8, 9, 10 , 11, 12]
y = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
r_201a_x = [0.67731318, .0764833021, 0.63400512, 1.163247542,
            1.007364555, 0.612152612, 0.38983562, 0.286121233]
r_201b_x = [0.453411656, 0.644553735, 0.557409357, 0.928146274,
            0.80210438, 0.541779199, 0.306332054, 0.255985839]
r_201c_x = [0.420668259, 0.510069688, 0.374376481, 0.767722904,
            0.720229567, 0.468628913, 0.275571705,0.196952045]
r_202a_x = [1.005073701, 1.110859957, 0.280019945, 0.852649908,
            0.714355751, 0.493183753, 0.288433667, 0.246391686]
plt.plot(x, r_201a_x, 's-', color='r', label='Room 201a')
plt.plot(x, r_201b_x, 'o-', color='g', label='Room 201b')
plt.plot(x, r_201c_x, 's-', color='b', label='Room 201c')
plt.plot(x, r_202a_x, 'o-', color='y', label='Room 202a')
plt.xlabel('Month')
plt.ylabel('Average Consumption')
plt.legend(loc='best')
plt.show()


