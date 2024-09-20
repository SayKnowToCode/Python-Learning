from typing import List

class Solution:
    def permutations(self,s:str) -> List[str]:
        result = []

        def backTrack(index : int):

            if index == len(s)-1:
                result.append("".join(s))
                return
            
            for i in range(index,len(s)):
                s[index],s[i] = s[i],s[index]
                backTrack(index+1)
                s[index],s[i] = s[i],s[index]

        backTrack(0)
        return result
            
s = "abcef"
res = Solution().permutations(list(s))
print(res)
print(len(res))