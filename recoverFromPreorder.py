# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/ 

class Solution(object):
	def recoverFromPreorder(self, S):
		def build(S):
			if not S:
				return None

			i = 0
			headval = ''
			while i < len(S) and S[i] != '-':
				headval += S[i]
				i += 1

			headval = int(headval)
			headnode = TreeNode(headnode)

			leftdepth = 0
			while i < len(S) and S[i] == '-':
				i += 1
				leftdepth += 1

			j = i
			depth = 0
			while j < len(S):
				if S[j] == '-':
					depth += 1
				elif depth == leftdepth:
					break
				else:
					depth = 0
				j += 1

			headnode.left = build(S[i:j])
			headnode.right = build(S[j:])
			return headnode

		return build(S) 
