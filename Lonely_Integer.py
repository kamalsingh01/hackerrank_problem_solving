'''
Given an array of integers, where all elements but one occur twice, find the unique element.

Example a = [1,2,3,4,3,2,1]

The unique element is 4.

Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once

Input Format

The first line contains a single integer, n , the number of integers in the array.
The second line contains n  space-separated integers that describe the values in a.

Constraints

    1<=n<=100

It is guaranteed that n is an odd number and that there is one unique element.
, where .
 0 <= a[i] <=1 00, where 0 <= i <= n
'''

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def lonelyinteger(a):
    # Write your code here
    lst = []
    unique_num = None
    for i in a:
        if i in lst:
            lst.remove(i)
            continue
        else:
            lst.append(i)
    return lst[0]

#another Solution
# def lonelyinteger(a):
#     s = set(a)
#     double_sum = 2 * sum(s)
#     return double_sum - sum(a)
            
        

if __name__ == '__main__':

    a = [1,2,3,4,3,2,1]
    #a=[]
    #n = int(input())
    # for i in range(n):
    #     a.append(int(input()))
    result = lonelyinteger(a)
    print(result)