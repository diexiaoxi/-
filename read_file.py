
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


tele_data = pd.read_csv('extract-by-190627.csv')

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
tele_data.to_csv('data_del.csv',header=True)

# 设定地图边界
map = Basemap(projection='stere',lat_0 = 28, lon_0 = 104,\
              llcrnrlat=3 ,urcrnrlat= 54,\
              llcrnrlon=73,urcrnrlon=-136,
              rsphere=6371200.,resolution='l',area_thresh=10000)

map.drawmapboundary()   # 绘制边界
map.drawstates()        # 绘制州
map.drawcoastlines()    # 绘制海岸线
map.drawcountries()     # 绘制国家
map.drawcounties()      # 绘制县

lat = np.array(tele_data['latitude'])                        # 获取维度之维度值
lon = np.array(tele_data['longitude'])                        # 获取经度值
rsrp = np.array(tele_data['lte_rsrp'])
level = np.array(tele_data['rsrp_level'])

#根据RSRP等级描点
colors = ['k','b','g','r','orange','y']
colors_level = []
for i in range(0,len(level)):
    index = int(level[i])-1
    colors_level = np.append(colors_level, colors[index])

print(colors_level)
x,y = map(lon,lat)
map.scatter(x,y,s= 0.1,c = colors_level)
plt.show()
plt.savefig("one.png")