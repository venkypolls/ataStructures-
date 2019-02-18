__author__ = '212576702'

arr = [3,4,5,6,7,8,1,2]
key = 2

def search(arr,low,high):
    #find the pivot
    if high == low:
        return low
    if low > high:
        return -1
    mid = int((low+high)/2)
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if low < mid and arr[mid-1] > arr[mid]:
        return (mid-1)
    if arr[mid] >= arr[low]:
        return search(arr,mid+1,high)
    return search(arr,low,mid-1)

x = search(arr,0,len(arr)-1)+1
if arr[0] >= key:
    low = x
    high = len(arr)-1
elif arr[0] < key:
    low = 0
    high = x


while 1:
    mid = int((low+high)/2)
    if(arr[mid] == key):
        print(mid+1)
        break
    if arr[mid]>key and mid >low:
        high = mid-1
    if arr[mid]<key and mid <high :
        low = mid+1
    # print(low,mid,high)
