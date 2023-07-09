class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        res = 0

        while right > left:
            a = (right-left)*min(height[right],height[left])
            res = a if a > res else res

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res

