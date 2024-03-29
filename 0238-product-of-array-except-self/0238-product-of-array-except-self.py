from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize left and right product variables
        left_mult = 1
        right_mult = 1
        
        # Initialize left and right arrays to store prefix and suffix products
        left_arr = [1] * n
        right_arr = [1] * n
        
        # Calculate prefix products (left_arr)
        for i in range(n):
            left_arr[i] = left_mult
            left_mult *= nums[i]
        
        # Calculate suffix products (right_arr)
        for j in range(n - 1, -1, -1):
            right_arr[j] = right_mult
            right_mult *= nums[j]
        
        # Multiply corresponding elements of left and right arrays to get the final result
        result = [left_arr[i] * right_arr[i] for i in range(n)]
        
        return result
