from typing import List

class Solution:
    def powerSet(self,nums : List) -> List[List[int]]:
        n = 1 << len(nums)
        res = []
        for i in range(n):
            subset = []
            for j in range(len(nums)):
                if(i & (1<<j)):
                    subset.append(nums[j])
            res.append(subset)
        return res

print(Solution().powerSet([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]