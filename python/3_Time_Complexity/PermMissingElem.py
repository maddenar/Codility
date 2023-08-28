#################################################################################################################################################################################################################################
### PermMissingElem
### Codility Test Project
### Author: Amanda Madden
### Modified: 8/28/2023
### Input: integer array   Output: the missing element
### Description: An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing. Your goal is to find that missing element.
###		 The array starts at 1 and can up to N integers. If the array is empty, it is missing 1. If the array is length of 1, then either 1 or 2 is missing. 
### 		 Else sum up the numbers in the array and what the range would sum up to if all the elements were present. The difference of those will be the missing element. 		  
###              
#################################################################################################################################################################################################################################
##An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
##
##Your goal is to find that missing element.
##
##Write a function:
##
##def solution(A)
##
##that, given an array A, returns the value of the missing element.
##
##For example, given array A such that:
##
##  A[0] = 2
##  A[1] = 3
##  A[2] = 1
##  A[3] = 5
##the function should return 4, as it is the missing element.
##
##Write an efficient algorithm for the following assumptions:
##
##N is an integer within the range [0..100,000];
##the elements of A are all distinct;
##each element of array A is an integer within the range [1..(N + 1)].
#################################################################################################################################################################################################################################

def solution(A):
    array = A
    length = len(A)

    ## Empty array, return 1
    if length == 0:
        return 1
    elif length == 1:
        if array[0] == 1:
            return 2
        if array[0] == 2:
            return 1
    else:
        arraySum = sum(array)
        expectedSum =  ((length+1) * (length +2)) // 2 
        answer = expectedSum - arraySum

        return answer
