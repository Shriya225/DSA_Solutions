# 435. Non-overlapping Intervals
def nonOverlapping(a):
    a.sort(key=lambda x:x[1])
    c=0
    prev=a[0][0]
    for i in range(len(a)):
        if a[i][0]>=prev:
            prev=a[i][1]
        else:
            c+=1
    return c
            


e=list(map(int,input("c:").split()))
print(nonOverlapping(e))