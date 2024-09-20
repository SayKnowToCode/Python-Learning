from typing import List

class Solution:
    def ratMaze(self,grid : List[List[int]]) -> List[str]:
        result = []
        r = len(grid)
        c = len(grid[0])
        visited = set()
        output = ''

        def backTrack(i:int,j:int,output:str) -> None:
            if i==r or j==c or i<0 or j<0 or grid[i][j] == 0 or (i,j) in visited:
                return
            
            if i == r-1 and j == c-1:
                result.append(output)
                return
            
            visited.add((i,j))

            backTrack(i-1,j,output+'U')
            backTrack(i+1,j,output+'D')
            backTrack(i,j-1,output+'L')
            backTrack(i,j+1,output+'R')

            visited.remove((i,j))
    
        backTrack(0,0,output)
        return result
    
grid = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

print(Solution().ratMaze(grid))
