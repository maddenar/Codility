#################################################################################################################################################################################################################################
### PassingCars
### Codility Test Project
### Author: Amanda Madden
### Modified: 8/31/2023
### Input: non-empty integer array of 0 or 1   Output: number of 'passing cars'
### Description: The index of 0 has to be less than the index of 1 to be considered passing. Hence if they array starts with a 1, it does not pass any cars. 
###              The 0's are counted as east, and then if a 1 is encountered in a later index they are counted as a pair. Return -1 is limit is reached. 
###              
#################################################################################################################################################################################################################################
##A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
##
##Array A contains only 0s and/or 1s:
##
##0 represents a car traveling east,
##1 represents a car traveling west.
##The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
##
##For example, consider array A such that:
##
##  A[0] = 0
##  A[1] = 1
##  A[2] = 0
##  A[3] = 1
##  A[4] = 1
##We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
##
##Write a function:
##
##def solution(A)
##
##that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
##
##The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
##
##For example, given:
##
##  A[0] = 0
##  A[1] = 1
##  A[2] = 0
##  A[3] = 1
##  A[4] = 1
##the function should return 5, as explained above.
##
##Write an efficient algorithm for the following assumptions:
##
##N is an integer within the range [1..100,000];
##each element of array A is an integer that can have one of the following values: 0, 1.
#################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################

def solution(A):
    road = A
    east= 0
    pairs = 0
    limit = 1000000000
    
    for car in road:
        if car == 0:
            east += 1
        else:
            pairs += east
            if pairs > limit:
                return -1
    
    return pairs



