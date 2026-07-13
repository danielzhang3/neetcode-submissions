class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [(-cnt) for (ch, cnt) in count.items()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q: 
            time += 1
            if not max_heap: 
                time = q[0][1]
            else: 
                cnt = heapq.heappop(max_heap) + 1
                if cnt < 0: 
                    q.append((cnt, time + n))
            if q and q[0][1] == time: 
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time

        
        