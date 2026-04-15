# ninja training
# recurrence reln
# O(3^n)-tc
def nt(a,d,l=-1):
    if d<0:return 0
    ans=float('-inf')
    for i in range(3):
        if i!=l:
            x=a[d][i]+nt(a,d-1,i)
            ans=max(ans,x)
    return ans


# memoization
def nt(a,d,l,dp):
    if d<0:return 0
    if dp[d][l]!=-1:return dp[d][l]
    ans=float('-inf')
    for i in range(3):
        if i!=l:
            x=a[d][i]+nt(a,d-1,i,dp)
            ans=max(ans,x)
    dp[d][l]=ans
    return ans
