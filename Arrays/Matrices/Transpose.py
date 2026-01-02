# rectangle matrces best soln
# must use extra space
# just doing column wise traversal is enough..
def Transpose(a,r,c):
    ans=[]
    for i in range(c):
        l=[]
        for j in range(r):
            l.append(a[j][i])
        ans.append(l)
    return ans
            
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(Transpose(mat,r,c))


# square mat 
# inplace
# wont work fr rectangle
def Transpose_square(a,r,c):
    for i in range(r):
        for j in range(i+1,c):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    return mat
            
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(Transpose_square(mat,r,c))