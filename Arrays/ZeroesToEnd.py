# slow and fast pointer concept.
# o(n)
def MoveZerosToEnd(a):
    s=0
    for i in range(len(a)):
        if a[i]!=0:
            a[s],a[i]=a[i],a[s]
            s+=1
    print("ans",a)

l=list(map(int,input("a:").split()))
MoveZerosToEnd(l)