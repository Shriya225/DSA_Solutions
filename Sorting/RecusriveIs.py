
def ris(a,i,n):
    if n==0 or n==1:
        return a
    if i==n:
        return a
    if a[i]<a[i-1]:
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return ris(a,i+1,n)

a=list(map(int,input("a:").split()))
print(ris(a,1,len(a)))


# standard verion of recursiuon.
def recursive_insertion_sort(arr, n):
    # Base case: single element is always sorted
    if n <= 1:
        return

    # Sort first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    # Insert last element at its correct position in sorted subarray
    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..n-2], that are greater than last, to one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

# Example usage:
a = list(map(int, input("a: ").split()))
recursive_insertion_sort(a, len(a))
print(a)
