class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        attempt before conceptual 
        current = 0 
        next = 1
        max_profit = 0 
        while next < len(prices): 
            if prices[next] > prices[current]
        """
        l = 0 
        r = 1
        max_profit = 0 
        while (r < len(prices)): 
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r  
                
             
            r += 1 
        return max_profit 



