class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices.copy()

            for s, d, cst in flights:
                if prices[s] == INF:
                    continue
                if prices[s] + cst < temp_prices[d]:
                    temp_prices[d] = prices[s] + cst
            prices = temp_prices
        
        return prices[dst] if prices[dst] != INF else -1