class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while(start != 0 or goal != 0):
            d1 = start & 1
            d2 = goal & 1
            if d1 != d2:
                count += 1
            start = start >> 1
            goal = goal >> 1
        return count
    

start = 3
goal = 4

print(Solution().minBitFlips(start,goal))