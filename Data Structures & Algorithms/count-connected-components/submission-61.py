class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n

        def dfs(node): 
            for nei in adj[node]: 
                if visited[nei] == False: 
                    visited[nei] = True
                    dfs(nei)
        
        res = 0

        for node in range(n): 
            if visited[node] == False: 
                visited[node] = True
                dfs(node)
                res += 1
        
        return res
        