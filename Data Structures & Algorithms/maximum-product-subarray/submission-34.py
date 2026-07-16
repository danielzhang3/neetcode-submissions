class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMin, prevMax = nums[0], nums[0]
        res = nums[0]

        for i in range(1, len(nums)): 
            num = nums[i]
            currMin = min(num, num * prevMin, num * prevMax)
            currMax = max(num, num * prevMin, num * prevMax)
            res = max(res, currMax)
            prevMin, prevMax = currMin, currMax
        
        return res


        