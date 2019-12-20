'''
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


Test Cases Ran:

[[1,2],[2,3],[3,4],[4,5],[5,6]]
[[1,3],[2,6],[6,7],[8,10],[15,18]]
[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
[]
[[1,4],[0,4]]
[[1,4],[0,1]]
[[1,4],[2,3]]
[[1,4],[0,0]]
[[2,3],[4,5],[6,7],[8,9],[1,10]]

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return []
        
        intervals.sort()
        
        i = 1
        while i < len(intervals): 
            if intervals[i-1][1] >= intervals[i][0] and ( intervals[i-1][0] <= intervals[i][0] or intervals[i-1][0] <= intervals[i][1] ):
                intervals[i-1] = [min(intervals[i-1][0], intervals[i][0]), max(intervals[i-1][1], intervals[i][1])]
                del intervals[i]
            else:
                i += 1
                
                
        return intervals