# 566. Reshape the Matrix

# flatten and reshape
def reshape(a,r,c):
    mr=len(a)
    mc=len(a[0])
    if r*c!=(mr*mc):
        return a
    ans=[]
    for i in range(mr):
        for j in range(mc):
            ans.append(a[i][j])
    f_ans=[]
    x=0
    for i in range(r):
        l=[]
        for j in range(c):
            l.append(ans[x])
            x+=1
        f_ans.append(l)
    return f_ans
  
            
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)

print(reshape(mat,r,c))



# use var to check boundaries
# no flattening
# better sol
def reshape(a,r,c):
    mr=len(a)
    mc=len(a[0])
    if r*c!=(mr*mc):
        return a
    ans=[]
    x=y=0
    for i in range(r):
        l=[]
        for j in range(c):
            if y==mc:
                y=0
                x+=1
            print(x,y)
            l.append(a[x][y])
            y+=1
        ans.append(l)
    return ans

         
mr=int(input("r:"))
mc=int(input("c:"))
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(reshape(mat,r,c))




# flatten logic
def reshape(a,r,c):
    mr=len(a)
    mc=len(a[0])
    if r*c!=(mr*mc):
        return a
    ans=[]
    indx=0
    for i in range(r):
        l=[]
        for j in range(c):
            l.append(a[indx//mc][indx%mc])
            indx+=1
        ans.append(l)
    return ans
    
mr=int(input("r:"))
mc=int(input("c:"))
r=int(input("r:"))
c=int(input("c:"))
mat=[]
for i in range(r):
    mat.append(list(map(int,input(f"enter {r} row eles :").split())))
print(mat)
print(reshape(mat,r,c))