
def firstOccurence(a,t,i=0):
    if i==len(a):
        return -1
    if a[i]==t:
        return i
    return firstOccurence(a,t,i+1)
a=list(map(int,input("a:").split()))
t=int(input())
print(firstOccurence(a,t))