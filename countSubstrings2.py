# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/ 

class Solution(object):
	def countSubstrings(self, s, c):
		count = 0
		res = 0
		for x in s:
			if x == c:
				count += 1
				res += count
		return res
