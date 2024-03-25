class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        compare = set()
        
        for i in nums: 
            if i in compare:
                return True
            compare.add(i)
        return False
