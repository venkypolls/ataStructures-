#incomplete solution
def frog_jump(arr):
    our_arr = [False]*arr[len(arr)-1]
    our_arr[0] = True
    our_arr[1] = True
    k = 1
    print(our_arr)
    for i in arr:
        print(i)
        if i!=0 and i!=1:
            print(i,k)
            if (i-(k-1))>= 0 and (i-(k-1))<arr[len(arr)-1] and our_arr[i-(k-1)]:
                our_arr[i] = True
                k = k-1
            elif (i-(k+1))>= 0 and (i-(k+1))<arr[len(arr)-1]  and our_arr[i-(k+1)] :
                our_arr[i] = True
                k = k + 1
            elif (i-(k))>= 0 and (i-(k))<arr[len(arr)-1]  and our_arr[i-k] :
                our_arr[i] = True
                k = k

    print(our_arr)
    return our_arr[-1]

true = [0,1,3,5,6,8,12,17]
false = [0,1,2,3,4,8,9,11]
frog_jump(true)