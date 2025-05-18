def SortColors(a):
    Zeroes=0
    for i in range(len(a)):
        if a[i]==0:
            a[Zeroes],a[i]=a[i],a[Zeroes]
            Zeroes+=1
    ones=Zeroes
    for i in range(Zeroes,len(a)):
        if a[i]==1:
            a[ones],a[i]=a[i],a[ones]
            ones+=1
    print("ans",a)
    
l=list(map(int,input("A:").split()))
SortColors(l)