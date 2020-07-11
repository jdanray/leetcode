# https://leetcode.com/problems/reformat-date/

class Solution(object):
	def reformatDate(self, date):
		dy, mo, yr = date.split()

		dy = dy[:-2]
		if len(dy) < 2:
			dy = '0' + dy

		months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		mon2num = {m: '0' + str(i + 1) if i < 9 else str(i + 1) for i, m in enumerate(months)}
		mo = mon2num[mo]

		return yr + '-' + mo + '-' + dy
