class PrefixTree:

    def __init__(self):
        self.myDict = {}
        self.end = False
    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.myDict:
                curr.myDict[c] = PrefixTree()
            curr = curr.myDict[c]
        curr.end = True



    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.myDict:
                return False
            curr = curr.myDict[c]
        if curr.end == True:
            return True
        else:
            return False
    
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.myDict:
                return False
            curr = curr.myDict[c]
        return True
        
        