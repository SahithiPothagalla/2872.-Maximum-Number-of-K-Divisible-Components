class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adjList = collections.defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        self.ans = 0
        visited = set()
        visited.add(0)
        def dfs(node):
            total = values[node]
            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    isValid, temp = dfs(nei)
                    if not isValid:
                        total += temp
            if total % k == 0:
                self.ans+=1
                return (True,0) 
            else:
                return (False,total)

        dfs(0)
        return self.ans
