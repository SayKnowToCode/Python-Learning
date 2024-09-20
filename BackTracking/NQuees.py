from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        output = []
        for i in range(n):
            output.append(['.'] * n)

        col = set()

        def isSafe(row : int, column : int) -> bool:
            if row -1 < 0:
                return True
            if column in col:
                return False
            
            check1 = True
            check2 = True

            i = row
            j = column

            while i >= 0 and j >= 0:
                if output[i][j] == 'Q':
                    check1 = False
                    break
                i -= 1
                j -= 1

            i = row
            j = column

            while i >= 0 and j < n:
                if output[i][j] == 'Q':
                    check2 = False
                    break
                i -= 1
                j += 1
            
            return check1 and check2

        def outputToString():
            ans = []
            for i in range(n):
                ans.append(''.join(output[i]))
            return ans

        def backTrack(row:int) -> None:
            
            if row == n:
                result.append(outputToString())
                return
            
            for i in range(n):
                if isSafe(row,i):
                    output[row][i] = 'Q'
                    col.add(i)
                    backTrack(row + 1)
                    output[row][i] = '.'
                    col.remove(i)           

        backTrack(0)
        return result

n = 5
print(Solution().solveNQueens(n))