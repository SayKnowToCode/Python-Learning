from typing import List

class Solution:
    def subsetSumTabulationOptimized(self,nums:List[int]) -> bool :
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [False]*(target+1)

        dp[0] = True

        if nums[0] <= target:
            dp[nums[0]] = True

        for i in range(1,len(nums)):
            dummy = [False]*(target+1)
            dummy[0] = True

            for j in range(1,target+1):
                not_take = dp[j]
                take = False
                if j >= nums[i]:
                    take = dp[j-nums[i]]
                
                dummy[j] = take or not_take
            
            dp = dummy
        
        return dp[target]
    
ob = Solution()
print(ob.subsetSumTabulationOptimized([1,1,2,3]))