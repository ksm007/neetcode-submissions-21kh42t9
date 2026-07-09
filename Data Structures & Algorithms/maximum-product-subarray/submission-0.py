class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1,1

        for num in nums:
            tmp = num * curMax
            curMax = max(curMax * num, curMin* num, num )
            curMin = min(tmp, curMin * num, num)
            res = max(res, curMax)
        
        return res
