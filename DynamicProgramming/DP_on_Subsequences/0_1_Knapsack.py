
#reccurence rel'n
def Knapsack(wts,vals,limit,index):
    if limit==0 or index<0:
        return 0
    l=0
    if limit-wts[index]>=0:
        l=Knapsack(wts,vals,limit-wts[index],index-1)+vals[index]
    r=Knapsack(wts,vals,limit,index-1)
    return max(l,r)

# memoizaton
def knapsack_memo(wts,vals,limit,index,dp):
    if limit==0 or index<0:
        return 0
    if dp[index][limit]!=-1:return dp[index][limit]
    l=0
    if limit-wts[index]>=0:
        l=knapsack_memo(wts,vals,limit-wts[index],index-1,dp)+vals[index]
    r=knapsack_memo(wts,vals,limit,index-1,dp)
    dp[index][limit]=max(l,r)
    return dp[index][limit]

# tabulation
def kanp_tab(v,w,l):
    dp=[[0]*(l+1) for i in range(len(v))]
    # base case
    for i in range(1,l+1):
        if w[0]<=i:
            dp[0][i]=v[0]
    for i in range(1,len(w)):
        for j in range(l+1):
            left=0
            if w[i]<=j:
                left=dp[i-1][j-w[i]]+v[i]
            r=dp[i-1][j]
            dp[i][j]=max(left,r)
    return dp[-1][-1]


#space optimization...
def kanp_tab(v,w,l):
    dp=[0]*(l+1)
    # base case
    for i in range(1,l+1):
        if w[0]<=i:
            dp[i]=v[0]
    # tabulate
    for i in range(1,len(w)):
        for j in range(l,-1,-1):
            left=0
            if w[i]<=j:
                left=dp[j-w[i]]+v[i]
            r=dp[j]
            dp[j]=max(left,r)
    return dp[-1]

    




    

