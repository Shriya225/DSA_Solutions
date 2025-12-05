
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
n=int(input("n:"))
print("fact is:",fact(n))

def revStr(s):
    ans=''
    for i in range(len(s)):
        ans+=s[len(s)-i-1]
    return ans
s=input("s:")
print("rev is:",revStr(s))

def recurStr(s2,i=0):
    if i==len(s2):
        return ""
    return recurStr(s2,i+1)+s2[i]
s2=input("s:")
print("rev is:",recurStr(s2))

def toh(n,s='A',h='B',d='C'):
    if n==1:
        print(f"move disk {n} from {s} to {d}")
        return
    toh(n-1,s,d,h)
    print(f"move disk {n} from {s} to {d}")
    toh(n-1,h,s,d)
toh(3)


def mergearrs(a,b):
    i=j=0
    ans=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            ans.append(a[i])
            i+=1
        elif a[i]>b[j]:
            ans.append(b[j])
            j+=1
        else:
            ans.append(a[i])
            ans.append(a[i])
            i+=1
            j+=1
    while i<len(a):
        ans.append(a[i])
        i+=1
    while j<len(b):
        ans.append(b[j])
        j+=1
    print(ans)

a=list(map(int,input("a:").split()))
b=list(map(int,input("b:").split()))
mergearrs(a,b)


def setBits(n):
    c=0
    while n>0:
        n&=n-1
        c+=1
    print("setbits:",c)
n=int(input("n:"))
setBits(n)


def bs(a,l,h,t):
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            return m
        elif a[m]>t:
            h=m-1
        else:
            l=m+1
    return -1
def bs(a,l,h,t):
    if l>h:
        return -1
    m=(l+h)//2
    if a[m]==t:
        return m
    elif a[m]>t:
        return bs(a,l,m-1,t)
    else:
        return bs(a,m+1,h,t)
a=list(map(int,input("a:").split()))
t=int(input("t:"))
print(bs(a,0,len(a)-1,t))


def nonRepeating(s):
    d=dict()
    for i in s:
        d[i]=d.get(i,0)+1
    for i in s:
        if d[i]==1:
            print(i)
            return
    print("none")
    
s=input("S:")
nonRepeating(s)

def isPali(s):
    l,h=0,len(s)-1
    while l<h:
        if s[l]!=s[h]:
            return False
        l+=1
        h-=1
    return True

s=input("S:")
print(isPali(s))

def bs(a,l,h,t):
    if l>h:
        return -1
    m=(l+h)//2
    if a[m]==t:
        return m
    elif a[m]>t:
        return bs(a,l,m-1,t)
    else:
        return bs(a,m+1,h,t)

