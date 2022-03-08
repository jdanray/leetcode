# https://leetcode.com/problems/create-binary-tree-from-descriptions/ 

class Solution(object):
	def createBinaryTree(self, descriptions):
		noParent = {}
		graph = {}
		for (parent, child, isLeft) in descriptions:
			if parent not in graph:
				graph[parent] = [None, None]

			graph[parent][not isLeft] = child
			noParent[child] = False
			if parent not in noParent:
				noParent[parent] = True

		root = -1
		for node in noParent:
			if noParent[node]:
				root = node
				break

		def build(val):
			if val == None:
				return None

			node = TreeNode(val)
			if val in graph:
				node.left = build(graph[val][0])
				node.right = build(graph[val][1])
			return node

		return build(root)
