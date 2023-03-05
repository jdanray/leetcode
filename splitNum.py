# https://leetcode.com/problems/split-with-minimum-sum/ 

class Solution(object):
	def splitNum(self, num):
		digs = []
		while num > 0:
			digs.append(num % 10)
			num //= 10

		digs = sorted(digs)
		nums = [0, 0]
		for i, d in enumerate(digs):
			nums[i % 2] *= 10
			nums[i % 2] += d

		return sum(nums)

# count-sort implementation
class Solution(object):
	def splitNum(self, num):
		count = collections.Counter()
		while num > 0:
			count[num % 10] += 1
			num //= 10

		i = 0
		nums = [0, 0]
		for d in range(10):
			while count[d] > 0:
				nums[i] *= 10
				nums[i] += d
				i = 1 - i
				count[d] -= 1

		return sum(nums)
