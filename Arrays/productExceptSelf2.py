# most optimal soln
# 238. Product of Array Except Self
# prefix&suffix Product
# o(1)-sc
# without using // operator...
def productExceptSelf(a):
    n=len(a)
    prefixproduct=1
    suffixProduct=1
    ans=[1]*n
    for i in range(n):
        prefixproduct*=a[i]
        suffixProduct*=a[n-i-1]
        if i+1<n:
            ans[i+1]*=prefixproduct
        if n-i-2>=0:
            ans[n-i-2]*=suffixProduct
    
        print(ans)
    print(ans)
#other way...
def productExceptSelf(nums):
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]
        return output
l=list(map(int,input("A:").split()))
productExceptSelf(l)