# https://leetcode.com/problems/even-odd-tree/ 

class Solution(object):
	def isEvenOddTree(self, root):
		par = 0
		queue = [root]
		while queue:
			prev = None
			for _ in range(len(queue)):
				u = queue.pop(0)

				if u.val % 2 == par:
					return False 
				elif prev != None and par == 0 and u.val <= prev.val:
					return False
				elif prev != None and par == 1 and u.val >= prev.val:
					return False

				prev = u
				if u.left: queue.append(u.left)
				if u.right: queue.append(u.right)

			par = 1 - par

		return True

class Solution(object):
	def isEvenOddTree(self, root):
		prevnode = None
		level = -1
		queue = [[root, 0]]
		while queue:
			node, curlvl = queue.pop(0)

			if not node:
				continue

			if curlvl % 2 == node.val % 2:
				return False

			if level == curlvl:
				if level % 2 == 0 and node.val <= prevnode.val:
					return False
				elif level % 2 == 1 and node.val >= prevnode.val:
					return False

			level = curlvl
			prevnode = node

			queue.append([node.left, curlvl + 1])
			queue.append([node.right, curlvl + 1])

		return True
