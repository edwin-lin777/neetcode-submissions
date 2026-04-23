class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stack = {}
        for x in nums:
            stack[x] = stack.get(x, 0) + 1;

        final =[]
        for x in range(k):
            temp = - 10000000000000;
            push = 0;
            for x in stack:
                if stack[x] > temp:
                    temp = stack[x];
            for x in stack:
                if stack[x] == temp:
                    push = x
            final.append(push)
            stack.pop(push)

             
        return final;
