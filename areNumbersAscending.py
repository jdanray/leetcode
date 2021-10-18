# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/ 

class Solution(object):
	def areNumbersAscending(self, s):
		prev = -1
		tokens = s.split()
		for t in tokens:
			if t.isnumeric():
				if int(t) > prev:
					prev = int(t)
				else:
					return False

		return True
