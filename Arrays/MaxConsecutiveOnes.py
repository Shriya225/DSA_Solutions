def maxConsecutiveOnes(a):
    c=maxc=0
    for i in range(len(a)):
        if a[i]==1:
            c+=1
            maxc=max(maxc,c)
        if a[i]==0:
            c=0
    print("maxc",maxc)

l=list(map(int,input("a:").split()))
maxConsecutiveOnes(l)