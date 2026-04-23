# https://leetcode.com/problems/sum-of-distances/

class Solution(object):
	def distance(self, nums):
		N = len(nums)

		def do_sum(r):
			# seen[n] == [sum of prev dists, count of n's, index of last n]
			seen = dict()
			for i in r:
				n = nums[i]
				if n in seen:
					s, c, j = seen[n]
					d = abs(i - j)
					snew = s + (d * c)
					sums[i] += snew
					seen[n] = [snew, c + 1, i]
				else:
					seen[n] = [0, 1, i]

		sums = [0 for _ in range(N)]
		do_sum(range(N))
		do_sum(reversed(range(N)))

		return sums