# Count numbers ≤ N whose digit sum = K
def countN(a,k):
    a=str(a)
    dp=dict()
    def rec(pos,t,s):
        # pruning technique..
        if s>k:return 0
        # memoize
        if not t:
            if (pos,s) in dp:
                return dp[(pos,s)]
        # base case
        if pos==len(a):
            return 1 if s==k else 0
        # limit
        l=9 if not t else int(a[pos])
        ans=0
        # enumerate
        for d in range(l+1):
            nt=t and (d==l)
            ans+=rec(pos+1,nt,s+d)
        if not t:
            dp[(pos,s)]=ans
        return ans
    return rec(0,True,0)
a=int(input('a:'))
b=int(input('b:'))
k=int(input('k:'))

# print(countN(b)-countN(a)+1)
print(countN(b,k)-countN(a-1,k))