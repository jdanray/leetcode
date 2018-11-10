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
			elif digit >= 5:
				roman = half[place] + (unit[place] * (digit - 5)) + roman

			place += 1
			num //= 10

		return roman
