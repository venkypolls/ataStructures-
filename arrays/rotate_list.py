__author__ = '212576702'
import os
import sys

def reversearr(arr,start,end):
    while 1:
        if start == end or start > end:
            return arr
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end += -1

original_list = raw_input("please enter the array to be rotated")
shifts = raw_input("please enter the number of shifts")
print(original_list)
integer_list = map(int, original_list.split(','))
print(integer_list)
arr = reversearr(integer_list,0, int(shifts)-1)
arr = reversearr(arr,int(shifts),len(arr)-1)
print(list(reversed(arr)))
