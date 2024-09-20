from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0]*(n)
        dummy = [0]*n
        for i in range(m):
            for j in range(n):
                if i==0 and j==0 and obstacleGrid[i][j] == 0:
                    dummy[0] = 1
                    continue

                if obstacleGrid[i][j] == 1:
                    dummy[j] = 0
                    continue

                up = dp[j]
                left = 0
                if j > 0:
                    left = dummy[j-1]

                dummy[j] = up + left

            dp = dummy

        return dp[n-1] 

ob = Solution()
print(ob.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(ob.uniquePathsWithObstacles([[0,1],[0,0]]))
print(ob.uniquePathsWithObstacles([[1]]))