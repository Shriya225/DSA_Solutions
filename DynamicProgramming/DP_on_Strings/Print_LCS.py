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
    

# tabulation...
# from length of longest LCS ..we r trying to find out LCS.
class Solution:
    def longestCommonSubsequence(self,a,b) -> int:
        n, m = len(a), len(b)
        dp = [[0]*(m+1) for _ in range(n+1)]
        # fill dp
        for i in range(1,n+1):
            for j in range(1,m+1):
                l=r=0
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                        l=dp[i-1][j]
                        r=dp[i][j-1]  
                        dp[i][j]=max(l,r)
        
        # backtrack to find LCS
        # iterative version...
        x,y=n,m
        ans=""
        while x>0 and y>0:
            if a[x-1]==b[y-1]:
                ans=a[x-1]+ans
                x-=1
                y-=1
                continue
            l=dp[x-1][y]
            r=dp[x][y-1]
            if l>r:
                x-=1
            else:
                y-=1
        # return ans
    
        # backtrackign...recursion version....
        def bt(x,y):
            if x<=0 or y<=0:
                return ""
            if a[x-1]==b[y-1]:
                ans=a[x-1]+bt(x-1,y-1)
            else:
                l=dp[x-1][y]
                r=dp[x][y-1]
                if l>r:
                    ans=bt(x-1,y)
                    ans=bt(x-1,y)
                elif l<r:
                    ans=bt(x,y-1)
                else:
                    ans=bt(x,y-1)
                    ans=bt(x-1,y)

            return ans


