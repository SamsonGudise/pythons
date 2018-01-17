#!/usr/bin/python

def bubbleSort(alist):
    exchange = True
    passnum = len(alist)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
        passnum=passnum-1

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
