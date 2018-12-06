# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
	def letterCombinations(self, digits, i=0, c=""):
		if not digits:
			return []

		phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
		stack = [[0, ""]]
		combos = []

		while stack:
			i, c = stack.pop()

			if i >= len(digits):
				combos = [c] + combos
				continue

			for l in phone[digits[i]]:
				stack.append([i + 1, c + l])

		return combos
