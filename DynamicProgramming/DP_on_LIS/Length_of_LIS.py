# 300. Longest Increasing Subsequence

def LIS(a, i, l):
    if i == len(a):
        return 0
    
    # always have the option to skip
    not_take = LIS(a, i+1, l)
    
    take = 0
    if l==-1 or a[i] > a[l]:
        take = 1 + LIS(a, i+1, i)
    
    return max(take, not_take)


# memoization..
class Solution:
    def lengthOfLIS(self, a):
        def LIS(a, i, l,dp):
            if i == len(a):
                return 0
            if dp[i][l]!=-1:return dp[i][l]
            # always have the option to skip
            not_take = LIS(a, i+1, l,dp)
            
            take = 0
            if l==-1 or a[i] > a[l]:
                take = 1 + LIS(a, i+1, i,dp)
            dp[i][l]=max(take, not_take)
            return max(take, not_take)
        dp=[[-1]*len(a) for i in range(len(a))]
        return LIS(a,0,-1,dp)


# Tabulation..
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
