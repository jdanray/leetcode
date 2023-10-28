# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution(object):
	def constructDistancedSequence(self, n):
		def backtrack(i, seq, used):
			if i >= len(seq):
				return seq

			if seq[i] != 0:
				return backtrack(i + 1, seq, used)

			for x in range(n, 0, -1):
				if not used[x] and (x == 1 or (i + x < len(seq) and seq[i + x] == 0)):
					used[x] = True
					seq[i] = x
					if x != 1:
						seq[i + x] = x

					res = backtrack(i + 1, seq, used)
					if res:
						return res

					used[x] = False
					seq[i] = 0
					if x != 1:
						seq[i + x] = 0

		return backtrack(0, [0 for _ in range(2 * n - 1)], [False for _ in range(n + 1)])
