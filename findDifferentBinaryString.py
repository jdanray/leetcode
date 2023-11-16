# https://leetcode.com/problems/find-unique-binary-string/

"""
My old solution used a brute-force approach. I realized that diagonalization can solve this problem.

The idea is very simple: For each nums[i], res can't be the same as nums[i], because res differs from nums[i] at the i-th index.

In other terms: For all 0 <= i < n, res != nums[i], because res[i] != nums[i][i]. Therefore, res isn't in nums.
"""

class Solution(object):
	def findDifferentBinaryString(self, nums):
		return ''.join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))

class Solution(object):
	def findDifferentBinaryString(self, nums):
		res = ''
		for i in range(len(nums)):
			if nums[i][i] == '0':
				res += '1'
			else:
				res += '0'
		return res

class Solution(object):
	def findDifferentBinaryString(self, nums):
		N = len(nums)
		nums = set(nums)

		def genString(s):
			if len(s) >= N:
				if s not in nums:
					return s
				else:
					return False

			return genString(s + '1') or genString(s + '0')

		return genString('') 
