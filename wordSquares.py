# https://leetcode.com/problems/word-squares-ii/

class Solution(object):
	def wordSquares(self, words):
		words = sorted(words)

		res = []
		for i, top in enumerate(words):
			for j, left in enumerate(words):
				if j == i or left[0] != top[0]:
					continue

				for k, right in enumerate(words):
					if k in [i, j] or right[0] != top[-1]:
						continue

					for l, bottom in enumerate(words):
						if l in [i, j, k] or bottom[0] != left[-1] or bottom[-1] != right[-1]:
							continue

						res.append([top, left, right, bottom])

		return res