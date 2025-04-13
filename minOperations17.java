// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution {
	public int minOperations(int[] nums, int k) {
		return IntStream.of(nums).sum() % k;
	}
}