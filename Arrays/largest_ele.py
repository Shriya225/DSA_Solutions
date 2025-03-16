def largest_ele(a):
    l=a[0]
    for i in range(len(a)):
        if a[i]>l:
            l=a[i]
    print("largest element in the array is:",l)
a=list(map(int,input("a:").split()))
largest_ele(a)