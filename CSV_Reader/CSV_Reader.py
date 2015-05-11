# -*- coding: utf-8 -*-
'''
Goal : CSV Reader
Author : Yonghan Jung, ISyE, KAIST 
Date : 150511
Comment 
- 

'''

''' Library '''
import csv
''' Function or Class '''


class HansCSVReader:
    def __init__(self, FileName, delimiter, header):
        self.FileName = FileName
        self.delimiter = delimiter
        self.header = header

    def Reader(self):
        with open(self.FileName, 'rb') as csvfile:
            CSVReader = csv.reader(csvfile, delimiter = self.delimiter)
            if self.header:
                Header = CSVReader.next()
                Column = dict()
                for h in Header:
                    Column[h] = []
                for row in CSVReader:
                    for h, v in zip(Header, row):
                        Column[h].append(v)
            else:
                Column = []
                for row in CSVReader:
                    Row = []
                    Row.append(row.split(self.delimiter))
                    Column.append(Row)

        return Column


if __name__ == "__main__":
    print None