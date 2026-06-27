class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        
        def dfs(node):
            for nei in graph[node]:
                if not visited[nei]: 
                    visited[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n): 
            if not visited[node]: 
                visited[node] = True
                dfs(node)
                res += 1
        
        return res

        