# https://leetcode.com/problems/unique-number-of-occurrences/ 

class Solution(object):
	def uniqueOccurrences(self, arr):
		count = collections.Counter(arr)
		return len(set(count.values())) == len(count.values())

