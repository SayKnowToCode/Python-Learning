from typing import List

class Solution :

    def Tabulation(self, days:List[List[int]]) -> int:
        n = len(days)
        dp = []
        for i in range(n):
            dp.append([-1]*4)
        
        for i in range(3):
            maxi = 0
            for j in range(3):
                if i != j:
                    maxi = max(maxi,days[0][j])
            dp[0][i] = maxi
        
        print(dp)
        
        for i in range(1,n):
            for j in range(4):
                for k in range(3):
                    if j != k:
                        dp[i][j] = max(dp[i][j],days[i][k] + dp[i-1][k])
        
        print(dp)
        return max(dp[n-1])


    def NinjaTraining(self, days:List[List[int]]) -> int:

        n = len(days)
        dp = []

        for i in range(n):
            dp.append([-1]*4)

        def recursion(index,last):

            print(dp)
            if dp[index][last] != -1:
                print("Here")
                return dp[index][last]
            
            if index == 0 :
                maximum = 0
                for i in range(3):                   
                    if i != last:
                        maximum = max(maximum,days[index][i])
                dp[index][last] = maximum
                return maximum
            
            maximum = 0
            for i in range(3):
                if i != last:
                    maximum = max(maximum,days[index][i]+recursion(index-1,i))
            dp[index][last] = maximum
            return maximum


        return recursion(n-1,3)
    

days = [[2,1,3], [3,4,6], [10,1,6], [8,3,7]]
# days = [[10,50,1], [7,100,11]]
ob = Solution()
# print(ob.NinjaTraining(days)) # 19
print(ob.Tabulation(days)) # 19