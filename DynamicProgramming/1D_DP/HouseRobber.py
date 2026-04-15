#pick not pick...
# reccurence reln
def hr(a,i):
    if i<0:
        return 0
    if i==0:
        return a[i]
    p=a[i]+hr(a,i-2)
    np=hr(a,i-1)
    return max(p,np)


# memoization...
def hr_dp(a,i,dp):
    if i==0:
        return a[i]
    if i<0:
        return 0
    if dp[i]!=-1:return dp[i]
    l=hr_dp(a,i-2,dp)+a[i]
    r=hr_dp(a,i-1,dp)
    dp[i]=max(l,r)
    return dp[i]


# tabualtion...
def hr_tab(a):
    dp = [0] * len(a)
    dp[0] = a[0]   
    for i in range(1, len(a)):
        pick = a[i]
        if i > 1:
            pick += dp[i-2] 
        skip = dp[i-1]   
        dp[i] = max(pick, skip) 
    return dp[-1]

# space optimized...
def hr_opt(a):
    prev2 = 0
    prev1 = a[0]
    
    for i in range(1, len(a)):
        pick = a[i] + prev2
        skip = prev1
        
        curr = max(pick, skip)
        
        prev2 = prev1
        prev1 = curr
    
    return prev1