#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:50:04 2020
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
@author: chengchen
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        else:
            res = 0
            for i in range(1,len(points)):
                d1 = points[i][0]-points[i-1][0]
                d2 = points[i][1]-points[i-1][1]
                res += max(abs(d1), abs(d2))
            return res