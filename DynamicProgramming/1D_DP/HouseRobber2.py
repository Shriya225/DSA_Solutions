
def hr_opt(a):
    prev2 = 0
    prev1 = a[0]
    
    for i in range(1, len(a)):
        pick = a[i] + prev2
        skip = prev1
        
        curr = max(pick, skip)
        
        prev2 = prev1
        prev1 = curr
    
    return prev1

def hr2(a):
    if len(a)==1:
        return a[0]
    s=hr_opt(a[:len(a)-1])
    s2=hr_opt(a[1:])
    return max(s,s2)