
# tabualtion
def lis_tab(a):
    dp=[[0]*(len(a)+1) for i in range(len(a)+1)]
    for i in range(len(a)-1,-1,-1):
        for j in range(i,-1,-1):
            ans=dp[i+1][j]
            if j==0 or a[i]>a[j-1]:
                # prev index shifting is done..
                ans=max(ans,1+dp[i+1][i+1])
            dp[i][j]=ans
    return dp[0][0]

# space otimization
def lis_tab(a):
    dp=[0]*(len(a)+1)
    for i in range(len(a)-1,-1,-1):
        for j in range(i,-1,-1):
            ans=dp[j]
            if j==0 or a[i]>a[j-1]:
                # prev index shifting is done..
                ans=max(ans,1+dp[i+1])
            dp[j]=ans
    return dp[0]

