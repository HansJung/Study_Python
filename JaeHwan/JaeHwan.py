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
import json
import signal
''' Function or Class '''


class Example:
    def __init__(self):
        return None

def handler(signum, frame):
    print "Forever is over!"
    raise Exception("end of time")


def JaeHwanURL(lat,long):
    URL = "http://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+long+"&sensor=true_or_false"
    return URL


if __name__ == "__main__":
    # TESTURL = "http://maps.googleapis.com/maps/api/geocode/json?latlng=34.020658,-118.264611&sensor=true_or_false"
    TESTURL = "http://maps.googleapis.com/maps/api/geocode/json?latlng=" "&sensor=true_or_false"
    MyCSV = HansCSV()
    LatLongDict = MyCSV.Reader(FileName = "latlong.csv",Delimiter=',', Header=True)
    Lat = LatLongDict['lat']
    Long = LatLongDict['long']

    IterIdx = 0

    signal.signal(signal.SIGALRM, handler)

    for lat, long in zip(Lat,Long):
        IterIdx += 1
        signal.alarm(5)

        try:
            JHURL =  JaeHwanURL(lat,long)
            A = json.loads(urllib.urlopen(JHURL).read())
            print A
            for idx, val in enumerate(A['results']):
                JHPingPong = val['formatted_address']
                print IterIdx,"|", JHPingPong
                break
        except Exception, exc:
            print IterIdx, "ERROR"
            # print exc

        # if IterIdx > 100:
        #     break




