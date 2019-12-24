from leetcode import rotate_array, point_of_lattice

'''
rotate_array
'''
nums = [1,2,3,4,5,6,7]
k = 3

s = rotate_array.Solution()
s.rotate(nums, k )
print(nums)


'''
Point Of Lattice
'''

s = point_of_lattice.Solution()
r = s.move_90_deg( -1, 3, 3, 1)
print(r)