# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution(object):
	def trimMean(self, arr):
		P = 0.05

		r = int(len(arr) * P)
		arr = sorted(arr)
		arr = arr[r:-r]
        
		mean = 1.0 * sum(arr) / len(arr)
		return  mean
