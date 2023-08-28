#################################################################################################################################################################################################################################
### Binary Gap
### Codility Test Project
### Author: Amanda Madden
### Modified: 8/28/2023
### Input: integer    Output: max count of 0's
### Description: A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
###              Takes in an integer and converts it to binary. Splices the 0b off the converted binary value. Finds a 1 and counts the number of 0's until the next 1. Returns the largest count of 0's. 
#################################################################################################################################################################################################################################
##A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
##
##For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
##
##Write a function:
##
##def solution(N)
##
##that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
##
##For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
##
##Write an efficient algorithm for the following assumptions:
##
##N is an integer within the range [1..2,147,483,647].
#################################################################################################################################################################################################################################

def solution(N):
    binary = bin(N)
    b = str(binary)[2:]

    count = 0
    max_zeros= 0
    for bit in b:
        if bit == '0':
            count+=1
        elif bit == '1':
            max_zeros = max(max_zeros, count)
            count=0

    return max_zeros
