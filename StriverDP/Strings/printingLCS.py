class Solution :
    def lcsTabulation(self, s1:str, s2:str) -> int :
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])

        return dp
    
    def printLCS(self, s1:str, s2 : str) -> int:
        
        dp = self.lcsTabulation(s1,s2)
        r = len(s1)
        c = len(s2)
        memoize = [[-1]*(c+1) for _ in range(r+1)]

        def backTrack(i : int, j : int) -> int:
            if i==0 or j==0:
                return 1
            
            if s1[i - 1] == s2[j - 1]:
                total = 0

                if memoize[i-1][j-1] != -1:
                    total += memoize[i-1][j-1]
                else:
                    total += backTrack(i-1,j-1)

                if dp[i][j] == dp[i-1][j]:
                    if memoize[i-1][j] != -1:
                        total += memoize[i-1][j]
                    else:
                        total += backTrack(i-1,j)
                if dp[i][j] == dp[i][j-1]:
                    if memoize[i][j-1] != -1:
                        total += memoize[i][j-1]
                    else:
                        total += backTrack(i,j-1)

                memoize[i][j] = total
                return total
            
            else :
                total = 0
                if dp[i][j] == dp[i-1][j]:
                    if memoize[i-1][j] != -1:
                        total += memoize[i-1][j]
                    else:
                        total += backTrack(i-1,j)
                if dp[i][j] == dp[i][j-1]:
                    if memoize[i][j-1] != -1:
                        total += memoize[i][j-1]
                    else:
                        total += backTrack(i,j-1)

                memoize[i][j] = total
                return total
        
        return backTrack(r,c)
    
ob = Solution()
print(ob.printLCS("rabbbit","rabbit")) # 3
print(ob.printLCS("babgbag","bag")) # 3