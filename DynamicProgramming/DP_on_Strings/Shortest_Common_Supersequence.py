# 1092. Shortest Common Supersequence 

class Solution:
    def shortestCommonSupersequence(self, a,b) -> str:
       
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
        # return dp[-1][-1]
        

        # backtrack from lsat nad figure out hw t osarrange other tahn lCS elements in answer.
        p,q=n,m
        ans=""
        while p>0 and q>0:
            if a[p-1]==b[q-1]:
                ans+=a[p-1]
                p-=1
                q-=1
            elif dp[p][q-1]>dp[p-1][q]:
                ans+=b[q-1]
                q-=1
            else:
                ans+=a[p-1]
                p-=1
        while p>0:
             ans+=a[p-1]
             p-=1
        while q>0:
             ans+=b[q-1]
             q-=1
        return ans[::-1]
                 
                  