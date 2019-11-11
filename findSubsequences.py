# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ 

class Solution(object):
	def findSubsequences(self, nums):
		def helper(i):
			if i >= len(nums):
				return [[]]

			res = helper(i + 1)
			return res + [[nums[i]] + r for r in res if not r or r[0] >= nums[i]]

		return list(set(tuple(r) for r in helper(0) if len(r) >= 2))
