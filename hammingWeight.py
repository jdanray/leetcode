# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
	def hammingWeight(self, n):
		res = 0
		while n > 0:
			if n & 1 == 1:
				res += 1
			n >>= 1

		return res

"""
After I solve a problem, I like to look at other people's solutions. The solution found here has a better time performance in the average case: https://leetcode.com/problems/number-of-1-bits/discuss/55255/C%2B%2B-Solution%3A-n-and-(n-1)

At each iteration, the program drops the lowest set bit in n by setting n to n & (n - 1). So, the number of iterations is equal to the number of set bits in n. Here is my Python implementation of the program:
"""

class Solution(object):
	def hammingWeight(self, n):
		res = 0
		while n > 0:
			n &= (n - 1)
			res += 1

		return res
