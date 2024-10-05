from typing import List

class Solution:
    def targetSumRecursion(self, nums: List[int], target: int) -> int:

        def recursion(index : int, target : int) -> int:
            if index == 0:
                if nums[0] == 0:
                    return 2
                
                if abs(nums[0]) == target:
                    return 1
                else:
                    return 0
                
            pos = recursion(index-1,target - nums[index])
            neg = recursion(index-1,target + nums[index])

            return pos + neg

        return recursion(len(nums)-1,target)
    
    def targetSumTabulation(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total :
            return 0
        
        dp = [[0]*(total + 1) for _ in range (len(nums))]

        for j in range(total+1):
            if nums[0] == 0:
                dp[0][0] = 2
                break

            if j == abs(nums[0]) :
                dp[0][j] = 1
        
        for i in range(1,len(nums)):
            for j in range(total+1):
                
                neg = dp[i-1][abs(j - nums[i])]
                pos = 0
                if j + nums[i] < total + 1:
                    pos = dp[i-1][j + nums[i]]

                dp[i][j] = pos + neg

        return dp[-1][abs(target)]


ob = Solution()
print(ob.targetSumRecursion([1,1,1,1,1],3))
print(ob.targetSumRecursion([3,7,1,6,5],20))

# For tabulation, the target will be till the sum of all elements in the array
print(ob.targetSumTabulation([1,1,1,1,1],3))
print(ob.targetSumTabulation([3,7,1,6,5],20))
print(ob.targetSumTabulation([3,0,7,1,0,6,0,5],20))
print(ob.targetSumTabulation([0,0,0,0,0,0,0,0,1],1))