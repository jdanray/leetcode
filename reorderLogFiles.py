# https://leetcode.com/problems/reorder-data-in-log-files/ 

class Solution(object):
	def reorderLogFiles(self, logs):
		letter = []
		digit = []
		for l in logs:
			if l.split()[1][0].isdigit():
				digit.append(l)
			else:
				letter.append(l)

		letter = sorted(letter)
		letter = sorted(letter, key=lambda l: " ".join(l.split()[1:]))
		return letter + digit
