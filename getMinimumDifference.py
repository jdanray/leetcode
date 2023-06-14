# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class Solution(object):
	def getMinimumDifference(self, root):
		nums = []
		stack = [root]
		while stack:
			node = stack.pop()

			if not node: 
				continue

			nums.append(node.val)

			stack.append(node.left)
			stack.append(node.right)

		nums = sorted(nums)
		res = float('inf')
		for i in range(1, len(nums)):
			res = min(res, nums[i] - nums[i - 1])

		return res

class Solution(object):
	def getMinimumDifference(self, root):
		def inOrder(root):
			return inOrder(root.left) + [root.val] + inOrder(root.right) if root else []

		nums = inOrder(root)
		res = float('inf')
		for i in range(1, len(nums)):
			res = min(res, nums[i] - nums[i - 1])

		return res

class Solution(object):
	def getMinimumDifference(self, root):
		self.res = float('inf')

		def inOrder(root):
			if not root:
				return []

			left = inOrder(root.left)
			right = inOrder(root.right)

			if left:
				self.res = min(self.res, root.val - left[-1]) 

			if right:
				self.res = min(self.res, right[0] - root.val)

			return left + [root.val] + right

		inOrder(root)
		return self.res

class Solution(object):
	def getMinimumDifference(self, root):
		self.prev = None
		self.res = float('inf')
        
		def inOrder(root):
			if not root:
				return

			inOrder(root.left)

			if self.prev:
				self.res = min(self.res, root.val - self.prev.val)

			self.prev = root

			inOrder(root.right)

		inOrder(root)
		return self.res
