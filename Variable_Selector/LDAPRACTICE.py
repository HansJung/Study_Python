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
from sklearn.lda import LDA
from sklearn import datasets
import matplotlib.pyplot as plt

''' Function or Class '''


class Example:
    def __init__(self):
        return None


if __name__ == "__main__":
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names

    X = X[:100]
    y = y[:100]
    print "ho"
    clf =  LDA(solver='svd', n_components=3)
    NewX = clf.fit_transform(X,y)
    # NewX = clf.transform(X)

    for RowIdx in range(len(X)):
        EachData = NewX[RowIdx]
        for idx, elem in enumerate(EachData):
            if y[RowIdx] == 0:
                plt.plot(idx, elem, 'ro')
            elif y[RowIdx] == 1:
                plt.plot(idx, elem, 'bo')
    plt.grid()
    plt.show()