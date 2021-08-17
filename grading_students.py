#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
# url:https://www.hackerrank.com/challenges/grading/problem
#

def gradingStudents(grades):
    # Write your code here
    final_score = []
    for i in range(len(grades)):
        if grades[i] < 38:
            final_score.append(grades[i])
            continue

        final_score.append(grades[i] + (5 - grades[i] % 5) if grades[i] % 5 > 2 else grades[i])
    return final_score

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)