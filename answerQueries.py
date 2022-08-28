# https://leetcode.com/problems/longest-subsequence-with-limited-sum/ 

class Solution(object):
	def answerQueries(self, nums, queries):
		nums = sorted(nums)
		res = []
		for q in queries:
			s = 0
			l = 0
			for n in nums:
				if s + n > q:
					break
				else:
					s += n
					l += 1

			res.append(l)

		return res
