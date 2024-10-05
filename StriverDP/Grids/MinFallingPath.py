from typing import List

class Solution:
    def minPathSumRecursion(self,triangle : List[List[int]]) -> int:

        def recursion(r:int,c:int) -> int:
            value = triangle[r][c]
            if r == len(triangle) - 1:
                return value
            
            one = recursion(r+1,c)
            two = three = float('inf')

            if c != len(triangle) - 1:
                two = recursion(r+1,c+1)
            
            if c != 0:
                three = recursion(r+1,c-1)

            return value + min(one,two,three)

        minimum = float('inf')
        for i in range(len(triangle[0])):
            minimum = min(minimum,recursion(0,i))
        return minimum
    

    def minPathSumMemoization(self,triangle : List[List[int]]) -> int:
        dp = [[-1]*len(triangle) for _ in range(len(triangle))]
        
        def recursion(r:int,c:int) -> int:
            value = triangle[r][c]
            if r == len(triangle) - 1:
                dp[r][c] = value
                return value
            
            if dp[r+1][c] != -1:
                one = dp[r+1][c]
            else:
                one = recursion(r+1,c)

            two = three = float('inf')

            if c != len(triangle) - 1:
                if dp[r+1][c+1] != -1:
                    two = dp[r+1][c+1]
                else:
                    two = recursion(r+1,c+1)

            if c != 0:
                if dp[r+1][c-1] != -1:
                    three = dp[r+1][c-1]
                else:
                    three = recursion(r+1,c-1)

            dp[r][c] = value + min(one,two,three)
            return value + min(one,two,three)
        
        minimum = float('inf')
        for i in range(len(triangle)):
            minimum = min(minimum,recursion(0,i))
        return minimum

    def minPathTabulation(self,triangle : List[List[int]]) -> int:
        dp = [[-1]*len(triangle) for _ in range(len(triangle))]

        dp[-1] = triangle[-1]
        i = len(triangle) - 2
        while i >= 0:
            for j in range(len(triangle)):
                one = dp[i+1][j]
                two = three = float('inf')
                if j != len(triangle) - 1:
                    two = dp[i+1][j+1]
                if j != 0:
                    three = dp[i+1][j-1]
                
                dp[i][j] = triangle[i][j] + min(one,two,three)
            i -= 1
        
        return min(dp[0])

    
    def minPathTabulationOptimized(self,triangle : List[List[int]]) -> int:
        dp = triangle[-1]
        i = len(triangle) - 2
        while i >= 0:
            dummy = triangle[i]

            for j in range(len(triangle)):
                one = dp[j]
                two = three = float('inf')
                if j != len(triangle) - 1:
                    two = dp[j+1]
                if j != 0:
                    three = dp[j-1]
                
                dummy[j] = dummy[j] + min(one,two,three)

            dp = dummy
            i -= 1
        
        return min(dp)
    
ob = Solution()
print(ob.minPathSumRecursion([[2,1,3],[6,5,4],[7,8,9]]))
print(ob.minPathSumRecursion([[-19,57],[-40,-5]]))
print(ob.minPathSumMemoization([[2,1,3],[6,5,4],[7,8,9]]))
print(ob.minPathSumMemoization([[-19,57],[-40,-5]]))

print(ob.minPathTabulation([[2,1,3],[6,5,4],[7,8,9]]))
print(ob.minPathTabulation([[-19,57],[-40,-5]]))

print(ob.minPathTabulationOptimized([[2,1,3],[6,5,4],[7,8,9]]))
print(ob.minPathTabulationOptimized([[-19,57],[-40,-5]]))
print(ob.minPathTabulationOptimized([[7]]))
