# 368. Largest Divisible Subset

# wrong code..
# we are considering only one path greedily ,this will fail...
def lds(a):
    ans=[]
    for i in range(len(a)):
        if not ans:
            ans.append(a[i])
        else:
            f=True
            for k in range(len(ans)):
                if a[i]%ans[k]!=0 and ans[k]%a[i]!=0:
                    f=False
                    break
            if f:
                ans.append(a[i])
    return ans
# a=list(map(int,input("a:").split()))
# print(lds(a))


# just sort the given array
# convert ques to LIS..
def lds_tab(a):
    a.sort()
    dp=[1]*(len(a))
    bt=[-1]*(len(a))
    ans=0
    for i in range(len(a)):
        for j in range(i):
            if a[i]%a[j]==0:
                if dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    bt[i]=j
        if dp[i]>dp[ans]:
            ans=i
    # backtarck...
    fans=[]
    print(bt,ans,"dp",dp)
    while ans>=0:
        fans.append(a[ans])
        ans=bt[ans]
    return fans
        
a=list(map(int,input("a:").split()))
print(lds_tab(a))