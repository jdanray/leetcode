# https://leetcode.com/problems/most-frequent-even-element/ 

class Solution(object):
	def mostFrequentEven(self, nums):
		count = collections.Counter([n for n in nums if n % 2 == 0])
		mostFreq = [n for n in count if count[n] == max(count.values())]
		return min(mostFreq) if mostFreq else -1
