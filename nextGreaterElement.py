# https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
	def nextGreaterElement(self, nums1, nums2):
		stack = []
		greater = collections.defaultdict(lambda: -1)
		for n in nums2:
			while stack and stack[-1] < n:
				el = stack.pop()
				greater[el] = n
                
			stack.append(n)

		return [greater[n] for n in nums1]

class Solution(object):
	def nextGreaterElement(self, findNums, nums):
		res = []
		for f in findNums:
			i = 0
			while nums[i] != f:
				i += 1
			while i < len(nums) and nums[i] <= f:
				i += 1
			if i >= len(nums) or nums[i] <= f:
				res.append(-1)
			else:
				res.append(nums[i])
		return res
