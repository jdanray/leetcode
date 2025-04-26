# https://leetcode.com/problems/find-the-most-common-response/

class Solution(object):
	def findCommonResponse(self, responses):
		count = collections.Counter()
		m = float('-inf')
		res = ''
		for resp in responses:
			for r in set(resp):
				count[r] += 1

				if count[r] > m:
					m = count[r]
					res = r
				elif count[r] == m and (not res or r < res):
					res = r

		return res