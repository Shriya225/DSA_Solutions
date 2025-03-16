def smallest_ele(a):
    smallest=a[0]
    for i in range(len(a)):
        if a[i]<smallest:
            smallest=a[i]
    print("samllest element is:",smallest)
a=list(map(int,input("a:").split()))
smallest_ele(a)