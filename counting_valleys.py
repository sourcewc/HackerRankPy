#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
# url:https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#

def countingValleys(steps, path):
    # Write your code here
    depth = 0
    sea_level = 0
    prev_depth = 0
    route = list(path)
    vallys = 0

    for counter in range(steps):
        if route[counter] == 'U':
            depth += 1
        else:
            depth -= 1

        if depth > prev_depth and depth == sea_level:
            vallys += 1
        prev_depth = depth
    return vallys


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)