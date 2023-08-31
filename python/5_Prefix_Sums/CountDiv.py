#################################################################################################################################################################################################################################
### CountDiv
### Codility Test Project
### Author: Amanda Madden
### Modified: 8/31/2023
### Input: lower/upper of range, integer   Output: how many numbers within the range is divisible by the given integer
### Description: Get the range from the first multiple of num that is not num and the given high range. Divide that by num to get how many mulitples there are and add 1 to account for num itself. 
###              
#################################################################################################################################################################################################################################
##Write a function:
##
##def solution(A, B, K)
##
##that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
##
##{ i : A ≤ i ≤ B, i mod K = 0 }
##
##For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
##
##Write an efficient algorithm for the following assumptions:
##
##A and B are integers within the range [0..2,000,000,000];
##K is an integer within the range [1..2,000,000,000];
##A ≤ B.
#################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################
## 50% not efficient enough : O(B-A)
## 
##def solution(A, B, K):
##    low = A
##    high = B
##    num = K
##    count = 0
##
##    for i in range(low, high+1):
##        if i % num == 0:
##            count += 1
##
##    return count
#################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################

def solution(A, B, K):
    low = A
    high = B
    num = K
    count = 0

    ## Calculate the smallest multiple
    ## Get the number before the first multiple
    ## Floor division to round down when dividing by num
    ## Multiply that by num to get the first multiple of the num that is not the num
    first = (low + num - 1) // num * num

    ## num will always be at least 1 
    ## Get the range for the first multiple and the given high integer
    ## Divide by num to see how many instances of num fit into the range
    count = (high - first) // num

    ## Add on the first multiple
    return count + 1




