# When dealing with string input remember always be carful about str to int conversion and try to reconvert it to str or not convert firstly in int use dynamic typecasting/ inplace typecasting 

import math
import os
import random
import re
import sys

def timeConversion(s):
    time = s.split(':')
    

    if 'AM' in s:
        if time[0] == '12':
            time[0] = '00'
    else:
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)
    
    
    time[2] = time[2][:2]
    print(s, ":".join(time))
    # print(time)
    return ":".join(time)
        

if __name__ == '__main__':
    # s = input()
    s = '12:40:22AM'

    result = timeConversion(s)
    print(result)
