# https://leetcode.com/problems/move-pieces-to-obtain-a-string/ 

class Solution(object):
	def canChange(self, start, targ):
		N = len(start)

		if start.count('R') != targ.count('R') or start.count('L') != targ.count('L'):
			return False

		r = 0
		for i in range(N):
			if start[i] == 'R':
				r += 1
			elif start[i] == 'L' or targ[i] == 'L':
				r = 0

			if targ[i] == 'R':
				if r == 0:
					return False
				else:
					r -= 1

		if r > 0:
			return False

		l = 0
		for i in range(N - 1, -1, -1):
			if start[i] == 'L':
				l += 1
			elif start[i] == 'R' or targ[i] == 'R':
				l = 0

			if targ[i] == 'L':
				if l == 0:
					return False
				else:
					l -= 1

		if l > 0:
			return False

		return True