class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        row = [0] * (n + 1)
        row[n - 1] = 1

        for i in range(m - 1, -1, -1): 
            for j in range(n - 1, -1, -1): 
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                else: 
                    row[j] = row[j] + row[j + 1]

        return row[0] 

        