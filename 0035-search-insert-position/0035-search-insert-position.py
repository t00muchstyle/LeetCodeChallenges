class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = False
        low = 0 
        high = len(nums)-1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if target == nums[mid]:

                return mid 
            elif target > nums[mid]: 
                high = mid-1 
                
            elif target< nums[mid]:
                low = mid + 1
        if found == False:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)
        else:
            return mid


        
            
        