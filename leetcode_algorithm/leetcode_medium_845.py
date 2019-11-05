#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:29:44 2019

@author: chengchen


Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.


"""
A = [2,2,2]
def longestMountain(A):
    max_m = 0 # store the length of the longest mountain
    cur_m = 0 # the length of the current mountain
    status = 0 # 0: no mountain in record, 1: uphill, 2: downhill
    new_status = 0
    if len(A)<3:
        return 0
    else:
        for i in range(1,len(A)):
            #print('status',status)
            status = new_status
            if status == 0:
                cur_m = 0
                if A[i]>A[i-1]:
                    new_status = 1
                    cur_m += 1
            
            if status == 1: # uphilling
                if A[i]==A[i-1]:
                    new_status = 0 # flat, go back to search for mountain
                else:
                    if A[i]<A[i-1]:
                        new_status = status + 1 # downhilling
                    cur_m += 1
                    if new_status == 2:
                        max_m = max(max_m, cur_m)                        
            if status == 2: # downhilling
                if A[i]==A[i-1]:
                    new_status = 0
                else:
                    if A[i]<A[i-1]:
                        cur_m += 1
                        max_m = max(max_m, cur_m)
                    if A[i]>A[i-1]: # uphilling
                        new_status = 1
                        cur_m = 1
    if max_m>0:
        max_m += 1
    return(max_m)
print(longestMountain(A))


            