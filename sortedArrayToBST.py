# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution:
	def sortedArrayToBST(self, nums):
		if not nums:
			return None

		m = len(nums) // 2
		root = TreeNode(nums[m])
		root.left = TreeNode(nums[:m])
		root.right = TreeNode(nums[m + 1:])
		return root
