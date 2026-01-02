# # row wise traversal
def matrix(a,r,c):
    for i in range(r):
        for j in range(c):
            print(a[i][j],end=" ")
        print()

r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
matrix(mat,r,c)

# col wise traversal
def matrix(a,r,c):
    for i in range(c):
        for j in range(r):
            print(a[j][i],end=" ")
        print()

r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
matrix(mat,r,c)