# https://leetcode.com/problems/long-pressed-name/ 

class Solution(object):
	def isLongPressedName(self, name, typed):
		i = 0
		j = 0
		while i < len(name) and j < len(typed):
			if typed[j] == name[i]:
				i += 1
				j += 1
			elif i - 1 >= 0 and name[i - 1] == typed[j]:
				j += 1
			else:
				return False

		if i < len(name):
			return False

		while j < len(typed) and typed[j] == name[i]:
			j += 1

		return j == len(typed)
