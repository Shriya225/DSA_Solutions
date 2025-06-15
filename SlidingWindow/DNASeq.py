# 187. Repeated DNA Sequences

def DNA(s):
    ans=[]
    d=dict()
    l=0
    for r in range(len(s)):
        if r-l+1>10:
            l+=1
        if r-l+1==10:
            if s[l:r+1] in d:
                if s[l:r+1] not in ans:
                    ans.append(s[l:r+1])
            else:
                d[s[l:r+1]]=1
        
    return ans

s=input("s:")
print(DNA(s))