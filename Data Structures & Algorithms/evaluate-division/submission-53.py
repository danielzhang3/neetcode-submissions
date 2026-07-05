class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (A, B), k in zip(equations, values): 
            graph[A].append((B, k))
            graph[B].append((A, 1.0 / k))
        
        def dfs(c, d, visited): 
            if c not in graph or d not in graph: 
                return -1.0
            if c == d: 
                return 1.0
            visited.add(c)
            for nei, weight in graph[c]: 
                if nei not in visited: 
                    result = dfs(nei, d, visited)
                    if result != -1.0: 
                        return weight * result
            return -1.0
        
        res = []
        for c, d in queries: 
            res.append(dfs(c, d, set()))
        
        return res

        