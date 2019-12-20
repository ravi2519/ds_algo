'''
https://leetcode.com/discuss/interview-question/396418/

'''

class Solution:
  def move_90_deg( self, ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay

    # Moving 90 degress
    # https://math.stackexchange.com/questions/1330161/how-to-rotate-points-through-90-degree
    rx = dy
    ry = -dx

    # GCD to get the first vector
    div = abs( self.gcd( rx, ry) )

    rx /= div
    ry /= div

    # Adding the origin x an y to approach the next Lattice
    return ( bx + rx, by + ry)
  
  def gcd(self, x, y):
    if y == 0:
      return x
    else:
      return self.gcd( y, x%y )
