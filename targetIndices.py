# https://leetcode.com/problems/find-target-indices-after-sorting-array/ 

# regular sort
# Time: O(n*log(n))
# Space: O(1)
class Solution(object):
	def targetIndices(self, nums, target):
		return [i for i, n in enumerate(sorted(nums)) if n == target]

# count sort
# Time: O(n)
# Space: O(n)
class Solution(object):
	def targetIndices(self, nums, target):
		count = collections.Counter(nums)
		idx = 0
		for n in range(target):
			while count[n] > 0:
				count[n] -= 1
				idx += 1

		return list(range(idx, idx + count[target]))

# count sort
# Time: O(n)
# Space: O(1)
# Idea from: https://leetcode.com/problems/find-target-indices-after-sorting-array/discuss/1599800/C%2B%2B-O(N)-Time-Counting-Sort 
class Solution(object):
	def targetIndices(self, nums, target):
		eq = 0
		lt = 0
		for n in nums:
			if n == target:
				eq += 1
			elif n < target:
				lt += 1

		return [lt + i for i in range(eq)]
