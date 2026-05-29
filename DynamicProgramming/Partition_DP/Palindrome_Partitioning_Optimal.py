# 132. Palindrome Partitioning II
# Front partitioning.... (Optimal ... 1D DP)
def pp(a,i):
    if i==len(a)-1:return 0
    ans=float('inf')
    for j in range(i,len(a)):
        if a[i:j+1]==a[i:j+1][::-1]:
            ans=min(ans,1+pp(a,j+1))
    return ans

# Memozation..
class Solution:
    def minCut(self, a: str) -> int:
        def pp(a,i,dp):
            if i>=len(a)-1:return 0
            if a[i:len(a)]==a[i:len(a)][::-1]:return 0
            if dp[i]!=-1:return dp[i]
            ans=float('inf')
            for j in range(i,len(a)):
                if a[i:j+1]==a[i:j+1][::-1]:
                    ans=min(ans,1+pp(a,j+1,dp))
            dp[i]=ans
            return ans
        dp=[-1]*(len(a))
        return pp(a,0,dp)
    
# Tabulation
class Solution:
    def minCut(self, a: str) -> int:
        dp=[0]*(len(a))
        for i in range(len(a)-2,-1,-1):
            if a[i:len(a)]==a[i:len(a)][::-1]:
                dp[i]=0
                continue
            ans=float('inf')
            for j in range(i,len(a)):
                    if a[i:j+1]==a[i:j+1][::-1]:
                        ans=min(ans,1+dp[j+1])
            dp[i]=ans
        return dp[0]

