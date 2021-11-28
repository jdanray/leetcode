# https://leetcode.com/problems/k-radius-subarray-averages/ 

# sliding-window solution

class Solution(object):
	def getAverages(self, nums, k):
		N = len(nums)

		k2 = k * 2
		res = [-1 for _ in range(N)]
		s = 0
		for i in range(N):
			s += nums[i]

			if i >= k2:
				res[i - k] = s / (k2 + 1)
				s -= nums[i - k2]

		return res

# prefix-sum solution

class Solution(object):
	def getAverages(self, nums, k):
		N = len(nums)
		subarrSize = 2 * k + 1

		prefixSum = [0 for _ in range(N + 1)]
		for i in range(N):
			prefixSum[i + 1] = prefixSum[i] + nums[i]

		res = [-1 for _ in range(N)]
		for j in range(k, N - k):
			res[j] = (prefixSum[j + k + 1] - prefixSum[j - k]) / subarrSize

		return res
