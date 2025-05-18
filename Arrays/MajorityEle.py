# Moore's Voting Algorithm
# O(n)-tc & o(1)-sc
def MajorityEle(a):
    ele=a[0]
    cnt=1
    for i in range(1,len(a)):
        if cnt==0:
            ele=a[i]
            cnt=1
        elif a[i]==ele:
            cnt+=1
        else:
            cnt-=1
    c=0
    for i in range(1,len(a)):
        if a[i]==ele:
            c+=1
    if c>(len(a)//2):
        return ele
l=list(map(int,input("A:".split())))
MajorityEle(l)