# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/ 

# recursive
class Solution(object):
	def executeInstructions(self, n, startPos, s):
		move = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}

		def execute(x, y, i):
			if i >= len(s):
				return 0

			addx, addy = move[s[i]]
			newx = x + addx
			newy = y + addy

			if newx < 0 or newx >= n or newy < 0 or newy >= n:
				return 0
			else:
				return 1 + execute(newx, newy, i + 1)

		res = []
		for i in range(len(s)):
			res.append(execute(startPos[0], startPos[1], i))

		return res

# manual stack
class Solution(object):
	def executeInstructions(self, n, startPos, s):
		move = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}

		stack = []
		for i in range(len(s)):
			stack.append([startPos[0], startPos[1], 0, i, i])

		res = [0 for _ in range(len(s))]
		while stack:
			x, y, m, i, idx = stack.pop()

			if i >= len(s):
				res[idx] = m
				continue

			addx, addy = move[s[i]]
			newx = x + addx
			newy = y + addy

			if newx < 0 or newx >= n or newy < 0 or newy >= n:
				res[idx] = m
			else:
				stack.append([newx, newy, m + 1, i + 1, idx])

		return res
