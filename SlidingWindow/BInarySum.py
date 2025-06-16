# 930. Binary Subarrays With Sum
# Prefix Sum concept
#  X not sliding window 

def binarySum(a,k):
    d=dict()
    s=0
    c=0
    for i in range(len(a)):
        s+=a[i]
        if s==k:
            c+=1
        if s-k in d:
            c+=d[s-k]
        if s in d:
            d[s]+=1
        else:
            d[s]=1
    return c

a=list(map(int,input("a:").split()))
k=int(input("k:"))
print(binarySum(a,k))