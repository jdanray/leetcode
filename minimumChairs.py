# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/ 

class Solution(object):
	def minimumChairs(self, s):
		people = 0
		chairs = 0
		for c in s:
			if c == 'E':
				people += 1
			else:
				people -= 1

			if people > chairs:
				chairs += 1

		return chairs
