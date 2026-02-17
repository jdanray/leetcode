# https://leetcode.com/problems/first-element-with-unique-frequency/

class Solution(object):
	def firstUniqueFreq(self, nums):
		# fr[n] is the number of times that n occurs in nums
		# frFreqs[fr] is the number of times that the frequency fr occurs
		# If frFreq[fr] == 1, the frequency of fr is unique

		fr = collections.Counter(nums) 
		frFreqs = collections.Counter(fr.values())
		for n in nums:
			if frFreqs[fr[n]] == 1:
				return n
		return -1