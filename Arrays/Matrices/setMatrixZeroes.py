# # ok using xtra space
# def matrixZeroes(a,r,c):
#     ans=[]
#     for i in range(r):
#         l=[]
#         for j in range(c):
#             l.append(a[i][j])
#         ans.append(l)
#     row=[]
#     col=[]
#     for i in range(r):
#         for j in range(c):
#                 if a[i][j]==0:
#                     print("a is 0",i,j)
#                     for k in range(r):
#                         ans[k][j]=0
#                     for k in range(c):
#                         ans[i][k]=0
#                     print("ans here",ans)
#     return ans
            
# r=int(input("r:"))
# c=int(input("c:"))
# mat=[]
# for i in range(r):
#     mat.append(list(map(int,input(f"enter {r} row eles :").split())))
# print(matrixZeroes(mat,r,c))


# set inf to avoid setting anothr 0 in smae col to vanish.
# def matrixZeroes(a,r,c):
#         r,c=len(a),len(a[0])
#         for i in range(r):
#             for j in range(c):
#                     if a[i][j]==0:

#                         for k in range(r):
#                             if a[k][j]!=0:
#                                 a[k][j]=float("inf")
#                         for k in range(c):
#                             if a[i][k]!=0:
#                                 a[i][k]=float("inf")
#         for i in range(r):
#             for j in range(c):
#                     if a[i][j]==float("inf"):
#                         a[i][j]=0
#         return a




# better soln
# use row,col arr to mark if entire is to be 0
def matrixZeroes(a,r,c):
        r,c=len(a),len(a[0])
        row=[0]*r
        col=[0]*c
        for i in range(r):
            for j in range(c):
                    if a[i][j]==0:
                          row[i]=1
                          col[j]=1
        for i in range(r):
            for j in range(c):
                    if row[i]==1 or col[j]==1:
                          a[i][j]=0
        return a
            
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(matrixZeroes(mat,r,c))