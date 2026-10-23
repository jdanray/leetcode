# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution(object):
	def takeCharacters(self, s, k):
		CHARS = 'abc'

		count = collections.Counter(s)
		if any(count[c] < k for c in CHARS):
			return -1

		def condition(value):
			lcount = collections.Counter()
			for i in range(value):
				lcount[s[i]] += 1

			if all(lcount[c] >= k for c in CHARS):
				return True

			rcount = collections.Counter()
			for i in range(value - 1, -1, -1):
				lcount[s[i]] -= 1

				j = len(s) - (value - 1 - i) - 1
				rcount[s[j]] += 1

				if all(lcount[c] + rcount[c] >= k for c in CHARS):
					return True

			return False

		left = 0
		right = len(s)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left