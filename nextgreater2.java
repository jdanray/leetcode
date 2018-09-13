// https://leetcode.com/problems/next-greater-element-ii/description/

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int j = i;
            do {
                j++;
                if (j >= nums.length)
                    j = 0;
            } while (nums[j] <= nums[i] && j != i);
            if (j == i)
                res[i] = -1;
            else
                res[i] = nums[j];
        }
        return res;        
    }
}
