# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution(object):
	def largestCombination(self, candidates):
		bit = collections.Counter()
		for c in candidates:
			i = 0
			while c > 0:
				bit[i] += (c & 1)
				i += 1
				c >>= 1
		return max(bit.values())

"""
After I solve a problem, I like to study other people's solutions. I found solutions that don't use a dictionary/counter, and I implemented the idea below: 
"""

class Solution(object):
	def largestCombination(self, candidates):
		res = 0
		for i in range(30):
			b = 0
			for c in candidates:
				b += (c >> i) & 1
			res = max(res, b)
		return res

class Solution(object):
	def largestCombination(self, candidates):
		return max(sum((c >> i) & 1 for c in candidates) for i in range(30))
