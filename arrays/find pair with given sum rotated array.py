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
        low = (low+1)%len(arr)
    elif currsum <pair_sum:
        low = (low+1)%len(arr)
    else:
        high = (len(arr) + high -1)%len(arr)

