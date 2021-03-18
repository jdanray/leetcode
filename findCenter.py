# https://leetcode.com/problems/find-center-of-star-graph/ 

class Solution(object):
	def findCenter(self, edges):
		return edges[1][0] if edges[1][0] in edges[0] else edges[1][1]
