# https://leetcode.com/problems/count-the-hidden-sequences/ 

class Solution(object):
	def numberOfArrays(self, differences, lower, upper):
		s = 0
		maxim = float('-inf')
		minim = float('inf')
		for d in differences:
			s += d
			maxim = max(maxim, s)
			minim = min(minim, s)

		return sum(a + maxim <= upper and a + minim >= lower for a in range(lower, upper + 1))

"""
After I solve a problem, I like to study other people's solutions.

I found a faster solution here: https://leetcode.com/problems/count-the-hidden-sequences/discuss/1709755/JavaC%2B%2BPython-Straight-Forward-Solution-with-Explantion
"""

class Solution(object):
	def numberOfArrays(self, differences, lower, upper):
		s = 0
		maxim = 0
		minim = 0
		for d in differences:
			s += d
			maxim = max(maxim, s)
			minim = min(minim, s)

		return max(0, (upper - lower) - (maxim - minim) + 1)
