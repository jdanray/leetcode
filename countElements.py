# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/ 

class Solution(object):
	def countElements(self, nums):
		N = len(nums)
		nums = sorted(nums)
		
		i = 0
		while i < N and nums[i] == nums[0]:
			i += 1

		j = N - 1
		while j >= 0 and nums[j] == nums[N - 1]:
			j -= 1

		return max(0, j - i + 1)

"""
After I solve a problem, I like to study other people's solutions.

I found a faster solution here: https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/discuss/1711240/Java-Simple-solution-of-finding-min-and-max

That solution is linear time, while my solution is linearithmic. I realize that the sort in my program is unnecessary. All I really use is the maximum and minimum elements.

Here is my Python translation of the Java program:
"""

class Solution(object):
	def countElements(self, nums):
		return len([n for n in nums if min(nums) < n < max(nums)])
