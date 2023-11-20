# https://leetcode.com/problems/maximum-product-subarray/ 

"""
I visited the "Discuss" page for a different problem: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/discuss/?currentPage=1&orderBy=most_votes&query=

A post mentions that the current problem is similar: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/discuss/855105/Java-Simple-DP-beat-100

I was able to adapt the solution to the different problem to the current problem.
"""

class Solution(object):
	def maxProduct(self, nums):
		# mx is the product of the max product subarray ending at nums[i]
		# mn is the product of the min product subarray ending at nums[i]
		# res is the max product over all subarray products

		mx = mn = res = nums[0]
		for i in range(1, len(nums)):
			mx, mn = max(nums[i], nums[i] * mx, nums[i] * mn), min(nums[i], nums[i] * mx, nums[i] * mn)
			res = max(res, mx)

		return res
