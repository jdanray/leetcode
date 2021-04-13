# https://leetcode.com/problems/short-encoding-of-words/ 

class Solution(object):
	def minimumLengthEncoding(self, words):
		tail = -1
		seen = {}
		words = sorted(words, key=len, reverse=True)
		for w in words:
			if w in seen:
				idx = seen[w]
			else:
				idx = tail + 1

			idx += len(w)
			tail = max(tail, idx)

			chars = ""
			for c in w[::-1]:
				chars = c + chars
				if chars not in seen:
					seen[chars] = idx - 1
				idx -= 1

		print(len(seen))
		return tail + 1
