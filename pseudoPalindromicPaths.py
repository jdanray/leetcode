# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

class Solution(object):
	def pseudoPalindromicPaths(self, root):
		# Let p be a path.
		# n is the number of nodes in p.
		# If n is even, there must be 0 digits that occur an odd number of times for p to be pseudo-palindromic
		# If n is odd, there must be 1 digit that occurs an odd number of times
		# parity[d] is the parity of the number of times that digit d has occurred in p
		# odd is the number of occurrences that are odd
		# res is the number of pseudo-palindromic paths
		# The loop body maintains these invariants

		res = 0
		stack = [[root, 0, 0, 0]]
		while stack:
			node, n, parity, odd = stack.pop()

			if not node:
				continue 

			n += 1

			parity ^= (1 << node.val)

			if (parity >> node.val) & 1 == 0:
				odd -= 1
			else:
				odd += 1

			if not node.left and not node.right and n % 2 == 0 and odd == 0:
				res += 1
			elif not node.left and not node.right and n % 2 == 1 and odd == 1:
				res += 1

			stack.append([node.left, n, parity, odd])
			stack.append([node.right, n, parity, odd])

		return res

"""
After I solve a problem, I like to examine other people's solutions.

There is a simpler way to think about this problem:

>To check if any permutaion of numbers can make a palindrome all we need to do is check if we have even count of all numbers and at max one odd count (for odd palindromes with a center with single number). eg: 121.

>We can easily do this by using a bit vector to store the parity of the counts of numbers (even or odd).

>All we need to do now is maintain this bit vector while traversing down the tree in a dfs fashion and check at leaf nodes if we can create a palindrome.

Source: 
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/648304/C%2B%2B-DFS-%2B-Bitvector

I translate their solution into Python. In this program, I maintain the number of digits that occur an odd number of times.
"""

class Solution(object):
	def pseudoPalindromicPaths(self, root):
		def dfs(root, parity, odd):
			if not root:
				return 0

			parity ^= (1 << root.val)
			if (parity >> root.val) & 1 == 0:
				odd -= 1
			else:
				odd += 1

			if not root.left and not root.right and odd <= 1:
				return 1
			else:
				return dfs(root.left, parity, odd) + dfs(root.right, parity, odd)

		return dfs(root, 0, 0)
