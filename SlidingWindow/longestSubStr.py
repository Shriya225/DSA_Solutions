# 3. Longest Substring Without Repeating Characters
# O(n)
def longestSubstr2(s):
            ans=float('-inf')
            if not s:
                return 0
            l=r=0
            d=dict()
            for r in range(len(s)):
                if s[r] in d:
                    while s[r] in d:
                        d.pop(s[l])
                        l=l+1
                    d[s[r]]=1
                else:
                    d[s[r]]=1
                ans=max(ans,r-l+1)

            return ans
s=input("s:")
print(longestSubstr2(s))