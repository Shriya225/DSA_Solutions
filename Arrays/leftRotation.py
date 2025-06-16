# brute force
# o(kn)

def leftRotate(a,k):
    k=k%len(a)
    if k==0:
        print("a:",a)
        return
    for i in range(k):
        temp=a[0]
        for j in range(len(a)-1):
            a[j]=a[j+1]
        a[-1]=temp
    print("a:",a)

def rightRotate(a,k):
    k=k%len(a)
    print("right ")
    if k==0:
        print("a:",a)
        return
    for i in range(k):
        temp=a[-1]
        for j in range(len(a)-1,0,-1):
            a[j]=a[j-1]
        a[0]=temp        
    print("right rotaion:",a)
l=list(map(int,input("a:").split()))
leftRotate(l,int(input("k:")))
l=list(map(int,input("a:").split()))
rightRotate(l,int(input("k:")))
# 1 2 3 4 5
# 2 3 4 5 1
# 5 1 2 3 4