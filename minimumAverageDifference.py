# https://leetcode.com/problems/minimum-average-difference/ 

class Solution(object):
	def minimumAverageDifference(self, nums):
		N = len(nums)

		leftSum = 0
		rightSum = sum(nums)
		minDiff = float('inf')
		res = -1
		for i, n in enumerate(nums):
			leftSum += n
			leftAvg = leftSum / (i + 1)

			rightSum -= n
			if i == N - 1:
				rightAvg = 0
			else:
				rightAvg = rightSum / (N - i - 1)

			d = abs(leftAvg - rightAvg)
			if d < minDiff:
				minDiff = d
				res = i

		return res
