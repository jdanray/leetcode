# https://leetcode.com/problems/sequential-digits/ 

class Solution(object):
	def sequentialDigits(self, low, high):
		res = []
		while low <= high:
			num = str(low)
			newlow = str(int(num[0]) + 1)
			for _ in range(1, len(num)):
				newlow += "0"

			digs = num[0]
			for _ in range(1, len(num)):
				d = int(digs[-1]) + 1
				if d > 9:
					digs = ""
					break
				else:
					digs += str(d)

			if digs:
				digs = int(digs)
				if low <= digs <= high:
					res.append(digs)

			low = int(newlow)

		return res
