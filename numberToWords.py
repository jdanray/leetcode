# https://leetcode.com/problems/integer-to-english-words/

class Solution(object):
	def numberToWords(self, num):
		if num == 0:
			return "Zero"
			
		ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
		teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
		decs = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
		thousands = ['Thousand', 'Million', 'Billion']
		
		thous = -1
		english = []
		while num > 0:
			add = []
			place = 0
			digits = num % 1000
			
			tens_place = digits % 100
			if tens_place >= 10 and tens_place <= 19:
				add = [teens[digits % 10]] + add
				place = 2
				digits //= 100
				
			while digits > 0:
				d = digits % 10
				if d == 0:
					pass
				elif place == 2:
					add = [ones[d - 1]] + ['Hundred'] + add
				elif place == 1:
					add = [decs[d - 2]] + add
				elif place == 0:
					add = [ones[d - 1]] + add
				
				digits //= 10
				place += 1
			
			if add and thous >= 0:
				add = add + [thousands[thous]]
			
			english = add + english
			num //= 1000
			thous += 1
			
		return ' '.join(english)
