# https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution(object):
	def subarraysWithKDistinct(self, nums, k):
		def atMost(k):
			i = 0
			res = 0
			count = collections.Counter()
			for j, n in enumerate(nums):
				count[n] += 1

				while len(count) > k:
					x = nums[i]
					count[x] -= 1
					if count[x] == 0:
						del count[x]
					i += 1

				res += (j - i + 1)

			return res

		return atMost(k) - atMost(k - 1)
