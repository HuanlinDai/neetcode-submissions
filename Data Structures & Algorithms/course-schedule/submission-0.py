class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for course, prereq in prerequisites:
            prereqs[course] = prereqs.get(course,[]) + [prereq]

        visited = set({})
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for prereq in prereqs.get(course,[]):
                if not dfs(prereq):
                    return False
            visited.remove(course)
            return True

        for course in prereqs:
            if not dfs(course):
                return False
        return True