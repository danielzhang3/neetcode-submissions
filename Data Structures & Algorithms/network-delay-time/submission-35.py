class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, target, time in times: 
            adj[src].append((target, time))
        
        heap = []
        heapq.heappush(heap, (0, k))
        maxTime = 0

        def neighbors(src, time): 
            for nei, t in adj[src]: 
                new_time = time + t
                heapq.heappush(heap, (new_time, nei))
        
        visited = set()

        while heap: 
            time, node = heapq.heappop(heap)
            if node in visited: 
                continue
            visited.add(node)
            neighbors(node, time)
            maxTime = max(maxTime, time)
        
        return maxTime if len(visited) == n else -1
        