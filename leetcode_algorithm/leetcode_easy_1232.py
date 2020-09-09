"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #今天不开心。不开心的时候打中文。也没有什么特别的原因，大概天气转凉了。成年人的不开心就是默默买几罐啤酒然后再买一杯奶茶。
        #两点确定一条直线。用y=kx+b。
        #先考虑特殊情况k=+inf
        if coordinates[0][0]==coordinates[1][0]:
            x = coordinates[0][0]
            for i in range(2, len(coordinates)):
                if coordinates[i][0]!=x:
                    return False
            return True
        #接下来正常求斜率+截距。
        k = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        b = coordinates[0][1] - coordinates[0][0]*k
        for i in range(2, len(coordinates)):
            if coordinates[i][1] - coordinates[i][0]*k - b != 0:
                return False
        return True