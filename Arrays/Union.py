def union(a,b):
        freq = {}
        union = []
        
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        for num in b:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq:
            union.append(num)
        union.sort() 
        # o(nlogn)
        print(union)

a=list(map(int,input("a:").split()))
b=list(map(int,input("a:").split()))
union(a,b)