from typing import List

class Solution:
    def subsetSumRecursion(self,nums:List[int]) -> int:
        N = sum(nums)
        
        def recursion(index :int, total:int)->int:
            if index == 0:
                s1 = total
                s2 = total + nums[0]
                
                d1 = abs(s1 - (N-s1))
                d2 = abs(s2 - (N-s2))

                return min(d1,d2)

            not_take = recursion(index-1,total)
            take = recursion(index-1,total+nums[index])
            
            return min(not_take,take)
        
        return recursion(len(nums)-1,0)
    
    def subsetSumRecursionWithEqualPartitions(self,nums:List[int]) -> int:
        N = sum(nums)
        equal = len(nums) // 2

        def recursion(index :int, total:int,n : int)->int:
            if n == equal:
                s1 = total
                s2 = N-total

                return abs(s1 - s2)
            
            if index == 0:
                total += nums[0]
                n += 1

                if n == equal:
                    s1 = total
                    s2 = N-total

                    return abs(s1 - s2)

                return float('inf')

            not_take = recursion(index-1,total,n)
            take = recursion(index-1,total+nums[index],n+1)
            
            return min(not_take,take)
        
        return recursion(len(nums)-1,0,0)


ob = Solution()
print(ob.subsetSumRecursion([3,9,7,3])) 
print(ob.subsetSumRecursion([2,-1,0,4,-2,-9])) 
print(ob.subsetSumRecursion([2,-1]))
print(ob.subsetSumRecursion([3,3,3,4,5])) 
print(ob.subsetSumRecursion([76,8,45,20,74,84,28,1])) 
print(ob.subsetSumRecursion([-36,36]))


# print(ob.subsetSumRecursionWithEqualPartitions([76,8,45,20,74,84,28,1])) 
# print(ob.subsetSumRecursionWithEqualPartitions([-36,36])) 
# print(ob.subsetSumRecursionWithEqualPartitions([7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694])) 