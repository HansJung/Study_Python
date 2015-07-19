# -*- coding: utf-8 -*-
'''
Goal : 
Author : Yonghan Jung, ISyE, KAIST 
Date : 15
Comment 
- 

'''

''' Library '''
from CSV_Reader.CSV_Reader import HansCSV
import urllib
import unicodedata
from bs4 import BeautifulSoup

''' Function or Class '''


class Example:
    def __init__(self):
        return None

def CarInfo(CarID):
    URL = "http://auto.naver.com/car/lineup.nhn?" + CarID
    HTMLtext = urllib.urlopen(URL).read()
    soup = BeautifulSoup(HTMLtext)
    return [soup.find_all('div',{'class':'btm_col main_info'}), soup.find_all('div',{'class':'btm_col'})]




if __name__ == "__main__":
    CarIDFile = open("CarID.txt",'rU')
    CarIDBox = []
    for row in CarIDFile.readlines():
        row = row[:-2]
        CarIDBox.append(row)

    # print CarIDBox
    for idx, eachID in enumerate(CarIDBox):
        print CarIDBox[idx]
        Info = CarInfo(eachID)
        # Info[0] = Info[0].replace("\t","")
        TargetString_Main = str(Info[0]).replace("\t","")
        TargetString_Main = TargetString_Main.replace("<br>","")
        TargetString_Main = TargetString_Main.replace("</br>","")
        TargetString_Main = TargetString_Main.replace("</li>","")
        TargetString_Main = TargetString_Main.replace("\n","")
        MainInfo = TargetString_Main.replace("\t","").split("<li>")

        TargetString_Engine = str(Info[1]).replace("\t","")
        TargetString_Engine = TargetString_Engine.replace("<br>","")
        TargetString_Engine = TargetString_Engine.replace("</br>","")
        TargetString_Engine = TargetString_Engine.replace("</li>","")
        TargetString_Engine = TargetString_Engine.replace("\n","")
        EngineInfo = TargetString_Engine.replace("\t","").split("<li>")

        # TargetString_Performance = str(Info[2]).replace("\t","")
        # TargetString_Performance = TargetString_Performance.replace("<br>","")
        # TargetString_Performance = TargetString_Performance.replace("</br>","")
        # TargetString_Performance = TargetString_Performance.replace("</li>","")
        # PerfInfo = TargetString_Performance.replace("\t","").split("<li>")

        # print type(MainInfo), len(MainInfo)
        print "=" * 100
        print "주요제원"

        for MainString in MainInfo:
            # MainString = MainString
            if '</ul></div>, <div class="btm_col main_info"><ul>' in MainString:
                print "-" * 50
            else:
                print MainString

        print "\n"

        print "=" * 100
        print "엔진제원"
        for EngineString in EngineInfo:
            print EngineString.decode('utf-8').encode('utf-8')


        print "=" * 100
        print "=" * 100
        print "=" * 100

        if idx > 0:
            break
