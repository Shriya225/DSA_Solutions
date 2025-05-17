# unsroted arr
# 2 sum
# hashing
def twoSum(a,k):
    d={}
    for i in range(len(a)):
        if k-a[i] in d:
            return [d[k-a[i]],i]
        d[a[i]]=i

l=list(map(int,input("A:").split()))
k=int(input("K:"))
print(twoSum(l,k))