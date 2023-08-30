#################################################################################################################################################################################################################################
### MissingInteger
### Codility Test Project
### Author: Amanda Madden
### Modified: 8/30/2023
### Input: integer array   Output: smallest positive integer not in given array
### Description: Store positive integers in a set so there are no dupes. If the positive number set is empty, that means all values were negative and return 1.
###              Find the max positive value of the set and that number + 2 will be the upper value to ensure all values are covered. 
###              
#################################################################################################################################################################################################################################
##Write a function:
##
##def solution(A)
##
##that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
##
##For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
##
##Given A = [1, 2, 3], the function should return 4.
##
##Given A = [−1, −3], the function should return 1.
##
##Write an efficient algorithm for the following assumptions:
##
##N is an integer within the range [1..100,000];
##each element of array A is an integer within the range [−1,000,000..1,000,000].
#################################################################################################################################################################################################################################

#################################################################################################################################################################################################################################

def solution(A):
    array = A
    posNum = set(num for num in array if num > 0)

    if not (posNum):
        return 1

    maxPos = max(posNum)

    for i in range(1, maxPos+2):
        if i not in posNum:
            return i



