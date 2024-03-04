# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/ 

from sortedcontainers import SortedList

class Solution(object):
	def resultArray(self, nums):
		def greaterCount(sl, n):
			return len(sl) - sl.bisect_right(n)

		arr1 = [nums[0]]
		arr2 = [nums[1]]
		sl1 = SortedList([nums[0]])
		sl2 = SortedList([nums[1]])
		for i in range(2, len(nums)):
			gc1 = greaterCount(sl1, nums[i])
			gc2 = greaterCount(sl2, nums[i])

			if gc1 > gc2:
				arr1.append(nums[i])
				sl1.add(nums[i])
			elif gc1 < gc2:
				arr2.append(nums[i])
				sl2.add(nums[i])
			elif len(arr1) > len(arr2):
				arr2.append(nums[i])
				sl2.add(nums[i])
			else:
				arr1.append(nums[i])
				sl1.add(nums[i])

		return arr1 + arr2
