#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    possiblemat = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]
    minvalue = sys.maxsize

    for i in range(len(possiblemat)):
        possiblemat[i]
        cost=0
        for j in range(3):
            for k in range(3):
              if possiblemat[i][j][k]!=s[j][k]:
                cost+= abs(possiblemat[i][j][k]-s[j][k])
        if cost<minvalue:
            minvalue=cost
    print(minvalue)

if __name__ == '__main__':
    result = formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
