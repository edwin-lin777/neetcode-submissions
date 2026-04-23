class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            count = Counter(tasks)
            heap = [ -c for c in count.values()]

            heapq.heapify(heap)
            time = 0
            q = collections.deque()

            while heap or q:
                time += 1
                if heap:
                    c = heapq.heappop(heap) + 1
                    if c:
                        q.append([c, time + n])
                
                if q and q[0][1] == time:
                    temp = q.popleft()
                    heapq.heappush(heap, temp[0])
            return time

                





