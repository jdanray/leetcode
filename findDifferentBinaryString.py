# https://leetcode.com/problems/find-unique-binary-string/

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
