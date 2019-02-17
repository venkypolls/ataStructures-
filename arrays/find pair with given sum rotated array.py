import sys

#find the pivot

def pivot(arr,low,high):
    if low == high:
        return low
    if low>high:
        return -1
    mid = int((low+high)/2)
    if(arr[mid] > arr[mid+1]):
        return mid
    if arr[mid]<arr[mid-1]:
        return mid-1
    if arr[mid] > arr[low]:
        return pivot(arr,mid+1,high)
    return pivot(arr,low,mid-1)

arr = [4,5,6,7,8,1,2,3]
pair_sum = 9
piv = pivot(arr,0,len(arr)-1)
low = piv+1
high = piv
while low != high :
    currsum = arr[low]+arr[high]
    if(currsum == pair_sum):
        print("the pair is {} and {}".format(arr[low],arr[high]))
        if (low != len(arr) - 1):
            low += 1
        else:
            low = 0
    elif currsum <pair_sum:
        if(low != len(arr)-1):
            low+=1
        else:
            low = 0
    else:
        if high != 0:
            high -= 1
        else:
            high = len(arr)-1

