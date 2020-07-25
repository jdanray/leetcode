# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/ 

class Solution(object):
	def countOdds(self, low, high):
		res = (high - low) // 2
		if low % 2 == 1 or high % 2 == 1:
			res += 1
		return res
