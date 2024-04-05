class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # consider capital letters, spaces and punc
        
        checkPal= ""
        
        s = s.lower()
        
        for i in s:
            if i.isalnum(): #checks if alphanumeric
                checkPal += i
        return checkPal == checkPal[::-1]
                
      