# using prefixSum arr alone
# can try this even without using arr for psum,as we need only prev psum ,store it in var.
# then sc-o(1)
def pivotIndex2(a,n):
    s=sum(a)
    prefix=[]
    for i in range(n):
        if (i==0 or i==n-1)and s-a[i]==0 :
            return i
        if i==0:
            prefix.append(a[i])
        else:
            prefix.append(prefix[-1]+a[i])
        if i!=0 and prefix[i-1]==s-prefix[i]:
            return i
    return -1


l=list(map(int,input("A:").split()))
print(pivotIndex2(l,len(l)))