import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
from mpl_toolkits.basemap import Basemap
sns.set_context(rc={'figure.figsize': (10, 8)})

import warnings
warnings.filterwarnings('ignore')

class drawPic:
    def __init__(self):
        print("---To do: draw the map---")

    def drawDistribution(self, rsrp):
        sns.distplot(rsrp, rug=True, hist=False)
        plt.show()



    def drawHeatMap(self, tele_data):
        map = Basemap(projection='stere', lat_0=28, lon_0=104, \
                  llcrnrlat=3, urcrnrlat=54, \
                  llcrnrlon=73, urcrnrlon=-136,
                  rsphere=6371200., resolution='l', area_thresh=10000)

        map.drawmapboundary()  # 绘制边界
        map.drawstates()  # 绘制州
        map.drawcoastlines()  # 绘制海岸线
        map.drawcountries()  # 绘制国家
        map.drawcounties()  # 绘制县

        lat = np.array(tele_data['纬度'])  # 获取维度之维度值
        lon = np.array(tele_data['经度'])  # 获取经度值
        level = np.array(tele_data['rsrp_level'])

        # 根据RSRP等级描点
        colors = ['k', 'b', 'g', 'r', 'orange', 'y']
        colors_level = []
        for i in range(0, len(level)):
            index = int(level[i]) - 1
            colors_level = np.append(colors_level, colors[index])

        print(colors_level)
        x, y = map(lon, lat)
        map.scatter(x, y, s=0.1, c=colors_level)
        plt.show()
        plt.savefig("one.png")



