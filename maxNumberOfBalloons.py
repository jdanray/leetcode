# https://leetcode.com//problems/maximum-number-of-balloons/ 

"""
You can see a progression in the code. 

The first program is terrible. The second program is better. The third program is nice and simple.
"""

class Solution(object):
	def maxNumberOfBalloons(self, text):
		target = "balloon"
		count = collections.Counter(text)
		res = 0
		while True:
			for t in target:		# if target == '', then the loop won't terminate
				if count[t] > 0:
					count[t] -= 1
				else:
					return res
			res += 1

class Solution(object):
	def maxNumberOfBalloons(self, text):
		target = "balloon"
		freq = collections.Counter(target)
		count = collections.Counter(text)
		res = float('inf')
		for t in target:
			res = min(res, count[t] / freq[t])
		return 0 if res == float('inf') else res

class Solution(object):
	def maxNumberOfBalloons(self, text):
		target = "balloon"
		freq = collections.Counter(target)
		count = collections.Counter(text)
		return min(count[t] / freq[t] for t in target)
