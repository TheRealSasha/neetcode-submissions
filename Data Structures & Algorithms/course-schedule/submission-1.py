class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct the graph
        # for each node, store the in-degree
        # if a node has an in-degree of zero, then it is reachable
        
        # process all the starting nodes (in-degree = zero)
        # for all of their neighbors, reduce their in-degree

        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for src, dest in prerequisites:
            indegree[dest] += 1
            graph[src].append(dest)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        seen = len(q)

        while q:
            vert = q.popleft()

            for neigh in graph[vert]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    q.append(neigh)
                    seen += 1
        
        return seen == numCourses



        