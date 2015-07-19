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
from scipy import optimize
''' Function or Class '''

def test(x):
    x = np.reshape(x,(2,2))
    B = np.linalg.inv(x)
    return np.trace(np.dot(x,B))

    # return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0) + abs(sum(x))


if __name__ == "__main__":
    res = optimize.fmin(func=test, x0 = np.random.rand(2*2))
    print res

