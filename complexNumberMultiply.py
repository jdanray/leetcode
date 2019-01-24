# https://leetcode.com/problems/complex-number-multiplication/description/

class Solution:
	def complexNumberMultiply(self, A, B):
		def parse(M):
			i = M.find('+')
            
			a = int(M[:i])
			b = int(M[i + 1:-1])
            
			return (a, b) 

		a, b = parse(A)
		c, d = parse(B)
        
		e = a * c - b * d
		f = b * c + a * d
        
		return str(e) + "+" + str(f) + "i"

class Solution:
	def complexNumberMultiply(self, A, B):
		def parse(M):
			i = M.find('+')
			j = M.find('i')

			a = int(M[:i])
			b = int(M[i + 1:j])

			return (a, b)

		def mult(M, N):
			a, b = M
			c, d = N

			e = (a * c - b * d)
			f = (b * c + a * d)

			return (e, f)

		def compose(e, f):
			return str(e) + "+" + str(f) + "i"

		return compose(*mult(parse(A), parse(B)))
