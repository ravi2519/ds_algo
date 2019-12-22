'''

https://leetcode.com/problems/critical-connections-in-a-network/
https://stackoverflow.com/a/11221469/414744

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

'''


from Listin import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.node = 0
        
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        # create the edges using a dict
        graph = defaultdict(list)
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        res = []
        low = [-1]*n
        dist = [-1]*n
        visited=[False]*n
        parent=[-1]*n
        
        self.DFS(0, graph, visited, low, dist, parent, res)
        
        return res
                
    def DFS( self, i, graph, visited, low, dist, parent, res):
        visited[i] = True
        dist[i] = low[i] = self.node
        
        self.node += 1
        
        for j in graph[i]:
            if not visited[j]:
                parent[j] = i
                self.DFS(j, graph, visited, low, dist, parent, res)
                low[i] = min( low[i], low[j] )
                if low[j] == dist[j]:
                    res.append([i, j])
            elif parent[i] != j:
                low[i] = min( low[i], low[j] )
                
        
        
        