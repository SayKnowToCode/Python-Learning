from typing import List

class Solution:
    def rodCuttingRecursion(self,n : int,values:List[int])->int:
        
        def recursion(n :int) -> int:
            if n == 0:
                return 0
            
            if n < 0:
                return -1

            one = recursion(n - values[0])
            two = recursion(n - values[1])
            three = recursion(n - values[2])

            if one == -1 and two == -1 and three == -1:
                return -1
            return 1 + max(one,two,three)

        ans = recursion(n)
        if ans == -1:
            return 0
        else:
            return ans
        
    def rodCuttingMemoization(self,n : int,values:List[int])->int:
        
        dp = dict()
        def recursion(n :int) -> int:
            if n == 0:
                return 0
            
            if n < 0:
                return -1

            if n-values[0] in dp:
                one = dp[n-values[0]]
            else:
                one = recursion(n - values[0])

            if n-values[1] in dp:
                two = dp[n-values[1]]
            else:
                two = recursion(n - values[1])

            if n-values[2] in dp:
                three = dp[n-values[2]]
            else:
                three = recursion(n - values[2])

            if one == -1 and two == -1 and three == -1:
                return -1
            dp[n] = 1 + max(one,two,three)
            return 1 + max(one,two,three)

        ans = recursion(n)
        if ans == -1:
            return 0
        else:
            return ans
        
    def rodCuttingTabulation(self,n : int,values:List[int])->int:
        dp = [-1] * (n+1)
        dp[0] = 0
        
        for i in range(1,n+1):

            one = two = three = -1
            if i - values[0] >= 0:
                one = dp[i-values[0]]
            if i - values[1] >= 0:
                two = dp[i-values[1]]
            if i - values[2] >= 0:
                three = dp[i-values[2]]
            
            ans = max(one,two,three)
            print(ans)
            if ans == -1:
                continue
            else:
                dp[i] = 1 + ans
        
        return dp[n]

ob = Solution()
print(ob.rodCuttingRecursion(7,[5,2,1]))
print(ob.rodCuttingMemoization(200,[25,50,100]))
print(ob.rodCuttingTabulation(7,[5,2,2]))