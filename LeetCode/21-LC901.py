"""
class StockSpanner:
    def __init__(self):
        self.stx=[]
                
    def next(self, price: int) -> int:
        span=1
        while self.stx and self.stx[-1][0]<=price:
            span+=self.stx.pop()[1]
        self.stx.append([price,span])
        return span            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
"""