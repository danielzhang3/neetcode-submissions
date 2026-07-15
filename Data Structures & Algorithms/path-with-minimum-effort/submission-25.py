class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = []
        heapq.heappush(heap, (0, 0, 0))

        while heap: 
            eff, r, c = heapq.heappop(heap)
            if (r, c) in visited: 
                continue
            if (r == ROWS - 1 and c == COLS - 1): 
                return eff
            visited.add((r, c))
            for dr, dc in directions: 
                row, col = r + dr, c + dc
                if (row in range(ROWS) and col in range(COLS) and (row, col) not in visited): 
                    newEff = abs(heights[row][col] - heights[r][c])
                    maxEff = max(eff, newEff)
                    heapq.heappush(heap, (maxEff, row, col))


        