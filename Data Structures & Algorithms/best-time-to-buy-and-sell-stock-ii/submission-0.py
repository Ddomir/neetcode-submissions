class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = buyDay = 0
        have = False


        for day, price in enumerate(prices):
            if have == False and day + 1 < len(prices) and prices[day + 1] > prices[day]:
                buyDay = day
                have = True
            
            if have == True and day + 1 < len(prices) and prices[day + 1] < prices[day]:
                profit += prices[day] - prices[buyDay]
                have = False
            
            if day + 1 == len(prices) and have == True:
                profit += prices[day] - prices[buyDay]
                break
        
        return profit

    # Buy when next day higher
    # Sell when next day lower, update profit
        