from typing import List

class Solution:
    def coinChange2Recursion(self,coins : List[int],target : int) -> int :
        def recursion(index : int,t : int) -> int:
            if index == 0:
                if t % coins[0] == 0:
                    return 1
                else:
                    return 0
                
            non_pick = recursion(index-1,t)
            pick = 0
            if t >= coins[index] :
                pick = recursion(index,t - coins[index])
            
            return pick+non_pick

        return recursion(len(coins)-1,target)
    
    def coinChange2Tabulation(self,coins : List[int],target : int) -> int :
        dp = [[float('inf')]*(target+1) for _ in range(len(coins))]

        for j in range(target+1):
            if coins[0] == j:
                dp[0][j] = 1
        
        for i in range(1,len(coins)):
            for j in range(target+1):
                non_pick = dp[i-1][j]
                pick = dp[i][j]
                if j >= coins[i] :
                    pick = 1 + dp[i][j - coins[i]]
                
                dp[i][j] = min(pick,non_pick)
        
        return dp[-1][-1]
    
ob = Solution()
print(ob.coinChange2Recursion([1,2,5],5))
print(ob.coinChange2Recursion([1,2,5],11))