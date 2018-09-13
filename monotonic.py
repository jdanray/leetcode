# https://leetcode.com/contest/weekly-contest-100/problems/monotonic-array/

class Solution(object):
    def isMonotonic(self, A):
        # base case
        if len(A) == 1:
            return True
        
        # a monotonic array is either monotonic increasing or monotonic decreasing
        # so, we will tag it as increasing or decreasing
        # but we can't decide until we see a number different from the first number
        
        i = 1
        while i < len(A) and A[i] == A[i - 1]:
            i += 1
    
        # after the while loop,
        # i >= len(A) or A[i] != A[i - 1]
        
        if i >= len(A):
            return True
        
        # A[i] != A[i - 1]
        # so, A[i] > A[i - 1] or A[i] < A[i - 1]
        
        inc = False
        dec = False
        if A[i] > A[i - 1]:
            inc = True
        else:
            dec = True
            
        # check whether the array remains monotonic
        
        for j in range(i + 1, len(A)):
            if A[j] < A[j - 1] and inc:
                return False
            elif A[j] > A[j - 1] and dec:
                return False
            
        return True
