class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP=0
        
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxP=0
#         minBuy=prices[0]

#         for price in prices:
#             maxP=max(maxP,price-minBuy)
#             minBuy=min(minBuy,price)
#         return maxP