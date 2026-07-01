class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, target, time in times: 
            graph[src].append((target, time))
        
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        
        visited = set()
        maxTime = 0

        def expand(src, time):
            for nei, t in graph[src]: 
                new_time = time + t
                heapq.heappush(minHeap, (new_time, nei))

        while minHeap: 
            time, node = heapq.heappop(minHeap)
            if node in visited: 
                continue
            visited.add(node)
            maxTime = max(maxTime, time)
            expand(node, time)

        return maxTime if len(visited) == n else -1 

        