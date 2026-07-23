class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indeg = {}
        for w in words: 
            for c in w: 
                indeg[c] = 0
        
        for i in range(len(words) - 1): 
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2): 
                return ""
            
            for j in range(min(len(w1), len(w2))): 
                c1, c2 = w1[j], w2[j]
                
                if c1 != c2: 
                    if c2 not in graph[c1]: 
                        graph[c1].add(c2)
                        indeg[c2] += 1
                    break
        
        q = deque()
        for ch in indeg: 
            if indeg[ch] == 0: 
                q.append(ch)
        res = ""

        while q: 
            cur = q.popleft()
            res += cur
            for nei in graph[cur]: 
                indeg[nei] -= 1
                if indeg[nei] == 0: 
                    q.append(nei)
        
        return res if len(res) == len(indeg) else ""

        