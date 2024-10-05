from typing import List

class Solution:
    def countSubsetsWithTargetSumSpaceOptimized(self,nums:List[int],difference :int) -> bool :
        total = sum(nums)
        target = (total - difference)
        if target % 2 == 1:
            return 0
        target = target // 2
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
                
                dummy[j] = take + not_take
            
            dp = dummy
        
        return dp[target]
    
ob = Solution()
print(ob.countSubsetsWithTargetSumSpaceOptimized([1,1,2,3],1))
print(ob.countSubsetsWithTargetSumSpaceOptimized([5,2,6,4],3))