class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int curr_sum = 0;
        int l = 0;
        int res = Integer.MAX_VALUE;

        for (int r = 0; r < nums.length; r++) {
            curr_sum += nums[r];

            while (curr_sum >= target) {
                if (r - l + 1 < res) {
                    res = r - l + 1;
                }
                curr_sum -= nums[l];
                l++;
            }
        }
        
        if (res == Integer.MAX_VALUE) return 0;
        return res;
    }
}