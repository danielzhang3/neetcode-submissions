class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin, currMax = 0, 0
        globMin, globMax = nums[0], nums[0]
        total = 0

        for num in nums: 
            currMin = min(num, num + currMin)
            currMax = max(num, num + currMax)
            total += num
            globMin = min(globMin, currMin)
            globMax = max(globMax, currMax)
        
        if globMax >= 0: 
            return max(globMax, total - globMin)
        
        return globMax
        