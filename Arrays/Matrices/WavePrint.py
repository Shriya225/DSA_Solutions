
def Wave(a,r,c):
    for i in range(c):
        for j in range(r):
            if (i+1)%2==0:
                print(a[r-1-j][i],end=" ")
            else:
                print(a[j][i],end=" ")


            
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(Wave(mat,r,c))