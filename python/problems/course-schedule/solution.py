#!/usr/bin/python

class Solution(object):
    adjacency = {}
    cached = {}
    def has_cycle(self, course, prereq):
        if course in Solution.cached:
            return Solution.cached[course]
        
        visited = []
        to_visit = [course]
        
        while to_visit:
            current = to_visit[0]
            del to_visit[0]
            
            if current in Solution.cached:
                return Solution.cached[current]
            
            if current not in Solution.adjacency:
                Solution.adjacency[current] = [(s, e) for (s, e) in prereq if s==current]
            
            for (start, end) in Solution.adjacency[current]:
                if start in Solution.cached and Solution.cached[start] == True:
                    return True
                    
                if start in visited:
                    Solution.cached[course] = True
                    return True
                        
                to_visit.append(end)
            visited.append(current)
        
        Solution.cached[course] = False
        return False
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        Solution.adjacency = {}
        Solution.cached = {}

        for course in xrange(numCourses):
            if self.has_cycle(course, prerequisites):
                print Solution.cached
                return False

                
        return True

s = Solution()
print s.canFinish(3, [[0, 1], [0,2], [1,2]]) 
