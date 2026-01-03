
def Spiral(a,row,col):
    t=l=0
    b,r=row-1,col-1
    while t<=b and l<=r:
        for i in range(l,r+1):
            print(a[t][i],end=" ")
        t+=1
        for i in range(t,b+1):
            print(a[i][r],end=" ")
        r-=1
        if t<=b and l<=r:
            for i in range(r,l-1,-1):
                print(a[b][i],end=" ")
            b-=1
        if t<=b and l<=r:
            for i in range(b,t-1,-1):
                print(a[i][l],end=" ")
            l+=1

            
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(Spiral(mat,r,c))