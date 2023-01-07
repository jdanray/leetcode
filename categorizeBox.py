# https://leetcode.com/problems/categorize-box-according-to-criteria/ 

class Solution(object):
	def categorizeBox(self, length, width, height, mass):
		B = 10**4
		V = 10**9
		H = 100

		bulky = False
		heavy = False

		if (length >= B or width >= B or height >= B or mass >= B) or (length * width * height) >= V:
			bulky = True

		if mass >= H:
			heavy = True

		if bulky and heavy:
			return "Both"
		elif bulky:
			return "Bulky"
		elif heavy:
			return "Heavy"
		else:
			return "Neither"
