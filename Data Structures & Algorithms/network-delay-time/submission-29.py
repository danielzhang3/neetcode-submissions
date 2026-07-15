class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, target, time in times: 
            graph[src].append((target, time))
        
        heap = []
        visited = set()
        heapq.heappush(heap, (0, k))
        maxTime = 0

        def expand(src, time): 
            for nei, t in graph[src]: 
                new_time = time + t
                heapq.heappush(heap, (new_time, nei))
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited: 
                continue
            visited.add(node)
            maxTime = max(maxTime, time)
            expand(node, time)
        
        return maxTime if len(visited) == n else -1
            

        