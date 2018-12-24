# https://leetcode.com/problems/lemonade-change/

"""
You can get a 5, 10, or 20. Consider each case in turn:

Case 1: You get a 5

No problem. You don't have to make change. Increment the number of fives you have (nfives) and move on.

Case 2: You get a 10

You have to give the customer a 5 back. Check whether nfives is greater than 0. If it isn't, then you can't make change; return false. If it is, then decrement nfives and increment ntens.

Case 3: You get a 20

Here is where things get tricky. You can make change for a 20 if [i] you have 3 fives, or [ii] you have 1 five and 1 ten. But now let's say that nfives >= 3 and ntens >= 1. So, now you have a choice: You can make change for the 20 (a) with 3 fives or (b) with 1 five and 1 ten. Do you choose (a) or (b)?

Let's say that you choose (a). So, you decrement nfives by 3. Then nfives >= 0 and ntens >= 1.

Now, the next bill could be a 5, 10, or 20. Consider each case in turn:

	Case 3.A.1: You get a 5

	No problem--you don't have to make change.

	Case 3.A.2: You get a 10

	You have nfives >= 0. That means that nfives could equal 0. So, you might not be able to make change.

	Case 3.A.3: You get a 20

	You have fives >= 0 and tens >= 1. 
	Whether you make change (a) with 3 fives or (b) with 1 five and 1 ten, you need at least 1 five to make change. Since fives >= 0, it's possible that fives == 0. So, you may or may not be able to make change.

Now let's say that you choose (b). So, you decrement nfives by 1 and ntens by 1. Then nfives >= 2 and ntens >= 0. And the next bill could be a 5, 10, or 20:

	Case 3.B.1: You get a 5
	
	No problem.

	Case 3.B.2: You get a 10

	You have fives >= 2. You can definitely make change.

	Case 3.B.3: You get a 20

	You have fives >= 2 and tens >= 0. 
	Since fives >= 2, it's possible that fives >= 3, but it's also possible that fives < 3. So, you may or may not be able to make change with 3 fives.
	Since tens >= 0, it's possible that tens == 0. So, you may or may not be able to make change with a 10 and a 5.

So--in general--it's better to choose (b). Whether you choose (a) or (b), the case where you get a 5 or a 20 is the same: If you get a 5, there's no problem; if you get a 20, you may or may not be able to make change. But in the case where you get a 10, it's better to have chosen (b): Then you can definitely make change, whereas you may not be able to make change if you chose (a).

So, this analysis shows that it's generally better to choose (b). But say that you choose (b) and then later you arrive at a situation where you can't make change. Is it possible that if you had chosen (a) instead of (b), you would be able to make change?

The following analysis will resolve this issue. It will show that the answer to the above question is 'No'.

In the worrisome scenario, I chose (b) and now I can't make change. If I can't make change, then I must have received a 10 or a 20, because making change for a 5 just isn't an issue at all. So, let's consider both of these cases in turn:

Case A: I get a 10, and I can't make change

If I can't make change for a 10, that means that nfives == 0. So, if I had chosen (a) instead of (b), would nfives > 0?

No! If chose (b), then I handed over 1 five. In contrast, if I had chosen (a), then I handed over 3 fives! So, I'd have even fewer fives than I have now! Choosing (a) wouldn't have helped me AT ALL. This case is resolved.

Case B: I get a 20 and I can't make change

If I can't make change for a 20, then !(nfives > 0 and ntens > 0) and !(nfives >= 3). Assuming that we can't have a negative number of any bill, we can rewrite that as: (nfives == 0 or ntens == 0) and (nfives < 3). This condition holds if:

[i] nfives == 0, ntens == 0
[ii] nfives == 0, ntens > 0
[iii] 0 < nfives < 3, ntens > 0

In any case, nfives must equal either 0, 1, or 2. 

Now, let's say that, instead of choosing (b), I had chosen (a). Then I would have decremented nfives by 3 instead of by 1. So, nfives would equal -2, -1, or 0. But, in order to make change for a 20, I need at least 1 five! So, choosing (a) would NOT have saved me.

Now the analysis is done: You should ALWAYS choose (b) over (a). 
"""

class Solution(object):
	def lemonadeChange(self, bills):
		fives = 0
		tens = 0
		twenties = 0
		for b in bills:
			if b == 5:
				fives += 1
			elif b == 10:
				if fives > 0:
					fives -= 1
					tens += 1
				else:
					return False
			elif b == 20:
				if fives >= 1 and tens >= 1:
					fives -= 1
					tens -= 1
					twenties += 1
				elif fives >= 3:
					fives -= 3
					twenties += 1
				else:
					return False
		return True
