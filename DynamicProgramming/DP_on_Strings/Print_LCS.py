# Longest Common Subsequence
# Print LCS

# reccurence rel'n
def lcs(a,b,i,j):
    if i<0 or j<0:
        return ""
    if a[i]==b[j]:
        return lcs(a,b,i-1,j-1)+a[i]
    l=lcs(a,b,i-1,j)
    r= lcs(a,b,i,j-1)
    return l if len(l)>len(r) else r

# memoization
class Solution:
    def longestCommonSubsequence(self,a,b) -> int:
        def lcs(a,b,i,j,dp):
            if i<0 or j<0:
                return ""
            if dp[i][j]!=-1:return dp[i][j]
            if a[i]==b[j]:
                dp[i][j]=lcs(a,b,i-1,j-1,dp)+a[i]
            else:
                l=lcs(a,b,i-1,j,dp)
                r= lcs(a,b,i,j-1,dp)
                dp[i][j]=l if len(l)>len(r) else r
            return dp[i][j]
        n, m = len(a), len(b)
        dp = [[-1]*m for _ in range(n)]
        return lcs(a,b,len(a)-1,len(b)-1,dp)
    
