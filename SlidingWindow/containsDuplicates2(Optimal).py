# Fixed Size Sliding Window Problem!!!!

# so this problem can also be solved using dictionary alone,
# but takes SC-O(n),
# using Sliding window reduces it to O(k)

def dups2(a,k):
        l=0
        s=set()
        for r in range(len(a)):
            if r-l>k:
                s.remove(a[l])
                l+=1
            if a[r] in s:
                    return True   
            s.add(a[r])
        return False



a=list(map(int,input("a:").split()))
k=int(input("k:"))
print(dups2(a,k))