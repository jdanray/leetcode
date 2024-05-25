# https://leetcode.com/problems/maximum-good-people-based-on-statements/ 

class Solution(object):
	def maximumGood(self, states):
		N = len(states)
		res = 0
		for b in range(1, 2 ** N):
			if all(states[i][j] == 2 or states[i][j] == (b >> j) & 1 for j in range(N) for i in range(N) if (b >> i) & 1 == 1):
				res = max(res, sum((b >> k) & 1 for k in range(N)))
		return res

class Solution(object):
	def maximumGood(self, states):
		N = len(states)

		res = 0
		for b in range(1, 2 ** N):
			isValid = True
			for i in range(N):
				if (b >> i) & 1 == 0:
					continue

				if any(states[i][j] != 2 and states[i][j] != (b >> j) & 1 for j in range(N)):
					isValid = False
					break

			if isValid:
				n = 0
				for k in range(N):
					n += (b >> k) & 1
				res = max(res, n)

		return res
