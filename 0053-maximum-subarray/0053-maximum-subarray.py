class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #initilize max subarray
        #constanly computing the current Sum

        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0 #reset back to zero if cur sum is negative
            cur_sum += n 
            max_sub = max(max_sub, cur_sum)

        return max_sub
