from typing import List

class Solution:
    def houseRobber(self,nums:List[int]) -> int:

        dp = [-1] * len(nums)
        def recursion(index : int) -> int:
            if index == 0:
                return nums[0]
            
            pick = nums[index]

            if index > 1 :
                if dp[index-2] != -1:
                    pick += dp[index-2]
                else:
                    pick += recursion(index - 2)

            non_pick = 0
            if(dp[index-1] != -1):
                non_pick = dp[index-1]
            else:
                non_pick = recursion(index-1)

            dp[index] = max(pick,non_pick) 
            return max(pick,non_pick)

        return recursion(len(nums)-1)

    def Tabulation(self,nums:List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1,n):
            pick = nums[i]
            if i > 1:
                pick += dp[i-2]
            non_pick = dp[i-1]
            dp[i] = max(pick,non_pick)

        return dp[n-1]

    def SpaceOptimize(self,nums:List[int]) -> int:
        n = len(nums)
        curr = 0
        prev = nums[0]
        prev2 = 0

        for i in range(1,n):
            pick = nums[i]
            if i > 1:
                pick += prev2
            non_pick = prev
            curr = max(pick,non_pick)
            
            prev2 = prev
            prev = curr

        print(prev2,prev,curr)
        return prev


array = [5]
ob = Solution()
print(ob.houseRobber(array))
print(ob.Tabulation(array))
print(ob.SpaceOptimize(array))
print(array)