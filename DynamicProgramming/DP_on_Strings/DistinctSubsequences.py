# 115. Distinct Subsequences

# reccurence rel'n

class Solution:
    def numDistinct(self, a: str, b: str) -> int:
        def ds(a,b,i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            if a[i]==b[j]:
                return ds(a,b,i-1,j-1)+ds(a,b,i-1,j)
            return ds(a,b,i-1,j)
        return ds(a,b,len(a)-1,len(b)-1)

# memoization
class Solution:
    def numDistinct(self, a: str, b: str) -> int:
        def ds(a,b,i,j,dp):
            if j<0:
                return 1
            if i<0:
                return 0
            if dp[i][j]!=-1:return dp[i][j]
            if a[i]==b[j]:
                dp[i][j]=ds(a,b,i-1,j-1,dp)+ds(a,b,i-1,j,dp)
                return dp[i][j]
            dp[i][j]=ds(a,b,i-1,j,dp)
            return dp[i][j]
        dp=[[-1]*len(b) for i in range(len(a))]
        return ds(a,b,len(a)-1,len(b)-1,dp)
    
# tabultaion
class Solution:
    def numDistinct(self, a: str, b: str) -> int:
        dp=[[0]*(len(b)+1) for i in range(len(a)+1)]
        # BASE CASE
        for i in range(len(a)+1):
            dp[i][0]=1
        for i in range(1,len(a)+1):
            for j in range(1,len(b)+1):
                if a[i-1]==b[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
    
# space optimization

class Solution:
    def numDistinct(self, a: str, b: str) -> int:
        dp=[0]*(len(b)+1)
        dp[0]=1
        for i in range(1,len(a)+1):
            x=[0]*(len(b)+1)
            x[0]=1
            for j in range(1,len(b)+1):
                if a[i-1]==b[j-1]:
                    x[j]=dp[j-1]+dp[j]
                else:
                    x[j]=dp[j]
            dp=x
        return dp[-1]


# 1D array optimization...
class Solution:
    def numDistinct(self, a: str, b: str) -> int:
        dp=[0]*(len(b)+1)
        dp[0]=1
        for i in range(1,len(a)+1):
            # go reverse to fill the array up...
            for j in range(len(b),0,-1):
                if a[i-1]==b[j-1]:
                    dp[j]=dp[j-1]+dp[j]
        return dp[-1]

    