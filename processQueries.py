# https://leetcode.com/problems/queries-on-a-permutation-with-key/ 

class Solution(object):
	def processQueries(self, queries, m):
		pos = {n: n - 1 for n in range(1, m + 1)}
		num = {n: n + 1 for n in range(m)}

		res = []
		for q in queries:
			res.append(pos[q])

			for i in range(pos[q], -1, -1):
				pos[num[i]] += 1

				if i > 0: 
					num[i] = num[i - 1]

			pos[q] = 0
			num[0] = q

		return res
