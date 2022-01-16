# https://leetcode.com/problems/capitalize-the-title/ 

class Solution(object):
	def capitalizeTitle(self, title):
		title = "".join(c.lower() for c in title)
		title = " ".join(word.capitalize() if len(word) > 2 else word for word in title.split())
		return title
