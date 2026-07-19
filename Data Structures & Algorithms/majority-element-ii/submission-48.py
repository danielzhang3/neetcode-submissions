class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = {}

        for num in nums: 
            res[num] = 1 + res.get(num, 0)
            if len(res) <= 2: 
                continue
            
            newRes = defaultdict(int)
            for num, c in res.items(): 
                if c > 1: 
                    newRes[num] = c - 1
            res = newRes
        
        result = []
        for num in res: 
            if nums.count(num) > len(nums) // 3: 
                result.append(num)
        return result
        