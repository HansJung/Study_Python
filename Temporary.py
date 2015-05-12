# -*- coding: utf-8 -*-
'''
Goal : 
Author : Yonghan Jung, ISyE, KAIST 
Date : 15
Comment 
- 

'''

''' Library '''
import pandas as pd
import numpy as np

''' Function or Class '''


class Example:
    def __init__(self):
        return None


if __name__ == "__main__":
    a = np.array([10,20,30,40,50]*5)
    a = a.reshape(5,5)

    print a

    Chooser = [1,2,4]
    Selector = np.zeros((len(Chooser), len(a)))

    for idx, chooser in enumerate(Chooser):
        Selector[idx][chooser] = 1

    print np.dot(np.dot(Selector, a), Selector.T)