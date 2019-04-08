# https://leetcode.com/problems/camelcase-matching/

class Solution:
	def camelMatch(self, queries, pattern):
		res = []
		for query in queries:
			j = 0
			for i in range(len(query)):
				if j < len(pattern) and query[i] == pattern[j]:
					j += 1
				elif query[i].isupper():
					break

			res.append(i + 1 == len(query) and j == len(pattern))

		return res
