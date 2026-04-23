class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        myDict = defaultdict(list)
        final = []
        tickets.sort()
        for original, target in tickets:
            myDict[original].append(target)

        def dfs(airport):
            while myDict[airport]:
                next_dest = myDict[airport].pop(0)
                dfs(next_dest)
            final.append(airport)
        dfs("JFK")
        return final[::-1]




