# LIS 2nd appraoch fr dp

# Ending at inedx i approach...

# recursive sol'n
class Solution:
    def lengthOfLIS(self, a):
        def h(a,i):
            ans=1
            for j in range(i):
                if a[j]<a[i]:
                    ans=max(ans,1+h(a,j))
            return ans
        ans=1
        for i in range(len(a)):
            ans=max(ans,h(a,i))
        return ans

# memoization
    def lengthOfLIS(self, a):
        def h(a,i,dp):
            ans=1
            if dp[i]!=0 :return dp[i]
            for j in range(i):
                if a[j]<a[i]:
                    ans=max(ans,1+h(a,j,dp))
            dp[i]=ans
            return ans
        ans=1
        dp=[0]*len(a) 
        for i in range(len(a)):
            ans=max(ans,h(a,i,dp))
        return ans
    
# Tabulation
def lis(a):
    n=len(a)
    dp=[1]*n
    ans=0
    for i in range(n):
        for j in range(i):
            if a[j]<a[i]:
                dp[i]=max(dp[i],1+dp[j])
        ans=max(ans,dp[i])
    return ans

# printing LIS
def lis(a):
    n=len(a)
    dp=[1]*n
    bt=[-1]*n
    ans=0
    li=0
    for i in range(n):
        for j in range(i):
            if a[j]<a[i]:
                if 1+dp[j]>dp[i]:
                    dp[i]= 1+dp[j]
                    if bt[i]==-1:
                        bt[i]=[j]

        if dp[i]>ans:
            ans=dp[i]
            li=i
        ans=max(ans,dp[i])

    # backtracks..
    ans=[]
    while li>=0:
        ans.append(a[li])
        li=bt[li]
    return ans[::-1]



