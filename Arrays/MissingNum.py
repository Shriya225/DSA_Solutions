def missingNum(a):
    temp=[-1]*(len(a)+1)
    for i in range(len(a)):
        temp[a[i]]=0
    for i in range(len(temp)):
        if temp[i]==-1:
            print("missing num is:",i)
b=list(map(int,input("a:").split()))
missingNum(b)