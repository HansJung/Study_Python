# -*- coding: utf-8 -*-
'''
Goal : Matrix Operator P choosing the variable
Author : Yonghan Jung, ISyE, KAIST 
Date : 150513
Comment 
- 

'''

''' Library '''
import numpy as np
''' Function or Class '''


class VariableSelector:
    def __init__(self, Data, Chooser):
        self.data = np.array(Data)
        # Chooser contains the index of the variable to be selected
        self.Chooser = Chooser

    def ArraySelector(self):
        Selector = np.zeros((len(self.Chooser), len(self.data)))
        for idx, chooser in enumerate(self.Chooser):
            Selector[idx][chooser] = 1
        return np.dot(Selector, self.data)

    def MatrixSelector(self):
        Selector = np.zeros((len(self.Chooser), len(self.data)))
        for idx, chooser in enumerate(self.Chooser):
            Selector[idx][chooser] = 1
        return np.dot(np.dot(Selector, self.data), Selector.T)




if __name__ == "__main__":
    a = np.array([10,20,30,40,50])
    # a = a.reshape(5,5)
    Ch = [3,2,0]
    var = VariableSelector(a, Ch)
    print var.ArraySelector()

