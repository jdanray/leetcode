# https://leetcode.com/problems/reformat-phone-number/

class Solution(object):
	def reformatNumber(self, number):
		digits = ''.join(num for num in number if num.isdigit())
		N = len(digits)
        
		i = 0
		blocks = []
		while N - i > 4:
			blocks += [digits[i] + digits[i + 1] + digits[i + 2]]
			i += 3

		if N - i == 4:
			blocks += [digits[i] + digits[i + 1]] + [digits[i + 2] + digits[i + 3]]
		else:
			blocks += [digits[i:N]]

		return '-'.join(blocks)
