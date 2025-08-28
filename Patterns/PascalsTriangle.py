# gneral method..not nCr..
#            1
#          1   1
#        1   2   1
#      1   3   3   1
#    1   4   6   4   1
#  1   5  10  10   5   1
# 1   6  15  20  15   6   1

def Pascals(n):
    ans=[]
    for i in range(1,n+1):
        row=[1]
        for j in range(1,i-1):
                row.append(ans[-1][j]+ans[-1][j-1])
        if i!=1:
            row.append(1)
        ans.append(row)
    print(ans)
    # print triangle...
    for i in range(n):
        print(" "*(n-i-1),end="")
        for j in range(len(ans[i])):
            print(ans[i][j],end=" ")
        print()


n=int(input("n:"))
Pascals(n)
