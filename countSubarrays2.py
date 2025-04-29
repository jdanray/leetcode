# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution(object):
	def countSubarrays(self, nums, k):
		m = max(nums)
		numMax = 0
		i = 0
		res = 0
		for n in nums:
			if n == m:
				numMax += 1

			while numMax == k:
				if nums[i] == m:
					numMax -= 1
				i += 1

			res += i

		return res

class Solution(object):
	def countSubarrays(self, nums, k):
		idx = collections.deque()
		m = max(nums)
		res = 0
		for (i, n) in enumerate(nums):
			if n == m:
				idx.append(i)

			if len(idx) > k:
				idx.popleft()

			if len(idx) == k:
				res += idx[0] + 1

		return res