class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        while low < high: 
            mid = (low + high) // 2
            total_days, cur = 1, 0

            for w in weights: 
                if cur + w > mid: 
                    total_days += 1
                    cur = 0
                cur += w
            
            if total_days <= days: 
                high = mid
            else: 
                low = mid + 1
        
        return low
        