# -*- coding: utf-8 -*-
'''
Goal : Study How to use Color Map for Spatio Temporal
Author : Yonghan Jung, IE, KAIST 
Date : 150502 To create Color Map
Comment 
- 
'''

''' Library '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

''' Function or Class '''

if __name__ == "__main__":
    a = np.sort(np.random.randn(10, 10)) # 10 X 10 Random value Matrix
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(a, cmap=cm.get_cmap('jet'))
    fig.savefig('map1.png')
    # plt.show()
    # SubPlot, Image a with jet color

    # let's use jet and modify the alpha channel
    # you would use your own colour map specified by f
    ## Modification of image setting
    ## This will change the RGB value specified by f
    my_cmap = cm.get_cmap('jet')
    alphas = np.abs(np.linspace(-1.0, 1.0, my_cmap.N))
    print alphas
    # overwrite the alpha channel of the jet colour map
    ## I think this represent R,G,B and
    ## This technique is for making gray coloured map
    my_cmap._lut[:-3,-1] = alphas

    # plot data with our modified colour map
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.imshow(a, cmap=my_cmap)
    fig.savefig('map2.png')


