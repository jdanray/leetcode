# https://leetcode.com/problems/find-all-good-indices/ 

class Solution(object):
	def goodIndices(self, nums, k):
		N = len(nums)

		def tonic(r, d):
			res = [0 for _ in range(N)]
			l = 1
			for i in r:
				res[i] = l
				if nums[i] <= nums[i + d]:
					l += 1
				else:
					l = 1 
			return res

		noninc = tonic(range(1, N), -1)
		nondec = tonic(range(N - 2, -1, -1), 1)

		return [i for i in range(k, N - k) if noninc[i] >= k and nondec[i] >= k]

class Solution(object):
	def goodIndices(self, nums, k):
		N = len(nums)

		noninc = [0 for _ in range(N)]
		l = 1
		for i in range(1, N):
			noninc[i] = l

			if nums[i] <= nums[i - 1]:
				l += 1
			else:
				l = 1 

		nondec = [0 for _ in range(N)]
		l = 1
		for i in range(N - 2, -1, -1):
			nondec[i] = l

			if nums[i] <= nums[i + 1]:
				l += 1
			else:
				l = 1 

		return [i for i in range(k, N - k) if noninc[i] >= k and nondec[i] >= k]
