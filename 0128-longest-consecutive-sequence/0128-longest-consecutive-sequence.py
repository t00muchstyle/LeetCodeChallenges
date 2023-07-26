class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        maxL,curM = 1,1
        nums = list(set(nums))
        nums.sort()
        while i < len(nums)-1:
            if nums[i+1] -1 == nums[i]:
                curM += 1
            else:
                curM = 1
            i += 1
            if curM > maxL:
                maxL=curM
        return maxL if nums != [] else 0 
