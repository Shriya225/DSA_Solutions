# rows <==> cols
# diagonal stays same
# lower triangle .. do swwap a[i][j],a[j][i]
# lower tirangle works effecively for square matrix
# for rectangular...
def transpose(a,m,n):
    ans=[([0]*m)]*n
    print(ans)
    for i in range(m):
        for j in range(n):
            if j<i:
                a[i][j],a[j][i]=a[j][i],a[i][j]
    for i in range(m):
        for j in range(n):
            print(a[i][j],end=" ")
        print()

mat=[]
m=int(input("rows:"))
n=int(input("cols:"))
ans=[([0]*m)]*n
print(ans)
for i in range(m):
    mat.append(list(map(int,input(f'row {i}:').split())))
print(mat)
transpose(mat,m,n)