import random
import math
import pandas as pd
import numpy as np

class generatePseudoLoc:
    def __init__(self):
        print("---To do: generate a series of pseudo GPS points---")
 def generate_random_gps(self, lati, lon, cid_index, radius):
        PseudoLocSet = pd.DataFrame(columns=('latitude', 'longtitude'))
        radius_in_degrees = radius /111300
        # 111300 is the meters in degree
        # for i in range(0, len(cid_index)-1):
        for i in range(0, 5):
            base_lat = np.mean(lati[int(cid_index[i]):int(cid_index[i+1])])
            base_log = np.mean(lon[int(cid_index[i]):int(cid_index[i+1])])
            u = float(random.uniform(0.0, 1.0))
            v = float(random.uniform(0.0, 1.0))
            w = radius_in_degrees * math.sqrt(u)
            t = 2 * math.pi * v
            x = w * math.cos(t)
            y = w * math.sin(t)
            longitude = y + base_log
            latitude = x + base_lat
            print(base_log,base_lat)
            print(longitude,latitude)
            # 这里是想保留6位小数点
            loga = '%.6f' % longitude
            lata = '%.6f' % latitude

            PseudoLocSet = PseudoLocSet.append(
                 pd.DataFrame({'latitude': [lata], 'longtitude': [loga]}),
                 ignore_index=True)
        return PseudoLocSet

