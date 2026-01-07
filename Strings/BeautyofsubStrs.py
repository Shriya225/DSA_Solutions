# 1781. Sum of Beauty of All Substrings
def baeuty(s):
    ans=0
    for i in range(len(s)):
        d=[0]*26
        for j in range(i,len(s)):
            d[ord(s[j])-ord('a')]+=1
            min_freq=float("inf")
            for x in d:
                if x!=0:
                    min_freq=min(min_freq,x)
            ans+=max(d)-min_freq

    return ans


s=input("s:")
print(baeuty(s))


# tc -o(n*2)
# sc o(1)   atmost 26 alph and atm ost 26 so it is sonstant 
def baeuty(s):
    ans=0
    for i in range(len(s)):
        d=dict()
        for j in range(i,len(s)):
            d[s[j]]=d.get(s[j],0)+1
            if len(d)>1:
                x=d.values()
                ans+=max(x)-min(x)
    return ans


s=input("s:")
print(baeuty(s))




# prefix sum logic
# same tc o(n^2) but logic d crazy check it out.
def beautySum(s: str) -> int:
    n = len(s)

    # prefix[i][c] = frequency of char c in s[0 : i]
    prefix = [[0]*26 for _ in range(n+1)]

    # build prefix frequency
    for i in range(n):
        prefix[i+1] = prefix[i].copy()
        prefix[i+1][ord(s[i]) - ord('a')] += 1

    ans = 0

    # generate all substrings
    for i in range(n):
        for j in range(i, n):
            mx = 0
            mn = float('inf')

            # compute freq of substring s[i..j]
            for c in range(26):
                freq = prefix[j+1][c] - prefix[i][c]
                if freq > 0:
                    mx = max(mx, freq)
                    mn = min(mn, freq)

            ans += mx - mn

    return ans
