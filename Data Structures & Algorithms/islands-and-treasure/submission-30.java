class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;
        int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        Deque<int[]> q = new ArrayDeque<>();

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 0) q.offerLast(new int[]{r, c});
            }
        }

        int current_distance = 0;

        while (!q.isEmpty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                int[] pair = q.pollFirst();
                int r = pair[0], c = pair[1];

                for (int[] d : dir) {
                    int row = r + d[0], col = c + d[1];
                    if (row < 0 || row == ROWS || col < 0 || col == COLS) continue;
                    if (grid[row][col] != 2147483647) continue;

                    grid[row][col] = current_distance + 1;
                    q.offerLast(new int[]{row, col});
                }
            }
            current_distance++;
        }
        
    }
}
