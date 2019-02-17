import sys
import os

def rotation(arr):
    temp = arr[0]
    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp
    return arr

def maxsum(arr):
    totalsum = 0
    add_sum = sum(arr)
    for i in range(len(arr)):
        totalsum += arr[i]*i
    for i in range(len(arr)):
        currsum = totalsum - add_sum + arr[i]*(len(arr))
        if currsum > totalsum:
            totalsum = currsum
    return totalsum


arr = [1, 20, 2, 10]
# print(rotation(arr))
print(maxsum(arr))

