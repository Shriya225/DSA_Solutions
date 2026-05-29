# 1043. Partition Array for Maximum Sum

# T(n)=T(n−1)+T(n−2)+T(n−3)

# which grows exponentially.

# TC= O(3^n)
# SC-depth of recursion ,O(n) worst case
def pas(a,i,j):
    if i>j:
        return 0
    ans=float('-inf')
    x=a[i]
    for k in range(3):
        if i+k>j:break
        x=max(x,a[i+k])
        ans=max(ans,(x*(k+1))+pas(a,i+k+1,j))
    return ans

# Memoization
class Solution:
    def maxSumAfterPartitioning(self, a, l: int) -> int:
        def pas(a,i,j,dp):
            if i>j:
                return 0
            if dp[i]!=-1:return dp[i]
            ans=float('-inf')
            x=a[i]
            for k in range(l):
                if i+k>j:break
                x=max(x,a[i+k])
                ans=max(ans,(x*(k+1))+pas(a,i+k+1,j,dp))
            dp[i]=ans
            return ans
        dp=[-1]*len(a)
        return pas(a,0,len(a)-1,dp)

# Tabulation
def pas(a,l):
    dp=[0]*(len(a)+1)
    for i in range(len(a)-1,-1,-1):
            ans=float('-inf')
            x=a[i]
            for k in range(l):
                if i+k>len(a)-1:break
                x=max(x,a[i+k])
                ans=max(ans,(x*(k+1))+dp[i+k+1])
            dp[i]=ans
    return dp[0]