# https://leetcode.com/problems/kth-missing-positive-number/

class Solution(object):
	def findKthPositive(self, arr, k):
		m = 1
		for n in arr:
			while m < n and k > 0:
				m += 1
				k -= 1

			if k == 0:
				return m - 1

			m += 1

		return arr[-1] + k

"""
The following program is simpler than the above program. 

However, there is an issue with the following program: The loop doesn't make progress toward termination at each iteration.

But the loop is guaranteed to terminate: n increases at each iteration, and arr must have finite length. So, eventually n will be greater than the greatest element of arr, and then n won't be in arr. Then k will surely decrease until it reaches 0, and then the loop terminates.
"""

class Solution(object):
	def findKthPositive(self, arr, k):
		arr = set(arr)
		n = 0
		while k > 0:
			n += 1
			if n not in arr:
				k -= 1
		return n 
