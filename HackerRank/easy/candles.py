#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    sort=sorted(ar)
    maxvalue=sort[-1]

    totalcandles=1
    for i in range(1,len(sort)):
        if sort[i]==maxvalue:
            totalcandles+=1
    print(totalcandles)
if __name__ == '__main__':

    lista=list()
    for j in range(100000):
        lista.append(9999999)
    result = birthdayCakeCandles(lista)

