# 1572. Matrix Diagonal Sum
def diagonalSum(a,r,c):
    s=0
    for i in range(r):
            s+=a[i][i]+a[i][r-1-i]
    if r%2!=0:
        s-=a[r//2][r//2]
    return s
            
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(diagonalSum(mat,r,c))