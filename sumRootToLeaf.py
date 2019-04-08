# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

class Solution(object):
	def sumRootToLeaf(self, root):
		s = 0
		stack = [[root, []]]
		while stack:
			node, num = stack.pop()

			num = [node.val] + num

			if not node.left and not node.right:
				p = 1
				for b in num:
					s += p * b
					p *= 2
                    
			if node.left:
				stack.append([node.left, num])
                
			if node.right:
				stack.append([node.right, num])

		return s
