# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution(object):
	def nextGreatestLetter(self, letters, target):
		if target >= letters[-1]:
			return letters[0]

		i = 0
		while target >= letters[i]:
			i += 1
		return letters[j]

class Solution(object):
	def nextGreatestLetter(self, letters, target):
		for l in letters:
			if l > target:
				return l
            
		return letters[0]

class Solution(object):
	def nextGreatestLetter(self, letters, target):
		def condition(value):
			return letters[value] > target

		left = 0
		right = len(letters)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return letters[left % len(letters)]
