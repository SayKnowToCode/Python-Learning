class Solution:

    def subsequences(self, s:str) -> None:
        ans = []
        
        def backTrack(index, subseq) -> None:
            if subseq:
                ans.append(subseq)

            for i in range(index,len(s)):
                subseq += s[i]
                backTrack(i+1,subseq)
                subseq = subseq[0:len(subseq)-1]

        backTrack(0, "")
        return ans
    
string = "abc"
print(Solution().subsequences(string))
