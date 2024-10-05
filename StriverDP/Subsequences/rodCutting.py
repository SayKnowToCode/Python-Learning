from typing import List

class Solution:
    def rodCuttingRecursion(self,prices:List[int]) -> int :
        n = len(prices)
        def recursion(index : int, length : int) -> int:
            if length == 0:
                return 0
            
            if index == 0:
                return (length * prices[0])

            non_pick = recursion(index-1,length)
            pick = 0
            if index+1 <= length:
                pick = prices[index] + recursion(index-1,length - (index + 1))
            
            return max(pick,non_pick)

        return recursion(n-1,n)

    def rodCuttingTabulation(self,prices:List[int]) -> int:
        n = len(prices)
        dp = [[0]*(n+1) for _ in range(n)]

        for j in range(1,n+1):
            dp[0][j] = j * prices[0]

        for i in range(n):
            for j in range(1,n+1):
                non_pick = dp[i-1][j]
                pick = 0
                if i+1 <= j:
                    pick = prices[i] + dp[i-1][j-(i+1)]
                
                dp[i][j] = max(pick,non_pick)
        
        return dp[-1][-1]
    
ob = Solution()
print(ob.rodCuttingRecursion([1,5,8,9,10,17,17,20])) # 22
print(ob.rodCuttingRecursion([2,5,7,8,10])) # 24

print(ob.rodCuttingTabulation([1,5,8,9,10,17,17,20])) # 22
print(ob.rodCuttingTabulation([2,5,7,8,10])) # 24