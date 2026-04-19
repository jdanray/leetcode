# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution(object):
	def maxDistance(self, nums1, nums2):
		snums1 = sorted((n1, i) for (i, n1) in enumerate(nums1))
		snums2 = sorted([(n2, j) for (j, n2) in enumerate(nums2)], key=lambda x: (x[0], -x[1]))

		i = 0
		res = float('-inf')
		for (n2, j) in snums2:
			while i < len(snums1) and snums1[i][0] <= n2:
				if snums1[i][1] <= j:
					res = max(res, j - snums1[i][1])
				i += 1

		return res if res != float('-inf') else 0