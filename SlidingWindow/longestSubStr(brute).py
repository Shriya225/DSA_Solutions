# Brute force
# o(n^2)
# 3. Longest Substring Without Repeating Characters
def longestSubstr(s):
    ans=float('-inf')
    if not ans:
        return 0
    for i in range(len(s)):
        d=dict()
        for j in range(i,len(s)):
            if s[j] in d:
                break
            d[s[j]]=1
            ans=max(ans,j-i+1)
    return ans
s=input("s:")
print(longestSubstr(s))