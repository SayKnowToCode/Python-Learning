class Solution:
    def uniquePathsRecursion(self, m: int, n: int) -> int:
        def recursion(r : int, c : int) -> int:
            if r < 0 or c < 0:
                return 0
            if r==0 and c==0:
                return 1
            
            left = recursion(r,c-1)
            up = recursion(r-1,c)

            return up+left
        
        return recursion(m-1,n-1)
    
    def uniquePathsMemoization(self, m: int, n: int) -> int:
        dp = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0
        # print(dp)

        def recursion(r : int, c : int) -> int:
            if r==1 and c==1:
                return 1
            
            if dp[r][c-1] != -1:
                left = dp[r][c-1]
            else:
                left = recursion(r,c-1)
            
            if dp[r-1][c] != -1:
                up = dp[r-1][c]
            else:
                up = recursion(r-1,c)
            
            dp[r][c] = up+left
            return up+left
        
        ans = recursion(m,n)
        # print(dp)
        return ans
    
    def uniquePathsTabulation(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] =dp[i-1][j] + dp[i][j-1]

        return dp[m][n]
    
    def uniquePathsSpaceOptimization(self, m: int, n: int) -> int:
        dp = [0]*(n)
        dummy = [0]*n
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dummy[0] = 1
                    continue

                up = dp[j]
                left = 0
                if j > 0:
                    left = dummy[j-1]

                dummy[j] = up + left

            dp = dummy

        return dp[n-1] 
                

    
ob = Solution()
print(ob.uniquePathsRecursion(3,3))
print(ob.uniquePathsMemoization(3,3))
print(ob.uniquePathsTabulation(3,3))
print("Testing")
print(ob.uniquePathsSpaceOptimization(3,3))
print(ob.uniquePathsSpaceOptimization(1,1))
print(ob.uniquePathsSpaceOptimization(2,2))
print(ob.uniquePathsSpaceOptimization(7,45))