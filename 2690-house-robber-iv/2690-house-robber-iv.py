class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low,high = min(nums),max(nums)
        ans = 0
        while low<= high:
            mid=(low+high)//2
            i = 0
            c = 0
            while i < len(nums):
                if nums[i]<=mid:
                    c+=1
                    i += 1
                    
                i+=1
            if c>=k:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
                    




            