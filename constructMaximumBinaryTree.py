# https://leetcode.com/problems/maximum-binary-tree/description/

class Solution:
	def constructMaximumBinaryTree(self, nums):
		if not nums:
			return None
		m = max(range(len(nums)), key=lambda i: nums[i])
		root = TreeNode(nums[m])
		root.left = self.constructMaximumBinaryTree(nums[:m])
		root.right = self.constructMaximumBinaryTree(nums[m + 1:])
		return root
