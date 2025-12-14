# N meetings in one room
# gfg
def Nmeetings(s,e):
    l=[[s[i],e[i]] for i in range(len(s))]
    l.sort(key=lambda x:x[1])
    ans=0
    prev_endtime=-1
    i=0
    while i<len(l):
        if l[i][0]>prev_endtime:
            ans+=1
            prev_endtime=l[i][1]
        else:
            i+=1
    return ans


s=list(map(int,input("c:").split()))
e=list(map(int,input("c:").split()))
print(Nmeetings(s,e))