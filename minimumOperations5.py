# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution(object):
	def minimumOperations(self, nums):
		OP = 3

		count = collections.Counter(nums)
		nondistinct = sum(count[n] > 1 for n in count)
		res = 0
		for i in range(0, len(nums), OP):
			if nondistinct == 0:
				return res

			res += 1
			for j in range(OP):
				k = i + j
				if k < len(nums):
					count[nums[k]] -= 1
					if count[nums[k]] == 1:
						nondistinct -= 1

		return res