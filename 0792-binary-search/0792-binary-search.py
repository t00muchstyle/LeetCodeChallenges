class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)
        mid = (low+high)//2

        found = False 
        while low <high:
            node = nums[mid]
            if node == target:
                found = True
                return mid 
                 
            elif node < target:
                low = mid
                mid = (low+high)//2
                if low == mid:
                    low+=1
            else:
                high = mid 
                mid = (low+high)//2
                if high == mid:
                    high-=1

        return -1

                
                
                
                