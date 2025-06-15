# 1446. Consecutive Characters
def consecutiveChars(s):
    char=''
    c=maxc=0
    for i in range(len(s)):
        if s[i]==char:
            c+=1
        else:
            c=1
            char=s[i]
        maxc=max(c,maxc)
    print("power",maxc)
s=input("s:")
consecutiveChars(s)