class MinStack:

    def __init__(self):
        self.arr=[]
        self.mini=float("inf")

    def push(self, val: int) -> None:
        self.arr.append(val)

        

    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        mini=float("inf")
        for i in self.arr:
            if mini!=min(mini,i):
                mini=i
        return mini
        
        
