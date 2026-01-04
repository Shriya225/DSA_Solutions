def Transpose_square(a,r,c):
    for i in range(r):
        for j in range(i+1,c):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    
    for i in range(r):
        for j in range(c//2):
            a[i][j],a[i][r-1-j]=a[i][c-1-j],a[i][j]
    return a


r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(Transpose_square(mat,r,c))