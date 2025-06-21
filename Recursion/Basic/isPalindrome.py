# Time Complexity: O(n), where n = len(s) — each pair is compared once.

# Space Complexity: O(n) due to recursion stack.


def isPalindrome(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return isPalindrome(s,l+1,r-1)
s=input("s:")
print(isPalindrome(s,0,len(s)-1))
