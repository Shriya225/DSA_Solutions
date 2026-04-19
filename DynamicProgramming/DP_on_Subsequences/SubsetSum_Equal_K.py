# GFG
# subset sum eual k(only +ve integrges)
# any subseq in arr sums to taget k


# reccurence re'n
# O(~2^n)(we prune some when t<0)
def subseq_k(a,i,t):
    if t==0:
        return True
    # if values are +ve
    if t<0:
        return False
    if i<0:
        return False
    l=subseq_k(a,i-1,t-a[i]) 
    r=subseq_k(a,i-1,t)
    # print(l or r ,f"subseq({a},{i},{t})")
    return l or r 
a=list(map(int,input("a:").split()))
print(subseq_k(a,len(a)-1,int(input("k:"))))


# memoization..
def subseq_k_memo(a,i,t,dp):
    if t==0:
        return True
    # if values are +ve
    if t<0:
        return False
    if i<0:
        return False
    if dp[i][t]!=-1:return dp[i][t]
    l=subseq_k_memo(a,i-1,t-a[i],dp) 
    r=subseq_k_memo(a,i-1,t,dp)
    # print(l or r ,f"subseq({a},{i},{t})")
    dp[i][t]=l or r
    return dp[i][t]
a=list(map(int,input("a:").split()))
k=int(input("k:"))
dp=[[-1]*(k+1) for _ in range(len(a))]
print(subseq_k_memo(a,len(a)-1,k,dp))


# tabualtion..
def subseq_tab(a,k):
    dp=[[-1]*(k+1) for _ in range(len(a))]
    # base case
    for i in range(k+1):
        if i==0:
            dp[0][0]=True
        else:
            dp[0][i]=True if a[0]==i else False
    # tabulate..
    for i in range(1,len(a)):
        for j in range(k+1):
            if j==0:
                dp[i][0]=True
            else:
                l=r=False
                l=dp[i-1][j]
                if j-a[i]>=0:
                    r=dp[i-1][j-a[i]]
                dp[i][j]=l or r
    return dp[len(a)-1][k]



# space optimization..
# 2D ---> 1D
def subseq_tab(a,k):
    dp=[-1]*(k+1)
    # base case
    for i in range(k+1):
        if i==0:
            dp[0]=True
        else:
            dp[i]=True if a[0]==i else False
    # tabulate..
    for i in range(1,len(a)):
        x=[-1]*(k+1)
        for j in range(k+1):
            if j==0:
                x[0]=True
            else:
                l=r=False
                l=dp[j]
                if j-a[i]>=0:
                    r=dp[j-a[i]]
                x[j]=l or r
        dp=x
    return dp[k]




    
