# 455. Assign Cookies
def cookies(g,c):
    l=r=0
    g.sort()
    c.sort()
    while l<len(g) and r<len(c):
        if g[l]<=c[r]:
            l+=1
        r+=1
    return l
g=list(map(int,input("g:").split()))
c=list(map(int,input("c:").split()))
print(cookies(g,c))