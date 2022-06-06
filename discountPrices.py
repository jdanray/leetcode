# https://leetcode.com/problems/apply-discount-to-prices/ 

class Solution(object):
	def discountPrices(self, sentence, discount):
		words = sentence.split()
		res = []
		for w in words:
			if w[0] == '$' and w[1:].isnumeric():
				price = float(w[1:])
				price -= price * discount / 100
				res.append('${:.2f}'.format(price))
			else:
				res.append(w)

		return ' '.join(res)
