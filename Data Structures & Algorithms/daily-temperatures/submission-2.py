class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    final.append(count)
                    break
                count += 1
                
                   
                if j == len(temperatures) - 1:
                    final.append(0)
        
        return final
