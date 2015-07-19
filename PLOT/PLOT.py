# -*- coding: utf-8 -*-
'''
Goal : 
Author : Yonghan Jung, ISyE, KAIST 
Date : 15
Comment 
- 

'''

''' Library '''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

''' Function or Class '''


class PLOT:
    def __init__(self, X):
        self.X = np.array(X)


    def Log(self):
        Y = np.log(self.X)
        plt.figure()
        plt.title("Log")
        plt.grid()
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.plot(self.X, Y, 'bo')
        pass

    def LogLog(self):
        Y = np.log(self.X)
        plt.figure()
        plt.title("LogLog")
        plt.grid()
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.plot(np.log(self.X), np.log(Y), 'bo')
        pass

    def Quad(self):
        Y = self.X -  (self.X ** 2)
        plt.figure()
        plt.title("QUAD")
        plt.grid()
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.plot(np.log(self.X), (Y), 'bo')
        pass




if __name__ == "__main__":
    # X = np.linspace(1,100,num=500)
    # MyPlot = PLOT(X)
    # MyPlot.Log()
    # MyPlot.LogLog()
    # # MyPlot.Quad()
    # plt.show()
    for idx in range(5):
        a = idx

    print a