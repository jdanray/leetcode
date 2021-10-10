# https://leetcode.com/problems/two-out-of-three/ 

class Solution(object):
	def twoOutOfThree(self, nums1, nums2, nums3):
		count = collections.Counter()

		def countNums(nums):
			for n in set(nums):
				count[n] += 1

		countNums(nums1)
		countNums(nums2)
		countNums(nums3)

		return [n for n in count if count[n] >= 2]
