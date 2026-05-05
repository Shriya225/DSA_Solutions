# 714. Best Time to Buy and Sell Stock with Transaction Fee

# Make  any no.of transations

# reccurence rel'n
def bs2(a,i,buy,f):
    if i==len(a):
        return 0
    ans=float("-inf")
    if buy:
        ans=max(-a[i]+bs2(a,i+1,False),bs2(a,i+1,True))
    else:
        ans=max(a[i]-f+bs2(a,i+1,True),bs2(a,i+1,False))
    return ans

# memoization
class Solution:
    def maxProfit(self, a,f):
        def bs2(a,i,buy,dp):
            if i==len(a):
                return 0
            if dp[i][buy]!=-1:return dp[i][buy]
            ans=float("-inf")
            if buy:
                ans=max(-a[i]+bs2(a,i+1,False,dp),bs2(a,i+1,True,dp))
            else:
                ans=max(a[i]-f+bs2(a,i+1,True,dp),bs2(a,i+1,False,dp))
            dp[i][buy]=ans
            return ans
        dp=[[-1]*(2) for _ in range(len(a))]
        return bs2(a,0,True,dp)
    

# Tabulation
def bs2_tab(a,f):
    dp=[[-1]*(2) for _ in range(len(a)+1)]

    # base case
    dp[-1][0]=0
    dp[-1][1]=0
    
    # fill dp
    for i in range(len(a)-1,-1,-1):
        for j in range(2):
            if j==1:
                ans=max(-a[i]+dp[i+1][0],dp[i+1][1])
                
            else:
                ans=max(a[i]-f+dp[i+1][1],dp[i+1][0])
            dp[i][j]=ans
    return dp[0][1]


# space optimization
def bs2_so(a,f):
    p1=p2=0
    # fill dp
    for i in range(len(a)-1,-1,-1):
            c_b=max(-a[i]+p1,p2)     
            c_s=max(a[i]-f+p2,p1)
            p1=c_s
            p2=c_b
    return c_b