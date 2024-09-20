from typing import List

class Solution :

    def subsets(self, nums : List[int]) -> None:
        ans = []
        output = []
        index = 0

        def backtrack(index, output):
            if(index == len(nums)):
                ans.append(output)
                return
            
            # We have to do list(output) because output is a reference to the same list
            # So if we modify output, we will modify the output of the previous recursive call
            # So we have to make a copy of the output list to avoid this problem

            # exclude the current element
            backtrack(index + 1, list(output))

            # include the current element
            output.append(nums[index])
            backtrack(index + 1, list(output))


        backtrack(index, output)
        return ans  
    
    def subsets_betterApproach(self, nums):
        result = []
        
        def backtrack(nums, subset, result, start):
            result.append(list(subset))
            # We have to do subset[:] because subset is a reference to the same list
            # So if we modify subset, we will modify the output of the previous recursive call
            # So we have to make a copy of the subset list to avoid this problem

            # What does [:] do?
            # It creates a shallow copy of the list. This means that it creates a new list and copies the elements of the original list into the new list.
            # This is different from the assignment operator (=) which creates a reference to the original list.
            # This means that if you modify the new list, the original list will not be modified.
            # This is useful when you want to modify the list without changing the original list.
            # I can also use list(subset) to create a shallow copy of the list.

            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(nums, subset, result, i + 1)
                subset.pop()
        
        backtrack(nums, [], result, 0)
        return result

nums = [1, 2, 3]
print(Solution().subsets(nums))
print(Solution().subsets_betterApproach(nums))