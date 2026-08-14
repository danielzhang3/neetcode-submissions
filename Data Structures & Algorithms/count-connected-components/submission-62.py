class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)
        
        res = 0
        
        def dfs(node): 
            for nei in adj[node]: 
                if not visited[nei]: 
                    visited[nei] = True
                    dfs(nei)

        for node in range(n): 
            if not visited[node]: 
                visited[node] = True
                dfs(node)
                res += 1
        
        return res
        