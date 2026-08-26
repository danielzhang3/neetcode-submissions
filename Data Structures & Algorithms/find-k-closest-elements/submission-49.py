class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - k

        while l < r: 
            m = (l + r) // 2
            left_gap = x - arr[m]
            right_gap = arr[m + k] - x

            if left_gap > right_gap: 
                l = m + 1
            else: 
                r = m
        
        return arr[l: l + k]
        