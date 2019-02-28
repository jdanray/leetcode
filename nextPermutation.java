// https://leetcode.com/problems/next-permutation/

class Solution {
	public void swap(int[] nums, int i, int j) {
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp; 
	}

	public void nextPermutation(int[] nums) {
		int i;
		int j;

	 	for (i = nums.length - 2; i >= 0 && nums[i] >= nums[i + 1]; i--);

		for (j = nums.length - 1; i >= 0 && j >= 0 && nums[j] <= nums[i]; j--);

		if (i >= 0 && j >= 0) 
			swap(nums, i, j);

		i++;
		j = nums.length - 1;
		while (i < j) {
			swap(nums, i, j);
			i++;
			j--;
		}
	}
}
