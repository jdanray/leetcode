# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/ 

class Solution(object):
	def maxOperations(self, s):
		ones = 0
		res = 0
		for i, c in enumerate(s):
			if c == '1':
				ones += 1
			elif i - 1 >= 0 and s[i - 1] == '1':
				res += ones
		return res

class Solution(object):
	def maxOperations(self, s):
		ones = 0
		res = 0
		for i, c in enumerate(s):
			if c == '1':
				ones += 1
				if i + 1 < len(s) and s[i + 1] == '0':
					res += ones
		return res
