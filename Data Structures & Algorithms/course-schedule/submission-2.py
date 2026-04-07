class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a hashmap where it'll be each course and a list of it's pre-reqs
        # then, iterate through prerequisites to append prereqs to the hashmap.
        # we will also have a set which indicates courses we are already visiting; 
        # after visiting a courses pre-req, if we notice that the pre-req is already in the set, then we return False (loop detected)

        adjList = [] 
        for _ in range(numCourses):
            adjList.append([])

        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visited = set()

        def dfs(course):
            # cycle detected
            if course in visited:
                return False
            elif not adjList[course]: # if it has no prereqs then you can take that course
                return True
            
            visited.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adjList[course] = [] # this is optional, but better to have to prevent recomputing the same course over and over again
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
                