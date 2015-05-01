# -*- coding: utf-8 -*-
'''
Goal : To know how to read the file
Author : Yonghan Jung, IE, KAIST 
Date : 
Comment 
- 
'''

''' Library '''
import numpy as np
import pandas as pd

''' Function or Class '''

''' Comment '''
# This is a simple and efficient way to read txt and csv. 

if __name__ == "__main__":
    MapData = np.loadtxt("../Data/mapdata_copyright_openstreetmap_contributors.txt")
    Traps = pd.read_csv('../Data/train.csv')[['Date', 'Trap','Longitude', 'Latitude', 'WnvPresent']]
