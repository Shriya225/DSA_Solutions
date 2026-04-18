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


# tabulation
# space O(n*4)
def nt_tab(a):
    dp=[[-1]*4 for _ in range(len(a))]
    dp[0][0]=max(a[0][1],a[0][2])
    dp[0][1]=max(a[0][0],a[0][2])
    dp[0][2]=max(a[0][1],a[0][0])
    dp[0][3]=max(a[0][1],a[0][2],a[0][0])

    for day in range(1,len(a)):
        for last in range(4):
            ans=float("-inf")
            for task in range(3):
                if task!=last:
                    ans=max(ans,a[day][task]+dp[day-1][task])
            dp[day][last]=ans
    return dp[len(a)-1][-1]


# tabulation
# space Optitmized
# tc- O(n*4*3)
# sc-O(4)
def nt_tab(a):
    dp=[-1]*4
    dp[0]=max(a[0][1],a[0][2])
    dp[1]=max(a[0][0],a[0][2])
    dp[2]=max(a[0][1],a[0][0])
    dp[3]=max(a[0][1],a[0][2],a[0][0])

    for day in range(1,len(a)):
        x=[-1]*4
        for last in range(4):
            ans=float("-inf")
            for task in range(3):
                if task!=last:
                    ans=max(ans,a[day][task]+dp[task])
            x[last]=ans
        dp=x
    return dp[-1]

