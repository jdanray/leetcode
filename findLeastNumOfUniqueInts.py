# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/ 

class Solution(object):
	def findLeastNumOfUniqueInts(self, arr, k):
		count = collections.Counter(arr)
		nums = sorted(count.keys(), key=lambda n: count[n])
		i = 0
		while i < len(nums) and k > 0:
			if count[nums[i]] > 0:
				count[nums[i]] -= 1
				k -= 1
			else:
				i += 1

		return len([n for n in nums if count[n] > 0])
