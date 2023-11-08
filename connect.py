# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Solution(object):
	def connect(self, root):
		queue = [root]
		while queue:
			prev = None
			for _ in range(len(queue)):
				node = queue.pop(0)

				if not node:
					continue

				if prev != None:
					prev.right = node

				prev = node
				queue.append(node.left)
				queue.append(node.right)

		return root

class Solution(object):
	def connect(self, root):
		front = None
		curlvl = 0
		queue = [[0, root]]
		while queue:
			lvl, node = queue.pop(0)
			
			if not node:
				continue

			if lvl > curlvl:
				curlvl = lvl
				front = None

			if front:
				front.next = node

			front = node

			queue.append([lvl + 1, node.left])
			queue.append([lvl + 1, node.right])

		return root
