# Given an array of positive integers arr[],
#  return the second largest element from the array. 
# If the second largest element doesn't exist then return -1.


# Brute Force
# Tc- o(2n)
def second_largest_1(a):
    l=a[0]
    for i in range(len(a)):
        if a[i]>l:
            l=a[i]
    
    sl=-1
    for i in range(len(a)):
        if a[i]>sl and a[i]<l:
            sl=a[i]
    print("second largest element is:",sl)


# optimal solution
# Tc-o(n)
def second_largest(a):
    l=-1
    sl=-1
    for i in range(len(a)):
        if a[i]>l:
            sl=l
            l=a[i]
        elif a[i]>sl and a[i]<l:
            sl=a[i]
    print("second largest element is:",sl)

a=list(map(int,input("a:").split()))
second_largest(a)
second_largest_1(a)
