#################################################################################################################################################################################################################################
### PermCheck
### Codility Test Project
### Author: Amanda Madden
### Modified: 8/29/2023
### Input: non-empty integer array   Output: if the array is a permutation
### Description: Initialize an array to all to zero. Then iterate through the array and make sure that all elements are within the 1-n range and checks for duplicates. 
###              
#################################################################################################################################################################################################################################
##A non-empty array A consisting of N integers is given.
##
##A permutation is a sequence containing each element from 1 to N once, and only once.
##
##For example, array A such that:
##
##    A[0] = 4
##    A[1] = 1
##    A[2] = 3
##    A[3] = 2
##is a permutation, but array A such that:
##
##    A[0] = 4
##    A[1] = 1
##    A[2] = 3
##is not a permutation, because value 2 is missing.
##
##The goal is to check whether array A is a permutation.
##
##Write a function:
##
##def solution(A)
##
##that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
##
##For example, given array A such that:
##
##    A[0] = 4
##    A[1] = 1
##    A[2] = 3
##    A[3] = 2
##the function should return 1.
##
##Given array A such that:
##
##    A[0] = 4
##    A[1] = 1
##    A[2] = 3
##the function should return 0.
##
##Write an efficient algorithm for the following assumptions:
##
##N is an integer within the range [1..100,000];
##each element of array A is an integer within the range [1..1,000,000,000].
#################################################################################################################################################################################################################################
## These are all the test cases that needed to be tested to get 100%
##[2 3 4 5]
##[2 3 4 1]
##[1]
##[2]
##[0]
##[]
##[1 1 2 2 3 4]
##[2 2 3 5]
##[1 1 2 3 4]
##[1 2 3 3 4 5 5]
#################################################################################################################################################################################################################################

def solution(A):
    n = len(A)
    occurrences = [0] * n
    
    for value in A:
        if not 1 <= value <= n:
            return 0
        occurrences[value - 1] += 1
        if occurrences[value - 1] > 1:
            return 0
    
    if all(count == 1 for count in occurrences):
        return 1
    else:
        return 0
