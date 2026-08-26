class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]

        rich = 0

        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                profit = sell - buy
                rich = max(profit, rich)
        return rich


        
        
        """left = 0
        right = len(prices) - 1
        summ = 0

        while prices[left] > prices[right]:
            left += 1
            right -= 1
            

        if right > left:
            summ = prices[right] - prices[left]
            return summ
        
        return 0    """

