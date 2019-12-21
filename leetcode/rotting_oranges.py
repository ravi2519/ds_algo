'''
https://leetcode.com/problems/rotting-oranges/

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 
Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

Testcases:
[[2,1,1],[1,1,0],[0,1,1]]
[[2,1,1],[0,1,1],[1,0,1]]
[[0,2]]
[[1],[2]]

'''

from listin import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Get rows and cols
        nr_rows = len(grid)
        nr_cols = len(grid[0])
        
        self.rows = nr_rows
        self.cols = nr_cols
        
        # Queue to store rotten oranges
        queue = []
        
        # Fill the Queue
        for i in range(nr_rows):
            for j in range(nr_cols):
                if grid[i][j] == 2:
                    queue.append( Orange(i, j, 0))
        
        # Start polling the queue
        res = 0
        while len(queue) > 0:
            orange = queue.pop(0)
            
            if orange.layer > res:
                res = orange.layer
            
            # check if upper orange is fresh
            if self.inside( orange.i - 1, orange.j ) and grid[orange.i - 1][orange.j] == 1:
                queue.append( Orange(orange.i - 1, orange.j, orange.layer + 1) )
                grid[orange.i - 1][orange.j] = 2
            
            # check if right orange is fresh 
            if self.inside( orange.i, orange.j + 1 ) and grid[orange.i][orange.j + 1] == 1:
                queue.append( Orange(orange.i, orange.j + 1, orange.layer + 1) )
                grid[orange.i][orange.j + 1] = 2
                
            # check if bottom orange is fresh 
            if self.inside( orange.i + 1, orange.j ) and grid[orange.i + 1][orange.j] == 1:
                queue.append( Orange(orange.i + 1, orange.j, orange.layer + 1) )
                grid[orange.i + 1][orange.j] = 2
            
            # check if left orange is fresh 
            if self.inside( orange.i, orange.j - 1 ) and grid[orange.i][orange.j - 1] == 1:
                queue.append( Orange(orange.i, orange.j - 1, orange.layer + 1) )
                grid[orange.i][orange.j - 1] = 2
            
        # check if any fresh orange left
        for i in range(nr_rows):
            for j in range(nr_cols):
                if grid[i][j] == 1:
                    return -1
        
        return res
            
            
    def inside( self, i, j ):
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols:
            return False
        else:
            return True
        
class Orange:
    
    def __init__( self, i, j, layer):
        self.i = i
        self.j = j
        self.layer = layer