# https://leetcode.com/problems/construct-string-with-repeat-limit/ 

class Solution(object):
	def repeatLimitedString(self, s, repeatLimit):
		cands = sorted(string.ascii_lowercase, reverse=True)
		count = collections.Counter(s)
		prev = ['', 0]
		res = ''
		building = True
		while building:
			building = False
			for c in cands:
				if count[c] > 0 and (prev[0] != c or prev[1] < repeatLimit):
					building = True
					res += c
					count[c] -= 1
                    
					if prev[0] == c:
						prev[1] += 1
					else:
						prev = [c, 1]

					break

		return res
