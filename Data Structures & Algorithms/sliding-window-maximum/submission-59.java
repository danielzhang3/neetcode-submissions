class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque<>();
        int l = 0;
        List<Integer> res = new ArrayList<>();

        for (int r = 0; r < nums.length; r++) {
            while (!q.isEmpty() && nums[q.peekLast()] < nums[r]) {
                q.pollLast();
            }
            q.offerLast(r);

            if (l > q.peekFirst()) {
                q.pollFirst();
            }

            if (r + 1 >= k) {
                res.add(nums[q.peekFirst()]);
                l++;
            }
        }

        int[] result = new int[res.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = res.get(i);
        }
        return result;
    }
}
