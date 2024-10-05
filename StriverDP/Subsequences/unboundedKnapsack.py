from typing import List

class Solution:
    def unboundedKnapsackRecursion(self,weights : List[int], values : List[int], W : int) -> int :
        n = len(weights)

        def recursion(index:int, weight : int) -> int :

            if index == 0:
                return 0 if weight < weights[0] else values[0]
            
            not_take = recursion(index - 1, weight)
            take = 0
            if weights[index] <= weight :
                take = values[index] + recursion(index, weight - weights[index])
            
            return max(not_take, take)

        return recursion(n-1,W)

    def unboundedKnapsackTabulation(self,weights : List[int], values : List[int], W : int) -> int :
        n = len(weights)
        dp = [[0]*(W+1) for _ in range(n)]

        for j in range(W+1):
            if j >= weights[0]:
                dp[0][j] = values[0]
        
        for i in range(1,n):
            for j in range(W+1):
                non_take = dp[i-1][j]
                take = 0
                if weights[i] <= j:
                    take = values[i] + dp[i][j-weights[i]]
                
                dp[i][j] = max(non_take, take)
        
        return dp[-1][-1]

ob = Solution()
print(ob.unboundedKnapsackRecursion([3,2,5],[30,40,60],6)) 
print(ob.unboundedKnapsackRecursion([1,3,4,5],[1,4,5,7],7)) # 9

print(ob.unboundedKnapsackTabulation([3,2,5],[30,40,60],6))
print(ob.unboundedKnapsackTabulation([3,2,5],[30,40,60],1))
print(ob.unboundedKnapsackTabulation([1,3,4,5],[1,4,5,7],7)) # 9