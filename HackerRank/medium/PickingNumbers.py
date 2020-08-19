#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    numbers=sorted(a)
    maxvalue=0
    cont=1
    for i in range(1,len(numbers)):

        if (numbers[i]-numbers[i-1])<2:
            cont+=1
        else:

            if maxvalue<cont:
                maxvalue=cont
            cont=1
    print(maxvalue)
if __name__ == '__main__':


    result = pickingNumbers([4,5,6,3,3,1])

