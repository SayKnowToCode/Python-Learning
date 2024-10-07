class Solution :
    def lcsRecursion(self, s1:str , s2:str) -> int :
        def recursion(i1 : int, i2 : int) -> int:
            if i1 < 0 or i2 < 0:
                return 0
            
            if s1[i1] == s2[i2]:
                return 1 + recursion(i1 - 1, i2 -1)
            
            return max(recursion(i1 , i2-1),recursion(i1 - 1, i2))

        return recursion(len(s1)-1 , len(s2)-1)
    
    def lcsMemoization(self, s1:str , s2:str) -> int :
        dp = [[-1]*(len(s2)) for _ in range(len(s1))]

        def recursion(i1 : int, i2 : int) -> int:
            if i1 < 0 or i2 < 0:
                return 0
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            
            if s1[i1] == s2[i2]:
                return 1 + recursion(i1 - 1, i2 -1)
            
            dp[i1][i2] = max(recursion(i1 , i2-1),recursion(i1 - 1, i2))
            return dp[i1][i2]
        
        return recursion(len(s1)-1 , len(s2)-1)
    
    def lcsTabulation(self, s1:str , s2:str) -> int :
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])

        for row in dp:
            print(row)
        
        return dp[-1][-1]        
    
ob = Solution()
# print(ob.lcsRecursion("abcde","ace")) # 3
# print(ob.lcsRecursion("abc","abc")) # 3
# print(ob.lcsRecursion("abc","def")) # 0

# print(ob.lcsMemoization("abcde","ace")) # 3
# print(ob.lcsMemoization("abc","abc")) # 3
# print(ob.lcsMemoization("abc","def")) # 0

# print(ob.lcsTabulation("abcde","ace")) # 3
# print(ob.lcsTabulation("abc","abc")) # 3
# print(ob.lcsTabulation("abc","def")) # 0

print(ob.lcsTabulation("rabbbit","rabbit")) # 3
print(ob.lcsTabulation("babgbag","bag")) # 5
# print(ob.lcsTabulation("abac","cab")) # 3
# print(ob.lcsTabulation("babcbb","bb")) # 3

# print(ob.lcsTabulation("ABCBDAB","BDCAB")) # 4
# print(ob.lcsTabulation("ACBAD","CBDA")) # 4
# print(ob.lcsTabulation("AABBCFECF","ABCF")) # 4