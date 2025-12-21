def merge(a, l, m, r):
    i = l
    j = m + 1
    temp = []

    while i <= m and j <= r:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    while i <= m:
        temp.append(a[i])
        i += 1

    while j <= r:
        temp.append(a[j])
        j += 1

    a[l:r+1] = temp
def mergesort(a, l, r):
    if l < r:
        m = (l + r) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)
        merge(a, l, m, r)
a = list(map(int, input("a: ").split()))
mergesort(a, 0, len(a) - 1)
print(a)
