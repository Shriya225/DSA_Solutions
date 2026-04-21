# Minimum sum partition (GFG)

# tabulation...

# space optimization..
# 2D ---> 1D


# this is getting TLE in GFG!!!!!!
def subseq_tab(a):
    k=sum(a)
    dp=[-1]*(k+1)
    # base case
    for i in range(k+1):
        if i==0:
            dp[0]=True
        else:
            dp[i]=True if a[0]==i else False
    # tabulate..
    for i in range(1,len(a)):
        x=[-1]*(k+1)
        for j in range(k+1):
            if j==0:
                x[0]=True
            else:
                l=r=False
                l=dp[j]
                if j-a[i]>=0:
                    r=dp[j-a[i]]
                x[j]=l or r
        dp=x
    ans=float("inf")
    # last row in tbale giving answer.
    for i in range(k+1):
        if dp[i]:
            ans=min(ans,abs(i-(k-i)))
    return ans


# this is workign in GFG
# most optimal one..
class Solution:
    def minDifference(self, a):
        k = sum(a)
        
        dp = [False] * (k + 1)
        dp[0] = True
        
        for num in a:
            # this loop is super smart...that backward one & ony looping till num too...
            for j in range(k, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        ans = float("inf")
        
        for i in range(k // 2 + 1):
            if dp[i]:
                ans = min(ans, k - 2 * i)
        
        return ans
