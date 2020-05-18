# https://leetcode.com/problems/count-binary-substrings/

class Solution(object):
	def countBinarySubstrings(self, s):
		s = [int(b) for b in s]
		count = [0, 0]
		res = 0
		for i, b in enumerate(s):
			if i - 1 >= 0 and s[i - 1] == b:
				count[b] += 1
			else:
				count[b] = 1
                   
			if count[b] <= count[1 - b]: 
				res += 1                    

		return res
