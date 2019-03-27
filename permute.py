# https://leetcode.com/problems/permutations/

class Solution:
	def permute(self, nums):
		if not nums:
			return []

		perms = []
		stack = [[[], 0]]
		while stack:
			p, used = stack.pop()
			
			if len(p) >= len(nums):
				perms.append(p)

			for i, n in enumerate(nums):
				if used & (1 << i) == 0:
					stack.append([p + [n], used | (1 << i)])

		return perms
