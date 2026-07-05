class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par): 
            if node in visited: 
                return False
            visited.add(node)
            for nei in adj[node]: 
                if nei == par: 
                    continue
                if not dfs(nei, node): 
                    return False
            return True
        
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if not dfs(u, -1): 
                return [u, v]


        