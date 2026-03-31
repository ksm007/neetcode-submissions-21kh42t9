class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        # xorr = size 
        # for i in range(size):
        #     xorr ^= i ^ nums[i]
        # return xorr
        res = size
        for i in range(size):
            res+= i - nums[i]
        
        return res