# O(k^n)
def fjk(a,i,k):
    ans=float('inf')
    if i==0:
        return 0
    for j in range(1,k+1):
        if i-j>=0:
            ans=min(ans,fjk(a,i-j,k)+abs(a[i]-a[i-j]))
    return ans

# Memoization
# tc - o(n*k)
def fjk(a,i,k,dp):
    ans=float('inf')
    if i==0:
        return 0
    if dp[i]!=-1:return dp[i]
    for j in range(1,k+1):
        if i-j>=0:
            ans=min(ans,fjk(a,i-j,k,dp)+abs(a[i]-a[i-j]))
    dp[i]=ans
    return ans

# tabulation
def fjf_tab(a,k):
    dp=[-1]*len(a)
    dp[0]=0
    for i in range(1,len(a)):
        ans=float('inf')
        for j in range(1,k+1):
            if i-j>=0:
                ans=min(ans,dp[i-j]+abs(a[i]-a[i-j]))
        dp[i]=ans
    return dp[len(a)-1]


# O(1) space optimzation.... how think??
