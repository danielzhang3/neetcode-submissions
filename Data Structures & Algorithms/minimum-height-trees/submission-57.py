class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: 
            return [0]
        
        graph = defaultdict(list)
        edge_cnt = {}
        q = deque()

        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        
        for src, nei in graph.items(): 
            edge_cnt[src] = len(nei)
            if len(nei) == 1: 
                q.append(src)
        
        while q: 
            if n <= 2: 
                return list(q)
            for i in range(len(q)): 
                cur = q.popleft()
                n -= 1
                for nei in graph[cur]: 
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1: 
                        q.append(nei)

        