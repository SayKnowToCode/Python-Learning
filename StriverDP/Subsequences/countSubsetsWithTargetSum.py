from typing import List

class Solution:
    def countSubsetsWithTargetSumRecursion(self,nums:List[int],target :int) -> int :
        def recursion(index:int,target:int) -> int:
            if target == 0 :
                return 1
            
            if index == 0 :
                return 1 if nums[index] == target else 0
            
            notTake = recursion(index-1,target)
            take = 0
            if target >= nums[index]:
                take = recursion(index-1,target-nums[index])

            return take + notTake 

        return recursion(len(nums)-1,target)
    
    def countSubsetsWithTargetSumMemoization(self,nums:List[int],target :int) -> int :
        dp = [[-1]*(target+1) for _ in range(len(nums))]
        def recursion(index:int,target:int) -> int:
            if target == 0 :
                dp[index][target] = 1
                return 1
            
            if index == 0 :
                dp[index][target] = 1 if nums[index] == target else 0
                return 1 if nums[index] == target else 0
            
            if dp[index][target] != -1:
                return dp[index][target]
            
            notTake = recursion(index-1,target)
            take = 0
            if target >= nums[index]:
                take = recursion(index-1,target-nums[index])

            dp[index][target] = take + notTake
            return take + notTake 

        return recursion(len(nums)-1,target)
    
    def countSubsetsWithTargetSumTabulation(self,nums:List[int],target :int) -> int :
        dp = [[0]*(target+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = 1
        
        if nums[0] <= target:
            dp[0][nums[0]] = 1
        
        for i in range(1,len(nums)):
            for j in range(1,target+1):
                notTake = dp[i-1][j]
                take = 0
                if nums[i] <= j:
                    take = dp[i-1][j-nums[i]]
                dp[i][j] = take + notTake
        
        return dp[-1][-1]
    
    def countSubsetsWithTargetSumSpaceOptimized(self,nums:List[int],target :int) -> bool :
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
print(ob.countSubsetsWithTargetSumRecursion([1,1,2,3],4))
print(ob.countSubsetsWithTargetSumRecursion([1,2,2,3],3))

print(ob.countSubsetsWithTargetSumMemoization([1,1,2,3],4))
print(ob.countSubsetsWithTargetSumMemoization([1,2,2,3],3))

print(ob.countSubsetsWithTargetSumTabulation([1,1,2,3],4))
print(ob.countSubsetsWithTargetSumTabulation([1,2,2,3],3))

print(ob.countSubsetsWithTargetSumSpaceOptimized([1,1,2,3],4))
print(ob.countSubsetsWithTargetSumSpaceOptimized([1,2,2,3],3))