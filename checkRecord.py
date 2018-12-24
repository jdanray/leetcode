# https://leetcode.com/problems/student-attendance-record-i/description/

class Solution:
	def checkRecord(self, s):
		nabsences = 0
		i = 0
		while i < len(s):
			if s[i] == 'A':
				nabsences += 1
			if nabsences > 1:
				return False

			if s[i] != 'L':
				i += 1
				continue

			nlates = 0
			while i < len(s) and s[i] == 'L':
				i += 1
				nlates += 1
			if nlates > 2:
				return False

		return True
