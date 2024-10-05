from typing import List

class Solution:

    def subsetSumRecursion(self,nums:List[int],target :int) -> bool :

        def recursion(index:int,target:int) -> bool:
            if target == 0 :
                return True
            
            if index == 0 :
                return nums[index] == target
            
            notTake = recursion(index-1,target)
            take = False
            if target >= nums[index]:
                take = recursion(index-1,target-nums[index])

            return take or notTake 

        return recursion(len(nums)-1,target)
    
    
    def subsetSumMemoization(self,nums:List[int],target :int) -> bool :

        dp = [[-1]*(target+1) for _ in range(len(nums))]
        def recursion(index:int,target:int) -> bool:
           
            if target == 0 :
                dp[index][target] = True
                return True
            
            if index == 0 :
                if nums[index] == target:
                    dp[index][target] = True
                    return True
                else:
                    dp[index][target] = False
                    return False
            
            if dp[index][target] != -1:
                return dp[index][target]
                                 
            notTake = recursion(index-1,target)
            take = False
            if target >= nums[index]:
                take = recursion(index-1,target-nums[index])

            dp[index][target] = take or notTake
            # print(dp)
            return take or notTake 

        return recursion(len(nums)-1,target)

    
    def subsetSumTabulation(self,nums:List[int],target :int) -> bool :
        dp =[[False]*(target+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1,len(nums)):
            for j in range(1,target+1):
                not_take = dp[i-1][j]
                take = False
                if j >= nums[i]:
                    take = dp[i-1][j-nums[i]]
                
                dp[i][j] = take or not_take
            # print(dp)

        return dp[len(nums)-1][target]

    def subsetSumTabulationOptimized(self,nums:List[int],target :int) -> bool :
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
    
    def subsetSumTabulationSuperOptimized(self,nums:List[int],target :int) -> bool :
        dp = [False]*(target+1)
        dp[0] = True

        if nums[0] <= target:
            dp[nums[0]] = True

        for i in range(1,len(nums)):
            j = target
            while(j >= 1):
                not_take = dp[j]
                take = False
                if j >= nums[i]:
                    take = dp[j-nums[i]]
                
                dp[j] = take or not_take
                j -= 1
        
        return dp[target]
               
    

ob = Solution()
print(ob.subsetSumRecursion([2,3,1,1],4)) # True
print(ob.subsetSumMemoization([2,3,1,1],4)) # True
print(ob.subsetSumTabulation([2,3,1,1],4)) # True
print(ob.subsetSumTabulation([76,8,45,20,74,84,28,1],168))
print(ob.subsetSumTabulationOptimized([2,3,1,1],4)) # True
print(ob.subsetSumTabulationOptimized([76,8,45,20,74,84,28,1],168))
print(ob.subsetSumTabulationOptimized([2,5,1,6,7],4))

print(ob.subsetSumTabulationSuperOptimized([76,8,45,20,74,84,28,1],168))
print(ob.subsetSumTabulationSuperOptimized([2,5,1,6,7],4))