# 1759. Count Number of Homogenous Substrings

def HomogenousSubstrs(s):
    ans = 0
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            ans += count * (count + 1) // 2
            count = 1

    ans += count * (count + 1) // 2
    return ans




def HomogenousSubstrs(a):
    ans=0
    d=dict()
    for i in range(len(a)):
        if not d:
            d[a[i]]=1
        elif len(d)==1 and a[i] not in d:
            x=sum(d.values())
            print(x)
            ans+=(x*(x+1)//2)
            d.clear()
            d[a[i]]=1
        else:
            d[a[i]]+=1
    x=sum(d.values())
    ans+=(x*(x+1)//2)
    return ans

a=input("s:")
print(HomogenousSubstrs(a))