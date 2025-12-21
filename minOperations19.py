# https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

class Solution(object):
	def minOperations(self, nums):
		count = collections.Counter(nums)
		ndups = sum(count[n] > 1 for n in count)

		if ndups == 0:
			return 0

		res = 0
		for i in range(0, len(nums), 3):
			for j in [i, i + 1, i + 2]:
				if j >= len(nums):
					break

				count[nums[j]] -= 1
				if count[nums[j]] == 1:
					ndups -= 1

			res += 1
			if ndups == 0:
				return res

		return res