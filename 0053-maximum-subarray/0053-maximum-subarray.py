class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end = 0     
        s = 0       # sum
        Max = -2147483648
        length = len(nums)
        for end in range(length) :
            s += nums[end]
            if s > Max:
                Max = s
            if s < 0:
                s = 0
            elif nums[end] > s:
                s = nums[end]
        return Max