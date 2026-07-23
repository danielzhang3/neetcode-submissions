class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]: 
            if start <= prev_end: 
                prev_end = max(prev_end, end)
            else: 
                res.append((prev_start, prev_end))
                prev_start, prev_end = start, end
        
        res.append((prev_start, prev_end))

        return res
        