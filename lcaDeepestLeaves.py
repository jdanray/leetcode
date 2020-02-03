# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/ 

class Solution(object):
	def lcaDeepestLeaves(self, root):
		deepest = 0
		dleaves = set()
		dlpath = dict()
		stack = [[root, 0, set()]]
		while stack:
			node, depth, path = stack.pop()

			if not node:
				continue

			newpath = path | {(depth, node)}

			if not node.left and not node.right:
				if depth > deepest:
					dleaves = set()
					deepest = depth
                    
				if depth == deepest:
					dleaves.add(node.val)
					dlpath[node.val] = newpath
			else:
				stack.append([node.left, depth + 1, newpath])
				stack.append([node.right, depth + 1, newpath])

		common = set.intersection(*list(dlpath[leaf] for leaf in dleaves))
		_, lca = max(common)
        
		return lca

"""
After I solve a problem, I like to examine other people's solutions. In this case, I particularly liked the ideas featured here:

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution

Here is my implementation of one of the programs:
"""

class Solution(object):
	def lcaDeepestLeaves(self, root):
		def helper(root):
			if not root:
				return [0, None]

			depthl, lcal = helper(root.left)
			depthr, lcar = helper(root.right)

			if depthl > depthr:
				return [depthl + 1, lcal]
			elif depthl < depthr:
				return [depthr + 1, lcar]
			else:
				return [depthl + 1, root]

		return helper(root)[1]
