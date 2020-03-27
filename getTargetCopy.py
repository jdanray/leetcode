# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

class Solution(object):
	def getTargetCopy(self, original, cloned, target):
		count = 0
		queue = [original]
		while queue:
			node = queue.pop(0)
			if not node:
				continue

			count += 1
			if node == target:
				break

			queue.append(node.left)
			queue.append(node.right)

		n =  0
		queue = [cloned]
		while queue:
			node = queue.pop(0)
			if not node:
				continue

			n += 1
			if n == count:
				return node

			queue.append(node.left)
			queue.append(node.right)

"""
After I solve a problem, I like to examine other people's solutions to the same problem. In this case, I came across the following Java solution:

https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/discuss/537728/Java-Simple-Solution

I translated that Java solution into Python:
"""

class Solution(object):
	def getTargetCopy(self, original, cloned, target):
		if not original or original == target:
			return cloned
        
		return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
