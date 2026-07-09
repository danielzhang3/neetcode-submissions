class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(heights): 
            start = i
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                start = index
                area = max(area, height * (i - index))
            stack.append((start, h))
        
        for i, h in stack: 
            area = max(area, h * (len(heights) - i))
        
        return area
        