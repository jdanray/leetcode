# https://leetcode.com/problems/maximum-swap/

class Solution:
	def targmax(self, num):
		om, oldmaxi = -1, 0
		m, maxi = -1, 0
		h, head = 0, 0
		t, targ = -1, 0

		while num > 0:
			head = num % 10

			if head < maxi:
				t, targ = h, head
			elif head > maxi:
				if t > m:
					om, oldmaxi = m, maxi
				m, maxi = h, head

			num //= 10
			h += 1

		if t < m:
			m, maxi = om, oldmaxi

		return m, maxi, t, targ

	def assemble(self, num, m, maxi, t, targ):
		rnum = 0
		i = 0
		d = 1
		while num > 0:
			if i == t:
				rnum += d * maxi
			elif i == m:
				rnum += d * targ
			else:
				rnum += d * (num % 10)
				
			num //= 10
			d *= 10
			i += 1

		return rnum

	def maximumSwap(self, num):
		return self.assemble(num, *self.targmax(num))
