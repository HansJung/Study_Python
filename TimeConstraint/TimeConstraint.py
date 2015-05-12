# -*- coding: utf-8 -*-
'''
Goal : 
Author : Yonghan Jung, ISyE, KAIST 
Date : 150512
Comment 
- 

'''

''' Library '''
import signal
''' Function or Class '''



def handler(signum, frame):
    print "Forever is over!"
    raise Exception("end of time")


class Example:
    def __init__(self):
        return None


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)

    for idx in range(10):
        signal.alarm(5)
        try:
            print "Print this in 5 seconds!"
        except Exception, exc:
            print exc
