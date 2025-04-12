# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution(object):
	def minOperations(self, boxes):
		N = len(boxes)

		res = [0 for _ in range(N)]
		def traverse(indexes):
			ones = 0
			moves = 0
			for i in indexes:
				moves += ones
				res[i] += moves
				if boxes[i] == '1':
					ones += 1

		traverse(range(N))
		traverse(range(N - 1, -1, -1))

		return res

class Solution(object):
	def minOperations(self, boxes):
		N = len(boxes)

		ones = 0
		moves = 0
		res = [0 for _ in range(N)]
		for i in range(N):
			moves += ones
			res[i] += moves
			if boxes[i] == '1':
				ones += 1

		ones = 0
		moves = 0
		for i in range(N - 1, -1, -1):
			moves += ones
			res[i] += moves
			if boxes[i] == '1':
				ones += 1

		return res