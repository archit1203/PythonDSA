"""
class StockSpanner:
    def __init__(self):
        self.stx=[]
                
    def next(self, price: int) -> int:
        self.stx.append(price)
        
        if len(self.stx)==1:
            return 1
        i=len(self.stx)-1

        span=1
        if self.stx[i]<self.stx[i-1]:
            return 1
        else:
            for j in range(i-1,-1,-1):
                if self.stx[i]>=self.stx[j]:
                    span+=1
                else:
                    return span
        
        return span
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""