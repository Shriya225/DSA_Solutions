def isSortedAndRotated(a):
    c=0
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            c+=1
    if c==0 or (c==1 and a[0]>=a[-1]):
        print("yes")
        return
    print("no")

l=list(map(int,input("a:").split()))
isSortedAndRotated(l)