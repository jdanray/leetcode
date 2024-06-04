# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/ 

class Solution(object):
	def clearStars(self, s):
		indexes = collections.defaultdict(list)
		removed = set()
		for i, c in enumerate(s):
			if c == '*':
				for a in string.ascii_lowercase:
					if indexes[a]:
						j = indexes[a].pop()
						removed.add(j)
						break
			else:
				indexes[c].append(i)

		return ''.join(c for i, c in enumerate(s) if c != '*' and i not in removed)

"""
After I solve a problem, I like to study other people's solutions. My solution is just like this one: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/discuss/5243492/O(N-*-26)-or-Simple-Greedy-Solution-or-C%2B%2B-or-Java-or-Python

But I like this solution better: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/discuss/5243342/Explained-with-thought-process-Using-min-heap-oror-Very-simple

One reason why I prefer it is that it is more general. My solution works on strings of lowercase letters. This solution works on sequences of elements that can be compared.

I implemented the solution in Python: 
"""

class Solution(object):
	def clearStars(self, s):
		pq = []
		heapq.heapify(pq)

		removed = set()
		for i, c in enumerate(s):
			if c == '*':
				_, j = heapq.heappop(pq)
				removed.add(-j)
			else:
				heapq.heappush(pq, (c, -i))

		return ''.join(c for i, c in enumerate(s) if c != '*' and i not in removed)
