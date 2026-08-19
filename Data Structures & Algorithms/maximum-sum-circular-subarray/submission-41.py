class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min, curr_max = 0, 0
        globMin, globMax = nums[0], nums[0]
        total = 0
        
        for num in nums: 
            curr_min = min(num, num + curr_min)
            curr_max = max(num, num + curr_max)
            total += num
            globMin = min(curr_min, globMin)
            globMax = max(curr_max, globMax)
        
        if globMax >= 0: 
            return max(globMax, total - globMin)
        
        return globMax