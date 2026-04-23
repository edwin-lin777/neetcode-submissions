class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()

        def helper(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
        
            visited.add(course)
            for pre in preMap[course]:
                if not helper(pre):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        for i in range(numCourses):
            if not helper(i):
                return False
        return True
        
                    