# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/ 

class Solution(object):
	def mergeArrays(self, nums1, nums2):
		M = 1000

		sums = collections.defaultdict(int)

		for (i, v) in nums1:
			sums[i] += v

		for (i, v) in nums2:
			sums[i] += v

		return [[i, sums[i]] for i in range(1, M + 1) if sums[i] > 0]

class Solution(object):
	def mergeArrays(self, nums1, nums2):
		M = len(nums1)
		N = len(nums2)

		i = 0
		j = 0
		res = []
		while i < M or j < N:
			while i < M and j < N and nums1[i][0] < nums2[j][0]:
				res.append(nums1[i])
				i += 1

			while i < M and j < N and nums2[j][0] < nums1[i][0]:
				res.append(nums2[j])
				j += 1

			while i < M and j < N and nums1[i][0] == nums2[j][0]:
				res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
				i += 1
				j += 1

			while i < M and j >= N:
				res.append(nums1[i])
				i += 1

			while i >= M and j < N:
				res.append(nums2[j])
				j += 1

		return res
