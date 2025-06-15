# 0 1 2 3 4
# 1 2 3 4 5

# 3 4 5 1 2
# o(n+k)
# sc-o(k%n)
def leftRotation(a,k):
    k=k%len(a)
    temp=[]
    for i in range(k):
        temp.append(a[i])
    print(temp,"temp")
    for i in range(len(a)-k):
        a[i]=a[i+k]
    c=0
    for i in range(len(a)-k,len(a)):
        a[i]=temp[c]
        c+=1
    print(a)

l=list(map(int,input("a:").split()))
k=int(input("K:"))
leftRotation(l,k)