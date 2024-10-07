class Solution :
    def lcsRecursion(self, s1:str , s2:str) -> int :
        def recursion(i1 : int, i2 : int) -> int:
            if i1 < 0 or i2 < 0:
                return 0
            
            if s1[i1] == s2[i2]:
                return 1 + recursion(i1 - 1, i2 -1)
            
            return recursion(i1 - 1, i2 -1)

        maximum = 0
        if len(s1) >= len(s2):
            n = len(s1)
            while n >= len(s2):
                maximum = max(maximum,recursion(n-1,len(s2)-1))
                n -= 1
        else:
            m = len(s2)
            while m >= len(s1):
                maximum = max(maximum,recursion(len(s1)-1,m-1))
                m -= 1

        return maximum
    
    def lcsTabulation(self, s1:str , s2:str) -> int :
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
        
        maximum = 0
        for i in range(len(s1)+1): 
            for j in range(len(s2)+1):
                maximum = max(maximum,dp[i][j])
        
        return maximum
    
ob = Solution()
print(ob.lcsRecursion("abcde","ace")) # 1
print(ob.lcsRecursion("abcjklp","acjkp")) # 3
print(ob.lcsRecursion("abc","def")) # 0

# print(ob.lcsTabulation("abcde","ace")) # 3
# print(ob.lcsTabulation("abcjklp","acjkp")) # 3
# print(ob.lcsTabulation("abc","def")) # 3
print(ob.lcsTabulation("babad","dabab")) # 3
print(ob.lcsTabulation("cbbd","dbbc")) # 3
print(ob.lcsTabulation("aacabdkacaa","aacakdbacaa")) # 0