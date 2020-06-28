# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

class Solution:
	def findTarget(self, root, k):
		values = []
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				stack.append(node.left)
				stack.append(node.right)
				values.append(node.val)

		for i in range(len(values)):
			for j in range(i + 1, len(values)):
				if values[i] + values[j] == k:
					return True

		return False

class Solution(object):
	def findTarget(self, root, k):
		seen = set()
		stack = [root]
		while stack:
			node = stack.pop()

			if not node:
				continue

			if k - node.val in seen:
				return True

			seen.add(node.val)
			stack.append(node.left)
			stack.append(node.right)

		return False	

class Solution(object):
	def findTarget(self, root, k):
		nums = []
		def inorder(node):
			if node:
				inorder(node.left)
				nums.append(node.val)
				inorder(node.right)

		inorder(root)
		i = 0
		j = len(nums) - 1
		while i < j and nums[i] + nums[j] != k:
			if nums[i] + nums[j] > k:
				j -= 1
			else:
				i += 1

		return i != j and nums[i] + nums[j] == k
