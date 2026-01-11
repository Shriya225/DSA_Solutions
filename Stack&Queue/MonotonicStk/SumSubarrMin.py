# 907. Sum of Subarray Minimums
def sumOfSubarrMin(a):
    nse=[None]*len(a)
    pse=[None]*len(a)
    stk=[]
    for i in range(len(a)):
        while stk and a[stk[-1]]>=a[i]:
            nse[stk.pop()]=i
        stk.append(i)
    stk=[]
    for i in range(len(a)):
        while stk and a[stk[-1]]>a[i]:
            stk.pop()
        if stk and a[stk[-1]]<a[i]:
            pse[i]=stk[-1]
        stk.append(i)
    ans=0
    print(nse)
    print(pse)
    for i in range(len(a)):
        n=nse[i] if nse[i]!=None else len(a)
        p=pse[i] if pse[i]!=None else -1
        ans+=a[i]*(i-p)*(n-i)
    return ans 


a=list(map(int,input("A:").split()))
print(sumOfSubarrMin(a))