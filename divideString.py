# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/ 

class Solution(object):
	def divideString(self, s, k, fill):
		res = [s[i:i + k] for i in range(0, len(s), k)]
		res[-1] += fill * (k - len(res[-1]))
		return res
