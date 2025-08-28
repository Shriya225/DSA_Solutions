def romanToInteger(s):
    d1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    d2={"V":"I","X":"I","L":"X","C":"X","D":"C","M":"C"}
    ans=0
    i=len(s)-1
    while i>=0:
        if s[i]!="I" and i!=0 and s[i-1]==d2[s[i]]:
            ans+=d1[s[i]]-d1[d2[s[i]]]
            i-=1
        else:
            ans+=d1[s[i]]
        i-=1
    return ans


s=input()
print(romanToInteger(s))