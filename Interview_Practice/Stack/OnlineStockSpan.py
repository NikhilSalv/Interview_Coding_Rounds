class StockSpanner:

    def __init__(self):
        self.stack = []  # each element: (price, span)

    def next(self, price: int) -> int:
        span = 1

        # collapse all previous smaller or equal prices
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # push current price with its total span
        self.stack.append((price, span))

        return span

if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]
    stockSpanner = StockSpanner()
    for price in prices:
        print(stockSpanner.next(price))