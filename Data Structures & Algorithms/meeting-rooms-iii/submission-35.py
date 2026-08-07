class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [i for i in range(n)]
        meetings.sort()
        used = []
        res = [0] * n

        for start, end in meetings: 
            while used and used[0][0] <= start: 
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available: 
                end_time, room = heapq.heappop(used)
                heapq.heappush(available, room)
                end = end_time + (end - start)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            res[room] += 1

        return res.index(max(res)) 
        