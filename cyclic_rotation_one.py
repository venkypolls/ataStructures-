__author__ = '212576702'
import sys

def cyclic(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    print(arr)

lis_arr = [1,2,3,4,5,6,7]
cyclic(lis_arr)

