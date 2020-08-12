#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        spaces = n - i
        numerals = i
        sentence = ""
        for j in range(spaces):
            sentence = sentence + " "
        for t in range(numerals):
            sentence = sentence + "#"
        print(sentence)




if __name__ == '__main__':
    n = int(input())

    staircase(n)
