#!/usr/bin/python


# Conditions and Loops
# http://rosalind.info/problems/ini4/

def sum_loop(start, stop):
    result = 0
    for i in range(start, stop+1):
        if i % 2 == 1:
            result += i
    return result 

	
print sum_loop(4593,9414)

