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
from scipy.stats import f

''' Function or Class '''


class Example:
    def __init__(self):
        return None


if __name__ == "__main__":
    DoF1 = 10
    DoF2 = 20

    print f.ppf(0.90, DoF1, DoF2)
