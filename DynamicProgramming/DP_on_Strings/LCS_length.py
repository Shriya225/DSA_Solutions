# 1143. Longest Common Subsequence
# Print len of LCS

# reccurence rel'n
def lcs(a,b,i,j):
    if i<0 or j<0:
        return 0
    if a[i]==b[j]:
        return 1+lcs(a,b,i-1,j-1)
    return max(lcs(a,b,i-1,j),lcs(a,b,i,j-1))


# memoization
class Solution:
    def longestCommonSubsequence(self,a,b) -> int:
        def lcs(a,b,i,j,dp):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:return dp[i][j]
            if a[i]==b[j]:
                dp[i][j]=1+lcs(a,b,i-1,j-1,dp)
            else:
                dp[i][j]=max(lcs(a,b,i-1,j,dp),lcs(a,b,i,j-1,dp))
            return dp[i][j]
        n, m = len(a), len(b)
        dp = [[-1]*m for _ in range(n)]
        return lcs(a,b,len(a)-1,len(b)-1,dp)


# tabulation
class Solution:
    def longestCommonSubsequence(self,a,b) -> int:
        n, m = len(a), len(b)
        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            if b[i]==a[0]:
                dp[0][i]=1
            if i-1>=0 and dp[0][i-1]==1:
                dp[0][i]=1
        # fill dp
        for i in range(1,n):
            for j in range(m):
                l=r=0
                if a[i] == b[j]:
                    # check fr -ve indexing everywhere...
                    if j > 0:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    if i-1>=0:
                        l=dp[i-1][j]
                    if j-1>=0:
                        r=dp[i][j-1]  
                    dp[i][j]=max(l,r)
        return dp[-1][-1]


#space optimize....
class Solution:
    def longestCommonSubsequence(self, a, b) -> int:
        n, m = len(a), len(b)
        
        dp = [0]*m   # previous row

        # base case (row 0)
        for j in range(m):
            if a[0] == b[j]:
                dp[j] = 1
            elif j > 0:
                dp[j] = dp[j-1]

        # fill
        for i in range(1, n):
            x = [0]*m   # current row
            
            for j in range(m):
                if a[i] == b[j]:
                    if j > 0:
                        x[j] = 1 + dp[j-1]
                    else:
                        x[j] = 1
                else:
                    up = dp[j]
                    left = x[j-1] if j > 0 else 0
                    x[j] = max(up, left)
            
            dp = x   # move current → previous
        return dp[-1]