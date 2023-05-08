#!/bin/python3

import math
import os
import random
import re
import sys

def calculate(n):
    #If  is even and in the inclusive range of 2 to 5, print Not Weird
    if n <= 5 :
        print("Not Weird")
    #If  is even and in the inclusive range of 6 to 20, print Weird
    elif n <= 20 :
        print("Weird")
    #If  is even and greater than 20, print Not Weird
    else :
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())

    if n >= 1 and n <= 100 :
        if n % 2 != 0 :
            print("Weird")
        else :
            calculate(n)