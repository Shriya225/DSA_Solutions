from collections import deque
# GFG
class Solution:
    def findOrder(self, words):

        # 1. collect all characters (nodes)
        chars = set()
        for w in words:
            for ch in w:
                chars.add(ch)

        # 2. build graph
        adj = {ch: [] for ch in chars}
        indegree = {ch: 0 for ch in chars}

        # 3. build edges using adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # invalid prefix case
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""

            l = min(len(w1), len(w2))
            for j in range(l):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break

        # 4. topo sort (Kahn)
        q = deque()
        for ch in chars:
            if indegree[ch] == 0:
                q.append(ch)

        ans = []

        while q:
            x = q.popleft()
            ans.append(x)
            for nei in adj[x]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # 5. cycle check
        if len(ans) != len(chars):
            return ""

        return "".join(ans)

    
