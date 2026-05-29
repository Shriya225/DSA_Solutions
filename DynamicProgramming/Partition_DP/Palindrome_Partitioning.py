# 132. Palindrome Partitioning II
# MCM style thinking
def pp2(a,i,j):
    if i>=j:return 0
    if a[i:j+1]==a[i:j+1][::-1]:return 0
    ans=float('inf')
    for k in range(i,j+1):
        ans=min(ans,1+pp2(a,i,k)+pp2(a,k+1,j))
    return ans

# Memoization
class Solution:
    def minCut(self, s: str) -> int:
        def pp2(a,i,j,dp):
            if i>=j:return 0
            if dp[i][j]!=-1:return dp[i][j]
            if a[i:j+1]==a[i:j+1][::-1]:return 0
            ans=float('inf')
            for k in range(i,j):
                ans=min(ans,1+pp2(a,i,k,dp)+pp2(a,k+1,j,dp))
            dp[i][j]=ans
            return ans
        dp=[[-1]*len(s) for i in range(len(s))]
        return pp2(s,0,len(s)-1,dp)

# Tabulation..
# Total:

# O(n⁴)

# Even with memoization/tabulation
class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        dp = [[0]*n for _ in range(n)]

        for i in range(n-1,-1,-1):

            for j in range(i+1,n):

                # already palindrome
                if s[i:j+1] == s[i:j+1][::-1]:
                    dp[i][j] = 0

                else:

                    ans = float('inf')

                    for k in range(i,j):

                        ans = min(
                            ans,
                            1 + dp[i][k] + dp[k+1][j]
                        )

                    dp[i][j] = ans

        return dp[0][n-1]
