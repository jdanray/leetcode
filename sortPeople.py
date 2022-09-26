# https://leetcode.com/problems/sort-the-people/

class Solution(object):
	def sortPeople(self, names, heights):
		indexes = sorted(list(range(len(names))), key=lambda i: heights[i], reverse=True)
		return [names[i] for i in indexes]
