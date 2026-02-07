# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/ 

class Solution(object):
	def minimumDeletions(self, s):
		a = s.count('a')
		b = 0
		res = float('inf')
		for c in s:
			if c == 'a':
				a -= 1

			res = min(res, a + b)

			if c == 'b':
				b += 1

		return res

"""
In November, 2020, I came upon the following two solutions. It is now February 6, 2026, and I came up with the above solution. The above solution is much cleaner. I thought of the idea for it immediately. It only took a few minutes to work out all of the implementation details.
"""

class Solution(object):
	def minimumDeletions(self, s):
		N = len(s)

		# number of b's to the left
		# number of a's to the right

		na = 0
		nb = 0
		left = [0 for _ in range(N)]
		right = [0 for _ in range(N)]
		for i in range(N):
			left[i] = nb
			right[N - 1 - i] = na

			if s[i] == 'b':
				nb += 1
			if s[N - 1 - i] == 'a':
				na += 1

		return min(left[i] + right[i] for i in range(N))

"""
After I solve problems, I like to examine other people's solutions.

The following is my Python implementation of a program written in Java. You can see the original program here: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/discuss/935374/2-Solutions-or-Easy-to-Understand-Code-with-Detailed-Steps-O(n)-Time-O(1)-Space

Both programs are based on similar ideas and run in O(n) time, but this program is O(1) space. The code also turns out to be simpler and prettier.
"""

class Solution(object):
	def minimumDeletions(self, s):
		N = len(s)

		acount = s.count('a')
		bcount = 0
		res = float('inf')
		for c in s:
			if c == 'b':
				res = min(res, acount + bcount)
				bcount += 1
			else:
				acount -= 1

		return min(res, acount + bcount)
