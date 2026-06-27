class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        connected = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROWS): 
            if board[r][0] == "O": 
                q.append((r, 0))
                connected.add((r, 0))
            if board[r][COLS - 1] == "O": 
                q.append((r, COLS - 1))
                connected.add((r, COLS - 1))
        for c in range(COLS): 
            if board[0][c] == "O": 
                q.append((0, c))
                connected.add((0, c))
            if board[ROWS - 1][c] == "O": 
                q.append((ROWS - 1, c))
                connected.add((ROWS - 1, c))
        
        while q: 
            r, c = q.popleft()
            for dr, dc in directions: 
                row, col = r + dr, c + dc
                if (row in range(ROWS) and col in range(COLS) and board[row][col] == "O"
                    and (row, col) not in connected): 
                    q.append((row, col))
                    connected.add((row, col))
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == "O" and (r, c) not in connected: 
                    board[r][c] = "X"