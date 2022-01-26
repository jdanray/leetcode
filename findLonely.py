# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

class Solution(object):
	def findLonely(self, nums):
		nums = sorted(nums)
		res = []
		for i, n in enumerate(nums):
			if (i - 1 < 0 or nums[i - 1] not in [n, n - 1]) and (i + 1 >= len(nums) or nums[i + 1] not in [n, n + 1]):
				res.append(n)
		return res

class Solution(object):
	def findLonely(self, nums):
		nums = sorted(nums)
		return [n for i, n in enumerate(nums) if (i - 1 < 0 or nums[i - 1] not in [n, n - 1]) and (i + 1 >= len(nums) or nums[i + 1] not in [n, n + 1])]

class Solution(object):
	def findLonely(self, nums):
		count = collections.Counter(nums)
		return [n for n in range(max(nums) + 1) if count[n] == 1 and not count[n - 1] and not count[n + 1]]
