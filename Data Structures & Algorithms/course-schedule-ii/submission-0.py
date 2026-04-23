class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {}
        for i in range(numCourses):
            courseMap[i] = []

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        
        visited = set()


        final =[]
        done = set()
        def helper(course):
            if course in visited:
                return False
            if course in done:
                return True

            visited.add(course)
            for temp in courseMap[course]:
                if not helper(temp):
                    return False
            visited.remove(course)
            done.add(course)
            final.append(course)
    
            return True

        for i in range(numCourses):
            if not helper(i):
                return []

        return final
            