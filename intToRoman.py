# https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
	def intToRoman(self, num):
		unit = ['I', 'X', 'C', 'M']
		half = ['V', 'L', 'D']
		roman = ''
		place = 0
		while num > 0:
			digit = num % 10
            
			if digit == 9:
				roman = unit[place] + unit[place + 1] + roman
			elif digit < 4:
				roman = (unit[place] * digit) + roman
			elif digit == 4:
				roman = unit[place] + half[place] + roman
			elif digit > 4:
				roman = half[place] + (unit[place] * (digit - 5)) + roman

			place += 1
			num //= 10

		return roman

"""
After I solve a problem, I like to examine other people's solutions. I discovered an elegant solution here:

https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution

I wanted to preserve it. I translated it into Python:
""" 

class Solution(object):
	def intToRoman(self, num):
		M = ["", "M", "MM", "MMM"]
		C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
		X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
		I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
		return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
