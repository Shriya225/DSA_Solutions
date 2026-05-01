# 44. Wildcard Matching

# reccurence rel'n

# my version...(used a loop fr * considered characters...)(Crct but exponential....)
def wm(a,p,i,j):
    if j<0 and i<0:
        return True
    if j<0:
        return False
    if i<0:
        for k in range(j + 1):
            if p[k] != '*':
                return False
        return True
    
    ans=False
    if a[i]==p[j] or  p[j]=='?':
        return wm(a,p,i-1,j-1)

    if p[j]=='*': 
        # used a loop
        for k in range(i+1): ans=ans or wm(a,p,i-k,j-1) 
    return ans


# standard optiaml reccurence..
def wm(a,p,i,j):
    if j<0 and i<0:
        return True
    if j<0:
        return False
    if i<0:
        for k in range(j + 1):
            if p[k] != '*':
                return False
        return True
    
    ans=False
    if a[i]==p[j] or  p[j]=='?':
        return wm(a,p,i-1,j-1)
    # pcik or not pick taht charcter fr * cateogry 
    # ex: ab def cs ,p=ab*cd
    if p[j]=='*':   
        return wm(a, p, i, j-1) or wm(a, p, i-1, j)
    return ans


# memoization

class Solution:
    def isMatch(self, a,p) -> bool:
        def wm(a,p,i,j,dp):
            if j<0 and i<0:
                return True
            if j<0:
                return False
            if i<0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True
            
            if dp[i][j]!=-1:return dp[i][j]
            
            ans=False
            if a[i]==p[j] or  p[j]=='?':
                return wm(a,p,i-1,j-1,dp)
            # pcik or not pick taht charcter fr * cateogry 
            # ex: ab def cs ,p=ab*cd
            if p[j]=='*':   
                return wm(a, p, i, j-1,dp) or wm(a, p, i-1, j,dp)
            dp[i][j]=ans
            return ans
        dp=[[-1]*len(p) for i in range(len(a))]
        return wm(a,p,len(a)-1,len(p)-1,dp)


# Tabualtion... 
class Solution:
        def isMatch(self, a,p) -> bool:
            dp=[[False]*(len(p)+1) for i in range(len(a)+1)]
            # base case
            dp[0][0]=True
            for i in range(1,len(p)+1):
                if p[i-1]=='*':
                    dp[0][i]=True and dp[0][i-1]

            # fill dp
            for i in range(1,len(a)+1):
                for j in range(1,len(p)+1):
                    if a[i-1]==p[j-1] or  p[j-1]=='?':
                                dp[i][j]=dp[i-1][j-1]
                                # pcik or not pick taht charcter fr * cateogry 
                                # ex: ab def cs ,p=ab*cd
                    if p[j-1]=='*': 
                        dp[i][j]=dp[i][j-1] or dp[i-1][j]  
            return dp[-1][-1]

# space optimized....
class Solution:
        def isMatch(self, a,p) -> bool:
            dp=[False]*(len(p)+1) 
            # base case
            dp[0]=True
            for i in range(1,len(p)+1):
                if p[i-1]=='*':
                    dp[i]=True and dp[i-1]

            # fill dp
            for i in range(1,len(a)+1):
                x=[False]*(len(p)+1) 
                for j in range(1,len(p)+1):
                    if a[i-1]==p[j-1] or  p[j-1]=='?':
                                x[j]=dp[j-1]
                    if p[j-1]=='*': 
                        x[j]=x[j-1] or dp[j]  
                dp=x
            return dp[-1]

