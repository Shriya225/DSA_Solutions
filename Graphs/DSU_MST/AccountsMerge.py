from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, a: List[List[str]]) -> List[List[str]]:
        d = dict()
        n = len(a)
        
        parent = [i for i in range(n)]
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            
            if px == py:
                return
            
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
        
        # Step 1: Union accounts sharing emails
        for i in range(n):
            for j in range(1, len(a[i])):
                email = a[i][j]          # FIXED indexing
                if email in d:
                    union(i, d[email])
                else:
                    d[email] = i
        
        # Step 2: Group emails by root
        root_to_emails = defaultdict(list)
        
        for email, acc_index in d.items():
            root = find(acc_index)
            root_to_emails[root].append(email)
        
        # Step 3: Build result
        result = []
        
        for root, emails in root_to_emails.items():
            name = a[root][0]
            result.append([name] + sorted(emails))
        
        return result
