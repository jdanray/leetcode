# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution(object):
	def increasingTriplet(self, nums):
		smallest = sys.maxsize
		second_smallest = sys.maxsize
		print(smallest)
		for n in nums:
			if smallest >= n:
				smallest = n
			elif second_smallest >= n:
				second_smallest = n
			else:
				return True
		return False
