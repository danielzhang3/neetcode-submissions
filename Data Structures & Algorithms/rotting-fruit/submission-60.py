class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        fresh = 0

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2: 
                    q.append((r, c))
        
        time = 0

        while q and fresh > 0: 
            for _ in range(len(q)): 
                r, c = q.popleft()
                for dr, dc in directions: 
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and col in range(COLS) and
                        grid[row][col] == 1): 
                        q.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
        