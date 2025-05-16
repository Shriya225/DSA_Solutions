# 974. Subarray Sums Divisible by K
def subarraysDivByK(a,k,n):
    d={}
    currSum=rem=0
    c=0
    for i in range(len(a)):
        currSum+=a[i]
        rem=currSum%k
        if rem==0:
            c+=1
        if rem in d:
            c+=d[rem]
        d[rem]=d.get(rem,0)+1
    print("c:",c)
a=list(map(int,input("a:").split()))
k=int(input("K:"))
subarraysDivByK(a,k,len(a))