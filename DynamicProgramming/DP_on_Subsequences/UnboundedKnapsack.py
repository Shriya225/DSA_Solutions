# GFG
#memoization
class Solution:
    def knapSack(self, vals, wts, limit):
        def knapsack_memo(wts,vals,limit,index,dp):
            if limit==0 or index<0:
                return 0
            if dp[index][limit]!=-1:return dp[index][limit]
            l=0
            if limit-wts[index]>=0:
                l=knapsack_memo(wts,vals,limit-wts[index],index,dp)+vals[index]
            r=knapsack_memo(wts,vals,limit,index-1,dp)
            dp[index][limit]=max(l,r)
            return dp[index][limit]
        dp=[[-1]*(limit+1) for i in range(len(vals))]
        return knapsack_memo(wts,vals,limit,len(wts)-1,dp)
   
# tabulation
def kanp_tab(v,w,l):
    dp=[[0]*(l+1) for i in range(len(v))]
    # base case
    for i in range(1,l+1):
        if w[0]<=i:
            dp[0][i] = (i // w[0]) * v[0]
    for i in range(1,len(w)):
        for j in range(l+1):
            left=0
            if w[i]<=j:
                left=dp[i][j-w[i]]+v[i]
            r=dp[i-1][j]
            dp[i][j]=max(left,r)
    return dp[-1][-1]


#space optimization...
# 1 arr only
# most optimal..
def kanp_tab(v,w,l):
    dp=[0]*(l+1)
    # base case
    for i in range(1,l+1):
        if w[0]<=i:
            dp[i] = (i // w[0]) * v[0]
    # tabulate
    for i in range(1,len(w)):
        for j in range(l+1):
            left=0
            if w[i]<=j:
                left=dp[j-w[i]]+v[i]
            r=dp[j]
            dp[j]=max(left,r)
    return dp[-1]