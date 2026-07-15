class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        current = []
        trips.sort(key=lambda x:x[1])
        current_load = 0

        for num, start, end in trips: 
            while current and current[0][0] <= start: 
                prev_end, num_pass = heapq.heappop(current)
                current_load -= num_pass
            
            heapq.heappush(current, (end, num))
            current_load += num

            if current_load > capacity: 
                return False
        
        return True
        