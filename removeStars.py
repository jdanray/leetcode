# https://leetcode.com/problems/removing-stars-from-a-string/ 

class Solution(object):
	def removeStars(self, s):
		remove = set()
		n = 0
		for i in range(len(s) - 1, -1, -1):
			if s[i] == '*':
				remove.add(i)
				n += 1
			elif n > 0:
				remove.add(i)
				n -= 1

		return ''.join(c for i, c in enumerate(s) if i not in remove)
