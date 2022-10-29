# https://leetcode.com/problems/words-within-two-edits-of-dictionary/ 

class Solution(object):
	def twoEditWords(self, queries, dictionary):
		N = len(queries[0])

		res = []
		for q in queries:
			incl = False
			for d in dictionary:
				diff = 0
				for i in range(N):
					if q[i] != d[i]:
						diff += 1

				if diff <= 2:
					incl = True

			if incl:
				res.append(q)

		return res
