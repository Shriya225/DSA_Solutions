# 930. Binary Subarrays With Sum
# sliding window variant
def countLessThank(a,k):
    l=0
    c=0
    s=0
    for r in range(len(a)):
        s+=a[r]
        while s>k:
            s-=a[l]
            l+=1
        c+=r-l+1
    return c
def binarySum2(a,k):
    x=countLessThank(a,k)
    x2=countLessThank(a,k-1)
    print(x-x2)
a=list(map(int,input("a:").split()))
k=int(input("k:"))
print(binarySum2(a,k))