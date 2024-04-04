class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # letter in s == letter in t 

        if Counter(s) == Counter(t):
            return True