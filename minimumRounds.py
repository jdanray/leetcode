# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/ 

class Solution(object):
	def minimumRounds(self, tasks):
		count = collections.Counter(tasks).values()
		res = 0
		for c in count:
			if c < 2:
				return -1

			res += (c // 3)
			res += (c % 3 > 0)

		return res
