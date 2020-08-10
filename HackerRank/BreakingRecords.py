#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    minrecord = scores[0]
    maxrecord = scores[0]
    timesmin = 0
    timesmax = 0
    for i in range(1, len(scores)):
        if scores[i] < minrecord:
            timesmin += 1
            minrecord = scores[i]
        if scores[i] > maxrecord:
            timesmax += 1
            maxrecord = scores[i]
    print( [ timesmax,timesmin])


if __name__ == '__main__':


    result = breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])

