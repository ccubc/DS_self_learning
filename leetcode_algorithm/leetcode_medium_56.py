"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals using the left value
        intervals.sort(key = lambda x: x[0])
        res = []        
        for interval in intervals:
            # if the list of merged intervals is empty or if the current interval doesn't overlap with previous, then append the current interval
            if (not res) or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # otherwise, there is overlap, so we update the result to merge the overlapping intervals
                res[-1][1] = max(res[-1][1], interval[1])
        return res