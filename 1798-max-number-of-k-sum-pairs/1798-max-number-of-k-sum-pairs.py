class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        first = 0
        second = len(nums)-1
        count = 0
        nums.sort()
        while (first < second):
            if nums[first]+ nums[second]>k:
                second-=1
            elif nums[first]+nums[second]<k:
                first+=1
            elif nums[first]+nums[second]==k:
                count +=1
                first +=1
                second -=1

        return count

            
            






        


