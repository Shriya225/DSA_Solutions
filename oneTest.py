#  1   5  10  10   5   1
# 1   6  15  20  15   6   1

def Pascals(n):
    ans=[[1]]
    for i in range(2,n+1):
        x=[]
        for j in range(i):
            if j==0 or j==i-1:
                x.append(1)
            else:
                x.append(ans[-1][j]+ans[-1][j-1])
        ans.append(x)
    return ans
            



n=int(input("n:"))
print(Pascals(n))