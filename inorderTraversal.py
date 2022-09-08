# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution(object):
	def inorderTraversal(self, root):
		if not root:
			return []
		else:
			return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

class Solution(object):
	def inorderTraversal(self, root):
		stack = []
		crawl = root
		while crawl:
			stack.append(crawl)
			crawl = crawl.left

		res = []
		while stack:
			crawl = stack.pop()
			res.append(crawl.val)

			if crawl.right:
				crawl = crawl.right
				while crawl:
					stack.append(crawl)
					crawl = crawl.left

		return res
