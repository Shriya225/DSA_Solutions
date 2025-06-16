def largestAndSmallest(a):
    l=float('-inf')
    s=float('inf')
    print("onf",float("inf"))
    for i in range(len(a)):
        if a[i]>l:
            l=a[i]
        if a[i]<s:
            s=a[i]
    print("l=",l,"s:",s)

def secondLargestAndSmallest(a):
    l=sl=float("-inf")
    s=ss=float('inf')
    for i in range(len(a)):
        if a[i]>l:
            sl=l
            l=a[i]
        elif l>a[i]>sl:
            sl=a[i]
        if a[i]<s:
            ss=s
            s=a[i]
        elif s<a[i]<ss:
            ss=a[i]
    print(f"l={l},sl={sl}")
    print(f"s={s},ss={ss}")
l=list(map(int,input("a:").split()))
largestAndSmallest(l)
secondLargestAndSmallest(l)