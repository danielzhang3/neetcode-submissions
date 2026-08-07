class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]: 
            graph[src].append(dst)
        
        res = []

        def dfs(src): 
            while graph[src]: 
                dst = graph[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs('JFK')
        return res[::-1]
        