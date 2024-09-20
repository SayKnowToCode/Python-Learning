from typing import List

class Solution:
    def minPathSumRecursion(self, grid: List[List[int]]) -> int:
        def recursion(r:int,c:int) -> int:
            if r < 0 or c < 0:
                return float('inf')
            if r == 0 and c == 0:
                return grid[0][0]
            
            up = grid[r][c] + recursion(r-1,c)
            left = grid[r][c] + recursion(r,c-1)

            return min(up,left)

        return recursion(len(grid)-1,len(grid[0])-1)
    
    def minPathSumMemoization(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[-1]*(n) for _ in range(m)]

        def recursion(r:int,c:int) -> int:
            if r < 0 or c < 0:
                return float('inf')
            if r == 0 and c == 0:
                dp[0][0] = grid[0][0]
                return grid[0][0]
            
            up = left = grid[r][c]
            if r-1 >= 0 and dp[r-1][c] != -1:
                up += dp[r-1][c]
            else:
                up += recursion(r-1,c)

            if c-1 >= 0 and dp[r][c-1] != -1:
                left += dp[r][c-1]
            else:
                left += recursion(r,c-1)

            dp[r][c] = min(up,left)
            return min(up,left)

        ans = recursion(m-1,n-1)
        # print(dp)
        return ans
    
    def minPathSumTabulation(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*(n) for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = left = float('inf')
                if i-1>=0:
                    up = dp[i-1][j]
                if j-1>=0:
                    left = dp[i][j-1]

                dp[i][j] = grid[i][j] + min(up,left)

        return dp[m-1][n-1]
    
    def minPathSumSpaceOptimization(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')]*n
        dummy = [0] * n
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dummy[0] = grid[0][0]
                    continue
                
                left = float('inf')
                up = dp[j]
                if j>0:
                    left = dummy[j-1]
                
                dummy[j] = grid[i][j] + min(left,up)
            
            dp = dummy
        
        return dp[n-1]

        

ob = Solution()
print("Recursion")
print(ob.minPathSumRecursion([[1,3,1],[1,5,1],[4,2,1]]))
print(ob.minPathSumRecursion([[1,2,3],[4,5,6]]))
print(ob.minPathSumRecursion([[1,2,3]]))
print("Memoization")
print(ob.minPathSumMemoization([[1,3,1],[1,5,1],[4,2,1]]))
print(ob.minPathSumMemoization([[1,2,3],[4,5,6]]))
print(ob.minPathSumMemoization([[1,2,3]]))
print("Tabulation")
print(ob.minPathSumTabulation([[1,3,1],[1,5,1],[4,2,1]]))
print(ob.minPathSumTabulation([[1,2,3],[4,5,6]]))
print(ob.minPathSumTabulation([[1,2,3]]))  
print("SpaceOptimization")
print(ob.minPathSumSpaceOptimization([[1,3,1],[1,5,1],[4,2,1]]))
print(ob.minPathSumSpaceOptimization([[1,2,3],[4,5,6]]))
print(ob.minPathSumSpaceOptimization([[1,2,3]]))
print(ob.minPathSumSpaceOptimization([[3]]))
print(ob.minPathSumSpaceOptimization([[3],[3]]))
