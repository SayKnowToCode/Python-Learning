from typing import List

class Solution:
    def stocks2Recursion(self, prices: List[int]) -> int:
        def recursion(i : int,val : int):
            if i == 0 :
                return 0 if (prices[0] >= val) else (val - prices[0])

            if prices[i] >= val:
                return 0 + recursion(i-1,prices[i])
            else:
                one = recursion(i-1,val)
                two = (val - prices[i]) + recursion(i-1,prices[i])
                return max(one,two)
        
        if len(prices) > 1:
            return recursion(len(prices)-1,prices[-1])
        else:
            return 0
        
    def stocks2Memoization(self, prices: List[int]) -> int:

        dp = [[-1]*(max(prices)+1) for _ in range(len(prices))]
        def recursion(i : int,val : int):
            if i == 0 :
                return 0 if (prices[0] >= val) else (val - prices[0])

            if dp[i][val] != -1:
                return dp[i][val]
            
            if prices[i] >= val:
                dp[i][val] = recursion(i-1,prices[i])
                return dp[i][val] 
            else:
                one = recursion(i-1,val)
                two = (val - prices[i]) + recursion(i-1,prices[i])
                dp[i][val] = max(one,two)
                return dp[i][val]
        
        if len(prices) > 1:
            return recursion(len(prices)-2,prices[-1])
        else:
            return 0
        
    def stocks2Tabulation(self, prices: List[int]) -> int:
        dp = [[0]*(max(prices)+1) for _ in range(len(prices))]

        for j in range(max(prices)+1):
            if prices[0] < j:
                dp[0][j] = j - prices[0]
        
        for i in range(1,len(prices)):
            for j in range(max(prices)+1):
                if prices[i] >= j:
                    dp[i][j] = dp[i-1][prices[i]]
                else:
                    one = dp[i-1][j]
                    two = (j - prices[i]) + dp[i-1][prices[i]]
                    dp[i][j] = max(one,two)

        return dp[-1][prices[len(prices)-1]]

ob = Solution()
print(ob.stocks2Recursion([7,1,5,3,6,4]))
print(ob.stocks2Recursion([1,2,3,4,5]))
print(ob.stocks2Recursion([7,6,4,3,1]))

print(ob.stocks2Memoization([7,1,5,3,6,4]))
print(ob.stocks2Memoization([1,2,3,4,5]))
print(ob.stocks2Memoization([7,6,4,3,1]))

print(ob.stocks2Tabulation([7,1,5,3,6,4]))
print(ob.stocks2Tabulation([1,2,3,4,5]))
print(ob.stocks2Tabulation([7,6,4,3,1]))