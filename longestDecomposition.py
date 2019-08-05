# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution(object):
	def longestDecomposition(self, text):
		def helper(start, end):
			if start == end:
				return 1
			elif start > end:
				return 0

			i = start
			j = end
			head = ''
			tail = ''
			while i < j:
				head += text[i]
				tail = text[j] + tail
				if text[i] == text[end] and head == tail:
					return 2 + helper(i + 1, j - 1)
				i += 1
				j -= 1
			return 1

		return helper(0, len(text) - 1)
