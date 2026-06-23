# Count numbers in range N

# memoized sol'n
# only for tight=False we need to memoize 
def countN(a):
    a=str(a)
    dp=[-1]*(len(a)+1)
    def rec(pos,t):
        if not t:
            if dp[pos]!=-1:
                return dp[pos]
        if pos==len(a):
            return 1
        l=9 if not t else int(a[pos])
        ans=0
        for d in range(l+1):
            nt=t and (d==l)
            ans+=rec(pos+1,nt)
        if not t:
            dp[pos]=ans
        return ans
    return rec(0,True)
a=int(input('a:'))
b=int(input('b:'))
print(countN(b)-countN(a)+1)
print(countN(b)-countN(a-1))