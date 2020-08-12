#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    dist = sys.maxsize
    for i in range(100):
        if dist == 0:
            return "YES"
        newdist = abs(x1 - x2)
        print(str(x1)+ " "+ str(x2)+ "    "+str(newdist))
        if newdist > dist:
            return "NO"
        else:
            dist=newdist
            x1 =  x1+ v1
            x2 = x2 + v2


if __name__ == '__main__':


    result = kangaroo(43, 2, 70, 2)
    print(result)
