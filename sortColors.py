# https://leetcode.com/problems/sort-colors/ 

# dutch national flag problem
class Solution(object):
	def sortColors(self, nums):
		lo = 0
		mid = 0
		hi = len(nums) - 1
		while mid <= hi:
			if nums[mid] == 0:
				nums[mid], nums[lo] = nums[lo], nums[mid]
				lo += 1
				mid += 1
			elif nums[mid] == 1:
				mid += 1
			elif nums[mid] == 2:
				nums[mid], nums[hi] = nums[hi], nums[mid]
				hi -= 1

# dutch national flag problem
class Solution:
	def sortColors(self, nums):
		mid = 1
		i = 0
		j = 0
		n = len(nums) - 1
		while j <= n:
			if nums[j] < mid:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
				j += 1
			elif nums[j] > mid:
				nums[j], nums[n] = nums[n], nums[j]
				n -= 1
			else:
				j += 1

# a count sort
class Solution:
	def sortColors(self, nums):
		c = [0, 0, 0]
		for n in nums: c[n] += 1
		i = 0
		j = 0
		while j < len(c):
			while c[j] > 0:
				c[j] -= 1
				nums[i] = j
				i += 1
			j += 1
