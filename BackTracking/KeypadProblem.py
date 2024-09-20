class Solution :
        
    def letterCombinations(self,digits : str) -> None:
        ans = []
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backTrack(index,string) -> None:
            if index == len(digits):
                ans.append(string)
                return
            
            newStr = phone[digits[index]]
            for j in range(len(newStr)):
                backTrack(index+1,string+newStr[j])
    
        backTrack(0,"")
        return ans
        
s = "47"
print(Solution().letterCombinations(s))
            
           