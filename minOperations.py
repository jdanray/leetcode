# https://leetcode.com/problems/minimum-operations-to-make-array-equal/  

class Solution(object):
	def minOperations(self, n):
		arr = [(2 * i) + 1 for i in range(n)]
		median = arr[n // 2]
		res = 0
		for a in arr:
			res += abs(a - median)
		return res // 2

"""
The above solution uses O(n) space, but that isn't necessary. I came up with the following solution that uses O(1) space.
"""

class Solution(object):
	def minOperations(self, n):
		median = 2 * (n // 2) + 1
		a = 1
		res = 0
		for _ in range(n):
			res += abs(a - median)
			a += 2
		return res // 2

"""
After I solve a problem, I like to examine other people's solutions. The following code is my Python version of the simplest and fastest solution I found. The following URL links to the solution I found:

https://leetcode.com/problems/minimum-operations-to-make-array-equal/discuss/794229/C%2B%2B-1-liner-O(1)-solution-(return-n*n4)-beats-100-with-detailed-explanation
"""

class Solution(object):
	def minOperations(self, n):
		return (n * n) // 4
