# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/ 

class Solution(object):
	def closetTarget(self, words, target, startIndex):
		N = len(words)

		res = float('inf')
		for d in range(N):
			if words[(startIndex + d) % N] == target:
				res = min(res, d)

			if words[(startIndex - d) % N] == target:
				res = min(res, d)

		return -1 if res == float('inf') else res

class Solution(object):
	def closetTarget(self, words, target, startIndex):
		N = len(words)

		res = float('inf')
		for d in range(N):
			for sgn in [1, -1]:
				if words[(startIndex + d * sgn) % N] == target:
					res = min(res, d)

		return -1 if res == float('inf') else res
