class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a hashmap where it'll be each course and a list of it's pre-reqs
        # then, iterate through prerequisites to append prereqs to the hashmap.
        # we will also have a set which indicates courses we are already visiting; 
        # after visiting a courses pre-req, if we notice that the pre-req is already in the set, then we return False (loop detected)

        courses = {} # course: [prereq1, prereq2]
        for course in range(numCourses):
            courses[course] = []

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        visited = set()

        def dfs(course):
            # cycle detected
            if course in visited:
                return False
            elif not courses[course]:
                return True
            
            visited.add(course)

            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            courses[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True





