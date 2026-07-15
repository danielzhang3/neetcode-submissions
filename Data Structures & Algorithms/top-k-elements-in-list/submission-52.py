class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)
        for num in count: 
            cnt = count[num]
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1): 
            for num in freq[i]: 
                res.append(num)
                if len(res) == k: 
                    return res
        

        