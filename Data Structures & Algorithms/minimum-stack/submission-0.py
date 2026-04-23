class MinStack:

    def __init__(self):
        self.myList = []
        self.myMin = []
    def push(self, val: int) -> None:
        if len(self.myMin) == 0:
            self.myMin.append(val)
            self.myList.append(val)
        else: 
            self.myMin.append(min(val, self.myMin[-1]))
            self.myList.append(val)
         

    def pop(self) -> None:
        
        self.myMin.pop()
        self.myList.pop()
    def top(self) -> int:
        return self.myList[-1]

    def getMin(self) -> int:
        return self.myMin[-1]

        
