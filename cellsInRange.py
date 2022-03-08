# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/ 

class Solution(object):
	def cellsInRange(self, s):
		alphabet = string.ascii_uppercase
        
		c1, r1, c2, r2 = s[0], s[1], s[3], s[4]
        
		cols = alphabet[alphabet.find(c1):alphabet.find(c2) + 1]
		rows = "".join(str(r) for r in range(int(r1), int(r2) + 1))
        
		return [c + r for c in cols for r in rows]

"""
After I solve a problem, I like to see other people's solutions. I found a simpler solution here:

https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/discuss/1823744/Two-Loops

Here is the code:
"""

class Solution:
	def cellsInRange(self, s):
		return [chr(c) + chr(r) for c in range(ord(s[0]), ord(s[3]) + 1) for r in range(ord(s[1]), ord(s[4]) + 1)]
