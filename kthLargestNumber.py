# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/ 

class Solution(object):
	def kthLargestNumber(self, nums, k):
		nums = sorted(int(n) for n in nums)
		return str(nums[-k])

"""
After I solve a problem, I like to examine other people's solutions. I found the following solution. It is a little simpler than mine:

https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/discuss/1431849/Python-3-One-Liner
"""

class Solution(object):
	def kthLargestNumber(self, nums, k):
		return sorted(nums, key=int)[-k]
