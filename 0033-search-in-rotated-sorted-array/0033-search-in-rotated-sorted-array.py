class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        #nums = array ascendin order 
        #find target in nums and return index
        # return -1 if target is not in nums 
        #runtime 0(log n)
        
        if target in nums:
            return nums.index(target)
        else:
            return -1
        
        
        

        