// https://leetcode.com/problems/sequential-digits/ 

/*
 * You can find my solution to this problem at sequentialDigits.py.
 * After I solve a problem, I like to examine other people's solutions.
 * I found a very nice solution here:
 * https://leetcode.com/problems/sequential-digits/discuss/853592/Python-Solution-using-queue-explained
 * I wanted to preserve that solution, and I wanted to rewrite it in Java:
 */

class Solution {
	public List<Integer> sequentialDigits(int low, int high) {
		Queue<Integer> queue = new LinkedList<Integer>();
		for (int num = 1; num <= 9; num++) {
			queue.add(num);
		}

		List<Integer> res = new ArrayList<Integer>();
		while (!queue.isEmpty()) {
			int num = queue.poll();
			if (num >= low && num <= high) {
				res.add(num);
			}

			int last = num % 10;
			if (last < 9) {
				queue.add(num * 10 + last + 1);
			}
		}

		return res;
	}
}
