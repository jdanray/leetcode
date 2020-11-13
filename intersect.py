# https://leetcode.com/problems/intersection-of-two-arrays-ii/ 

class Solution(object):
	def intersect(self, nums1, nums2):
		N = len(nums1)
		M = len(nums2)

		nums1 = sorted(nums1)
		nums2 = sorted(nums2)

		i = 0
		j = 0
		res  = []
		while i < N and j < M:
			if nums1[i] < nums2[j]:
				i += 1
			elif nums1[i] > nums2[j]:
				j += 1
			else:
				res.append(nums1[i])
				i += 1
				j += 1

		return res

class Solution:
	def intersect(self, nums1, nums2):
		res = []
		count1 = collections.Counter(nums1)
		for n in nums2:
			if count1[n] > 0:
				res.append(n)
				count1[n] -= 1

		return res
