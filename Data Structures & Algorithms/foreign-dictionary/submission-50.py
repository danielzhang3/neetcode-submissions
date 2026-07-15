class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indeg = {}
        for word in words: 
            for c in word: 
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
                        indeg[c2] = 1 + indeg.get(c2, 0)
                    break
    
        q = deque()
        for c in indeg: 
            if indeg[c] == 0: 
                q.append(c)
        res = []

        while q: 
            cur = q.popleft()
            res.append(cur)
            for nei in graph[cur]: 
                indeg[nei] -= 1
                if indeg[nei] == 0: 
                    q.append(nei)
        
        return "".join(res) if len(res) == len(indeg) else ""

        