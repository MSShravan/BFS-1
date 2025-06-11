# Time Complexity : O(V + E) where V is the number of courses and E is the number of prerequisites
# Space Complexity : O(V + E)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and in-degree array
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
        
        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return taken == numCourses
        