# https://leetcode.com/problems/permutations-ii/

class Solution(object):
	def permuteUnique(self, nums):
		def allperms(used, p):
			if len(p) == len(nums):
				return [p]

			perms = []
			for i, n in enumerate(nums):
				if (used >> i) & 1 == 0:
					perms += allperms(used ^ (1 << i), p + [n])

			return perms

		perms = allperms(0, [])
		perms = {tuple(p) for p in perms}
		perms = [list(p) for p in perms]

		return perms

"""
After I solve a problem, I like to study other people's solutions.
The following is my translation into Python of the following Java program:

https://leetcode.com/problems/permutations-ii/discuss/18594/Really-easy-Java-solution-much-easier-than-the-solutions-with-very-high-vote
"""

class Solution(object):
	def permuteUnique(self, nums):
		def allperms(used, p):
			if len(p) == len(nums):
				return [p]

			perms = []
			for i, n in enumerate(nums):
				if (used >> i) & 1 == 1:
					continue

				if i > 0 and nums[i - 1] == nums[i] and (used >> (i - 1)) & 1 == 0:
					continue

				perms += allperms(used ^ (1 << i), p + [n])

			return perms

		nums = sorted(nums)
		return allperms(0, [])
