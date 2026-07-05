class Solution {
    public int orangesRotting(int[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;
        Deque<int[]> q = new ArrayDeque<>();
        int fresh = 0;
        int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) fresh++;
                if (grid[r][c] == 2) q.offerLast(new int[]{r, c});
            }
        }

        int time = 0;
        while (!q.isEmpty() && fresh > 0) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                int[] pair = q.pollFirst();
                int r = pair[0], c = pair[1];

                for (int[] d : dir) {
                    int row = r + d[0], col = c + d[1];
                    if (row < 0 || row == ROWS || col < 0 || col == COLS) continue;
                    if (grid[row][col] != 1) continue;

                    grid[row][col] = 2;
                    fresh--;
                    q.offerLast(new int[]{row, col});
                }
            }
            time++;
        }
        
        if (fresh != 0) return -1;
        return time;
    }
}
