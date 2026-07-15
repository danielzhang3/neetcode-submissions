class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort(key=lambda x:x[0])

        heap = []
        i = 0
        res = [-1] * len(queries)

        for q, idx in queries: 
            while i < len(intervals) and intervals[i][0] <= q: 
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1
            
            while heap and heap[0][1] < q: 
                heapq.heappop(heap)
            
            if heap: 
                res[idx] = heap[0][0]
        
        return res
        