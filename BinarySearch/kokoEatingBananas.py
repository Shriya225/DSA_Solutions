# 875. Koko Eating Bananas
# A BS Variant looking for min possible answer...

# TC- O(n*log(max(a)))

import math
def helper(a,mid):
    s=0
    for i in a:
        s+=math.ceil(i/mid)
        print(math.ceil(1.000000003196068),i/mid,"i",i,mid)
    return s

def koko(a,hrs):
    l,h=1,max(a)
    ans=-1
    while l<=h:
        m=(l+h)//2
        newH=helper(a,m)
        print("newH:",newH,"h:",hrs)
        if newH<=hrs:
            ans=m
            h=m-1
        elif newH>hrs:
            l=m+1
    return ans
        

a=list(map(int,input("a:").split()))
h=int(input("T:"))
print(koko(a,h))  