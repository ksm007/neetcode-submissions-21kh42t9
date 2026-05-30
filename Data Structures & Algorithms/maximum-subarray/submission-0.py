class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')
        s = 0
        for n in nums:
            s = s+n
            res = max(res, s)
            if s < 0:
                s = 0
        
        return res