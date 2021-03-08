# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/ 

class Solution(object):
	def minElements(self, nums, limit, goal):
		d = abs(goal - sum(nums))
		return d // limit + (d % limit != 0)
