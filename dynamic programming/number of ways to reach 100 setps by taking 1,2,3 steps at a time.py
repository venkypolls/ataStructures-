def steps(n):
    lis = [0]*n
    lis[0] = 1
    lis[1] = 2
    lis[2] = 4
    for i in range(3,n):
        lis[i] = lis[i-1]+lis[i-2]+lis[i-3]
    return lis[n-1]


print(steps(4))