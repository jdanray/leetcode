# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution(object):
	def numSmallerByFrequency(self, queries, words):
		def freq(s):
			s = sorted(s)
			f = 0
			i = 0
			while i < len(s) and s[i] == s[0]:
				f += 1
				i += 1
			return f

		fqueries = [freq(q) for q in queries]
		fwords = [freq(w) for w in words]
		return [sum(fq < fw for fw in fwords) for fq in fqueries]

"""
In the above solution, freq(s) has O(|s| * log(|s|)) time-complexity. In the following solution, freq(s) has O(|s|) time-complexity (and O(|s|) space-complexity). 

Each solution has an overall time-complexity of O(|queries| * |words|).
"""

class Solution(object):
	def numSmallerByFrequency(self, queries, words):
		def freq(s):
			count = collections.Counter(s)
			for c in string.ascii_lowercase:
				if c in count:
					return count[c]

		fqueries = [freq(q) for q in queries]
		fwords = [freq(w) for w in words]
		return [sum(fq < fw for fw in fwords) for fq in fqueries]

"""
Here's an even simpler way to compute freq(s):

def freq(s):
	return s.count(min(s))

If we want to expand that, we can write:

def freq(s):
	m = s[0]	# precondition: len(s) >= 1
	for c in s: 
		m = min(m, c)
	return sum(c == m for c in s)

This method has O(|s|) time-complexity and O(1) space-complexity. 

I got the idea from: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/discuss/366367/Extremely-Short-Python-Solution

After I solve a problem, I like to study other people's solutions to the same problem. In this particular case, I am especially glad that I have that habit. Not only did I discover a simpler, more efficient way to compute freq(s), I also discovered a more efficient way to solve the overall problem:

For each w in words, compute freq(w) and store it in the list fwords. Sort fwords. Now, for each q in queries, compute freq(q) and binary search fwords for the right results.

I got the idea from: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/discuss/366353/java-binary-search
"""

class Solution(object):
	def numSmallerByFrequency(self, queries, words):
		def freq(s):
			return s.count(min(s))

		fwords = sorted(freq(w) for w in words)
		res = []
		for q in queries:
			fq = freq(q)
			lo = 0
			hi = len(fwords) - 1
			while lo <= hi:
				mid = lo + (hi - lo) // 2
				if fwords[mid] <= fq:
					lo = mid + 1
				else:
					hi = mid - 1
			res.append(len(fwords) - lo)
		return res
