
'''
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


from Listin import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # it will be a DFS solution
        # loop through the grid to get first 1
        
        nr_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # now mark all horizontal and vertical ones with 2
                    self.DFS(grid, i, j)
                    nr_islands += 1
                    
        return nr_islands
    
    def DFS(self, grid, i, j):
        if self.not_inner(grid, i, j) or grid[i][j] != '1':
            #print(i, j)
            return
        
        grid[i][j] = '2'
        
        # check above
        self.DFS(grid, i-1, j)
        
        #check right
        self.DFS(grid, i, j+1)
        
        #check bottom
        self.DFS(grid, i+1, j)
        
        #check left
        self.DFS(grid, i, j-1)
    
    def not_inner(self, grid, i, j):
        return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])
        

