# https://leetcode.com/problems/merge-two-binary-trees/description/

class Solution:
	def mergeTrees(self, t1, t2):
		if not t1:
			return t2
		elif not t2:
			return t1
		root = t1
		queue = [(t1, t2)]
		while queue:
			t1, t2 = queue.pop(0)

			if t1.left and t2.left:
				queue.append((t1.left, t2.left))
			elif not t1.left:
				t1.left = t2.left
			if t1.right and t2.right:
				queue.append((t1.right, t2.right))
			elif not t1.right:
				t1.right = t2.right
			t1.val = t1.val + t2.val
		return root
