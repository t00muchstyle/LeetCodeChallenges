class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1 
        high = max(piles)

        while low < high:
            mid = (low+high)//2
            totalH = sum(math.ceil(pile/mid)for pile in piles)
            #print(totalH)
            if totalH > h :
                low = mid + 1
            else:
                high = mid
        return low 
        


