#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a=sorted(a)
    b=sorted(b)
    listofnumbers=[]
    for i in range(a[-1],b[0]+1):
        print(i)
        isvalid=True
        for j in range(len(a)):
            if i%a[j]!=0:
                isvalid=False
        for j in range(len(b)):
             if b[j]%i!=0:
                isvalid=False
        if isvalid:
            listofnumbers.append(i)
    print (len(listofnumbers))
if __name__ == '__main__':
    total = getTotalX([2,4], [16,32,96])

