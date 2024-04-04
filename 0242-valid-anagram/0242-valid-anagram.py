class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # letter in s == letter in t 

        s = sorted(list(s)) 
        t = sorted(list(t)) 
        if s == t:
            return True