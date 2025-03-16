# Given an array of positive integers arr[],
#  return the second smallest element from the array. 
# If the second smallest element doesn't exist then return -1.

def second_smallest(a):
    s=ss=float('inf')
    for i in range(len(a)):
        if a[i]<s:
            ss=s
            s=a[i]
        elif a[i]>s and a[i]<ss:
            ss=a[i]
    ss=-1 if ss==float('inf') else ss
    print("second smallest is:",ss)
a=list(map(int,input("a:").split()))
second_smallest(a)