class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        ans = []
        for i in range (0,len(candies)):
            temp = candies[i]
            candies[i]=candies[i]+extraCandies
            if max(candies)== candies[i]:
                ans.append(True)
            else:
                ans.append(False)
            candies[i]=temp
        return ans