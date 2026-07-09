class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int n = arr.length;
        int low = 0, high = n - k;

        while (low < high) {
            int m = low + (high - low) / 2;
            int left_gap = x - arr[m];
            int right_gap = arr[m + k] - x;

            if (left_gap > right_gap) {
                low = m + 1;
            }
            else {
                high = m;
            }
        }
        
        List<Integer> res = new ArrayList<>();
        for (int i = low; i < low + k; i++) {
            res.add(arr[i]);
        }
        return res;
    }
}