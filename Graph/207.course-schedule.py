class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list 
        graph = {i : [] for i in range(numCourses)}
        
        for task, prereq in prerequisites: 
            graph[task].append(prereq)

        # build indegree list
        indegree = self.getIndegree(graph)
        # add task with 0 indegree to q 
        q = [] 
        
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)

        while q:
            node = q.pop(0)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        for task in indegree:
            # impossible to complete
            if indegree[task] != 0:
                return False
        return True



    def getIndegree(self,graph):
        indegree = {task : 0 for task in graph}

        for task in graph:
            for prereq in graph[task]:
                indegree[prereq] += 1
        
        return indegree
            
