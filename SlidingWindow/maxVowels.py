# 1456. Maximum Number of Vowels in a Substring of Given Length
def maxVowels(self, s: str, k: int) -> int:
        l=0
        d=dict()
        c=0
        ans=0
        for r in range(len(s)):
            if s[r] in 'aeiou':
                c+=1
            if r-l+1>k:
                if s[l] in 'aeiou':
                    c-=1
                l+=1
            if r-l+1==k:
                ans=max(ans,c)
        return ans