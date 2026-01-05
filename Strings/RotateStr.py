# at each point check if this is roatted point
def rotateString( s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i:]+s[:i]==t:
                return True
        return False
        