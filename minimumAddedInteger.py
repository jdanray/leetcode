# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution(object):
	def minimumAddedInteger(self, nums1, nums2):
		left = -1000
		right = 1000

		count1 = collections.Counter(nums1)
		count2 = collections.Counter(nums2)

		for x in range(left, right + 1):
			hits = 0
			for n in count1:
				hits += min(count1[n], count2[n + x])

			if hits == len(nums2):
				return x