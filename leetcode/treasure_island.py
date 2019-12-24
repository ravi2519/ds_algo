
from Listin import List

class Solution:
  def treasureIsland(self, grid: List[List[str]] ) -> int:

    steps = 0
    self.bfs(grid, 0, 0, steps)

  def bfs(self, grid, i, j, steps):
    if grid[i][j] == 'D':
      return
    
    if grid[i][j] == 
    
