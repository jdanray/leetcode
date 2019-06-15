# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

class Solution(object):
	def constructFromPrePost(self, pre, post):
		def construct(i, j, k, l):
			if i > j:
				return None
			elif i == j:
				return TreeNode(pre[i])

			lnew = k
			while lnew <= l and post[lnew] != pre[i + 1]:
				lnew += 1
	
			jnew = (i + 1) + (lnew  - k)

			node = TreeNode(pre[i])
			node.left = construct(i + 1, jnew, k, lnew)
			node.right = construct(jnew + 1, j, lnew + 1, l - 1) 

			return node

		return construct(0, len(pre) - 1, 0, len(post) - 1)
