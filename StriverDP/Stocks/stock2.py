from typing import List

class Solution:
    def stocks2Recursion(self, prices: List[int]) -> int:
        def recursion(i : int,buy : int) -> int:
            if i == len(prices):
                return 0
            
            if buy == 1:
                bought = -prices[i] + recursion(i+1,0)
                left = 0 + recursion(i+1,1)
                return max(bought,left)
            else:
                sell = prices[i] + recursion(i+1,1)
                hold = 0 + recursion(i+1,0)
                return max(sell,hold)

        if len(prices) > 1:
            return recursion(0,1)
        else:
            return 0
        
    def stocks2Memoization(self, prices: List[int]) -> int:
        dp = [[-1]*2 for _ in range(len(prices))]

        def recursion(i : int,buy : int) -> int:
            if i == len(prices):
                return 0
            
            if dp[i][buy] != -1:
                return dp[i][buy]
            
            if buy:
                bought = -prices[i] + recursion(i+1,0)
                left = 0 + recursion(i+1,1)
                dp[i][buy] = max(bought,left)
                return max(bought,left)
            else:
                sell = prices[i] + recursion(i,1)
                hold = 0 + recursion(i+1,0)
                dp[i][buy] = max(sell,hold)
                return max(sell,hold)

        if len(prices) > 1:
            return recursion(0,1)
        else:
            return 0

ob = Solution()
print(ob.stocks2Recursion([7,1,5,3,6,4])) # 7
print(ob.stocks2Recursion([1,2,3,4,5])) # 4
print(ob.stocks2Recursion([7,6,4,3,1])) # 0

print(ob.stocks2Memoization([7,1,5,3,6,4])) # 7
print(ob.stocks2Memoization([1,2,3,4,5])) # 4
print(ob.stocks2Memoization([7,6,4,3,1])) # 0