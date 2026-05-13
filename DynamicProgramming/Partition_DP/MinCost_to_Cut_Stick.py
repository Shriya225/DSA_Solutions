# 1547. Minimum Cost to Cut a Stick

# Reccurence rel'n

def mcs(a,i,j):
    if i==j:return 1
    ans=float("inf")
    for k in range(i,j):
        ans=min(ans,(j-i)+mcs(a,i,k-1)+mcs(a,k+1,j))
    return ans
