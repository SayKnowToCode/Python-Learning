class Solution:
    def Recursion3D(self, n, m, grid):

        def recursion(row : int, c1 : int, c2 : int) -> int:
            if c1 < 0 or c2 < 0 or c1 == m or c2 == m:
                return 0
                
            if row == n-1 :
                if c1 != c2 :
                    return grid[row][c1] + grid[row][c2]
                else :
                    return grid[row][c1]
            
            if c1 != c2 :
                one = recursion(row+1,c1-1,c2-1)
                two = recursion(row+1,c1-1,c2)
                three = recursion(row+1,c1-1,c2+1)
                four = recursion(row+1,c1,c2-1)
                five = recursion(row+1,c1,c2)
                six = recursion(row+1,c1,c2+1)
                seven = recursion(row+1,c1+1,c2-1)
                eight = recursion(row+1,c1+1,c2)
                nine = recursion(row+1,c1+1,c2+1)
                return grid[row][c1] + grid[row][c2] + max(one,two,three,four,five,six,seven,eight,nine)
            
            else :
                one = recursion(row+1,c1-1,c2-1)
                two = recursion(row+1,c1-1,c2)
                three = recursion(row+1,c1-1,c2+1)
                four = recursion(row+1,c1,c2-1)
                five = recursion(row+1,c1,c2)
                six = recursion(row+1,c1,c2+1)
                seven = recursion(row+1,c1+1,c2-1)
                eight = recursion(row+1,c1+1,c2)
                nine = recursion(row+1,c1+1,c2+1)
                return grid[row][c1] + max(one,two,three,four,five,six,seven,eight,nine)
                
        return recursion(0,0,m-1)
    
    def Tabulation3D(self, n, m, grid):
        dp = [[[0] * (m+2) for _ in range(m+2)] for _ in range(n)]

        i = n-1
        while(i >= 0):
            for j in range(1,m+1):
                for k in range(1,m+1):

                    if i == n-1:
                        if j != k:
                            dp[i][j][k] = grid[i][j-1] + grid[i][k-1]
                        else:
                            dp[i][j][k] = grid[i][j-1]
                        continue

                    if j != k:
                        one = dp[i+1][j-1][k-1]
                        two = dp[i+1][j-1][k]
                        three = dp[i+1][j-1][k+1]
                        four = dp[i+1][j][k-1]
                        five = dp[i+1][j][k]
                        six = dp[i+1][j][k+1]
                        seven = dp[i+1][j+1][k-1]
                        eight = dp[i+1][j+1][k]
                        nine = dp[i+1][j+1][k+1]
                        dp[i][j][k] = grid[i][j-1] + grid[i][k-1] + max(one,two,three,four,five,six,seven,eight,nine)
                    else:
                        one = dp[i+1][j-1][k-1]
                        two = dp[i+1][j-1][k]
                        three = dp[i+1][j-1][k+1]
                        four = dp[i+1][j][k-1]
                        five = dp[i+1][j][k]
                        six = dp[i+1][j][k+1]
                        seven = dp[i+1][j+1][k-1]
                        eight = dp[i+1][j+1][k]
                        nine = dp[i+1][j+1][k+1]
                        dp[i][j][k] = grid[i][j-1] + max(one,two,three,four,five,six,seven,eight,nine)
            i -= 1
        
        return dp[0][1][m]


ob = Solution()
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(ob.Recursion3D(4,3,grid)) # 24
print(ob.Tabulation3D(4,3,grid)) # 24
