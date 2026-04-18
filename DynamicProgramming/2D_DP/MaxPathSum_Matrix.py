# variable start poin --> var end point
# Maximum path sum in matrix (GFG)

# reccurence rel'n
# tc- (3^n) -- exponential
def maxsum(a):
    def maxpath(a,i,j):
        if j < 0 or j >= len(a[0]):
            return float('-inf')
        if i==0:
            return a[i][j]
        x=a[i][j]
        l=r=d=float('-inf')
        l=maxpath(a,i-1,j)
        r=maxpath(a,i-1,j-1)
        d=maxpath(a,i-1,j+1)
        return x+max(l,d,r)
    ans=float('-inf')
    for i in range(len(a[0])):
        ans=max(ans,maxpath(a,len(a)-1,i))
    return ans


# memoization
def maxsum_memo(a):
    def maxpath(a,i,j,dp):
        if j < 0 or j >= len(a[0]):
            return float('-inf')
        if i==0:
            return a[i][j]
        if dp[i][j]!=-1:return dp[i][j]
        x=a[i][j]
        l=maxpath(a,i-1,j,dp)
        r=maxpath(a,i-1,j-1,dp)
        d=maxpath(a,i-1,j+1,dp)
        dp[i][j]=x+max(l,d,r)
        return dp[i][j]
    ans=float('-inf')
    dp=[[-1]*len(a[0]) for _ in range(len(a))]
    for i in range(len(a[0])):
        ans=max(ans,maxpath(a,len(a)-1,i,dp))
    return ans


# tabualtion
def maxsum_tab(a):
    dp=[[-1]*len(a[0]) for _ in range(len(a))]
    # Base case
    for i in range(len(a[0])):
        dp[0][i]=a[0][i]
    # tabualtion
    for r in range(1,len(a)):
        for c in range(len(a[0])):
            val=a[r][c]
            ld=rd=float('-inf')
            d=dp[r-1][c]
            if c-1>=0:
                ld=dp[r-1][c-1]
            if c+1<len(a[0]):
                rd=dp[r-1][c+1]
            dp[r][c]=val+max(d,ld,rd)
    return max(dp[-1])


# space optimization..
# 2 arrays
def maxsum_tab(a):
    dp=[-1]*len(a[0])
    # Base case
    for i in range(len(a[0])):
        dp[i]=a[0][i]
    # tabualtion
    for r in range(1,len(a)):
        x=[-1]*len(a[0])
        for c in range(len(a[0])):
            val=a[r][c]
            ld=rd=float('-inf')
            d=dp[c]
            if c-1>=0:
                ld=dp[c-1]
            if c+1<len(a[0]):
                rd=dp[c+1]
            x[c]=val+max(d,ld,rd)
        dp=x
    return max(dp)

    
