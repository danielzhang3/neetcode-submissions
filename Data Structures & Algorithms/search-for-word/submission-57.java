class Solution {
    public boolean exist(char[][] board, String word) {
        int ROWS = board.length, COLS = board[0].length;
        boolean[][] visited = new boolean[ROWS][COLS];

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (dfs(r, c, 0, board, word, visited) == true) return true;
            }
        }
        return false;
    }
    public boolean dfs(int r, int c, int i, char[][] board, String word, boolean[][] visited) {
        if (i == word.length()) return true;

        if (r < 0 || r == board.length || c < 0 || c == board[0].length) return false;
        if (board[r][c] != word.charAt(i) || visited[r][c] == true) return false;

        visited[r][c] = true;
        boolean result = (dfs(r + 1, c, i + 1, board, word, visited) ||
                          dfs(r - 1, c, i + 1, board, word, visited) ||
                          dfs(r, c + 1, i + 1, board, word, visited) ||
                          dfs(r, c - 1, i + 1, board, word, visited));
        visited[r][c] = false;
        return result;
    }
}
