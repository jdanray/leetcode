# https://leetcode.com/problems/greatest-common-divisor-of-strings/

"""
Definitions:

T divides S iff S = T*

Preconditions:

str1 and str2 are strings

Postconditions:

X is the largest string that divides both str1 and str2

Thoughts:

X divides str1. So, str1 = X*.
X divides str2. So, str2 = X*.

If X divides str1, then str1 = X or str1 = X*n.

When in doubt, use brute-force. --Ken Thompson

Find all strings that divide str1
Find all strings that divide str2
Take their intersection
Return the largest element the intersection

Construct a general way to find all "dividing strings", all "dividers". Apply it to str1 and to str2. Like cases invite like treatment. So, execute one and the same method in both cases.
"""

class Solution:
	def dividers(self, string):
		divs = set()
		s = ""
		for i, c in enumerate(string):
			s += c
			if s * (len(string) // (i + 1)) == string:
				divs.add(s)
		return divs

	def gcdOfStrings(self, str1, str2):
		div1 = self.dividers(str1) 
		div2 = self.dividers(str2)
		same = div1 & div2
		return max(same, key=len) if same else ""

# Simpler solution

class Solution(object):
	def gcdOfStrings(self, str1, str2):
		def divides(t, s):
			return t * (len(s) // len(t)) == s

		t = ''
		res = ''
		for c in str1:
			t += c
			if divides(t, str1) and divides(t, str2):
				res = t

		return res
