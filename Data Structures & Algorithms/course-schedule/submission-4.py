class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i:[] for i in range(numCourses)}
        for crs,prereq in prerequisites:
            prereqMap[crs].append(prereq)
        # initialize an empty visited set
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereqMap[course] == []:
                return True
            visited.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq): return False
            
            visited.remove(course)
            prereqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True
