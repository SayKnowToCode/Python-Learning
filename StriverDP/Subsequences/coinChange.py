from typing import List

class Solution:
    def coinChangeRecursion(self,coins : List[int],target : int) -> int :
        def recursion(index : int,t : int) -> int:
            if t == 0 :
                return 1
            
            if index == 0:
                if t % coins[0] == 0:
                    return t // coins[0]
                else:
                    return float('inf')
                
            non_pick = recursion(index-1,t)
            pick = float('inf')
            if t >= coins[index] :
                pick = 1 + recursion(index,t - coins[index])
            
            
            return min(pick,non_pick)

        ans = recursion(len(coins)-1,target)
        if ans == float('inf'):
            return -1
        else:
            return ans
    
    def coinChangeTabulation(self,coins : List[int],target : int) -> int :
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
    
    def coinChangeSuperSpaceOptimized(self,coins : List[int],target : int) -> int :
        dp = [float('inf')]*(target +1)

        for j in range(target+1):
            if j % coins[0] == 0:
                dp[j] = j // coins[0]
        
        for i in range(1,len(coins)):
            for j in range(target+1):
                non_pick = dp[j]
                pick = float('inf')
                if j >= coins[i]:
                    pick = 1 + dp[j - coins[i]]
                
                dp[j] = min(pick,non_pick)
        
        return dp[-1]
    
ob = Solution()
print(ob.coinChangeRecursion([1,2,5],11))
print(ob.coinChangeTabulation([1,2,5],11))
print(ob.coinChangeSuperSpaceOptimized([1,2,5],11))