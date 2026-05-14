# 1547. Minimum Cost to Cut a Stick

# Reccurence rel'n

class Solution:
    def minCost(self, n: int, a):
        def mcs(a,i,j):
            if i>j:return 0
            ans=float("inf")
            for k in range(i,j+1):
                ans=min(ans,a[j+1]-a[i-1]+mcs(a,i,k-1)+mcs(a,k+1,j))
            return ans
        a.sort()
        a=[0]+a+[n]
        return mcs(a,1,len(a)-2)
    
# Memoization

class Solution:
    def minCost(self, n: int, a):
        def mcs(a,i,j):
            if i>j:return 0
            if dp[i][j]!=-1:return dp[i][j]
            ans=float("inf")
            for k in range(i,j+1):
                ans=min(ans,a[j+1]-a[i-1]+mcs(a,i,k-1)+mcs(a,k+1,j))
            dp[i][j]=ans
            return ans
        a.sort()
        a=[0]+a+[n]
        dp=[[-1]*len(a) for i in range(len(a))]
        return mcs(a,1,len(a)-2)
    
# Tabulation
    def minCost(self, n: int, a):
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        for i in range(m - 2, 0, -1):

            for j in range(i, m - 1):

                ans = float("inf")

                for k in range(i, j + 1):

                    cost = (
                        cuts[j + 1] - cuts[i - 1]
                        + dp[i][k - 1]
                        + dp[k + 1][j]
                    )

                    ans = min(ans, cost)

                dp[i][j] = ans

        return dp[1][m - 2]
    



# My approach..try it once
cuts=[]
def solve(left, right, l, r):

    if l > r:
        return 0

    ans = float("inf")

    for k in range(l, r + 1):

        cost = (
            right - left
            + solve(left, cuts[k], l, k - 1)
            + solve(cuts[k], right, k + 1, r)
        )

        ans = min(ans, cost)

    return ans
    
