# -*- coding: utf-8 -*-
'''
Goal : To understand the concept of class inheritance
Author : Yonghan Jung, IE, KAIST 
Date : 
Comment 
- 
'''

''' Library '''

''' Function or Class '''
class ParentFather:
    def __init__(self, FatherName):
        self.FatherName = FatherName
    def Call(self):
        print "{Name} is called!".format(Name = self.FatherName)

class ParentMother:
    def __init__(self, MotherName):
        self.MotherName = MotherName
    def Call(self):
        print "{Name} is called!".format(Name = self.MotherName)

class Child(ParentFather, ParentMother):
    def __init__(self, FatherName, MotherName):
        ParentFather.__init__(self, FatherName)
        ParentMother.__init__(self, MotherName)
    def Intro(self):
        ParentFather.Call(self)
        ParentMother.Call(self)
        print "My parents are {Father} and {Mother}".format(Father = self.FatherName, Mother = self.MotherName)


if __name__ == "__main__":
    MyChild = Child("Hans", "Rachael")
    MyChild.Intro()
