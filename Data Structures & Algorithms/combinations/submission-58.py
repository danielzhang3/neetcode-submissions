class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = [], []

        def dfs(start): 
            if len(path) == k: 
                res.append(path.copy())
                return
            
            for end in range(start, n + 1): 
                path.append(end)
                dfs(end + 1)
                path.pop()
        
        dfs(1)
        return res
        