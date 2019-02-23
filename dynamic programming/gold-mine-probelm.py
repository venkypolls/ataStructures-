
def goldMine(gold,m,n):
    for j in range(1,m):
        for i in range(n):
            top = 0
            bottom =0
            left = 0
            if i-1>=0 and j-1>=0:
                top = gold[i-1][j-1]
            if j-1>=0 and i>=0:
                left = gold[i][j-1]
            if j-1>=0  and i+1<n :
                bottom = gold[i+1][j-1]
            gold[i][j] = gold[i][j]+compare(top,bottom,left)
    return gold

def compare(a,b,c):
    if a>=b:
        if a>=c:
            return a
        else :
            return c
    else:
        if b>=c:
            return b
        else:
            return c

gold = [[10, 33, 13, 15],
                  [22, 21, 4, 1],
                  [5, 0, 2, 3],
                  [0, 6, 14, 2]];

m = 4
n = 4
# print(goldMine(gold,m,n))
max = 0
for i in range(n):
    if gold[i][m-1] > max:
        max = gold[i][m-1]
print("maximum gold that can be obtained is ",max)