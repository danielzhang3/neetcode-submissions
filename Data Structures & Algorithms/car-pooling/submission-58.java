class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        Arrays.sort(trips, (a, b) -> Integer.compare(a[1], b[1]));
        PriorityQueue<int[]> current = new PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0])
        );
        int current_load = 0;

        for (int[] trip : trips) {
            int num = trip[0], start = trip[1], end = trip[2];
            while (!current.isEmpty() && current.peek()[0] <= start) {
                int[] pair = current.poll();
                current_load -= pair[1];
            }

            current.offer(new int[]{end, num});
            current_load += num;

            if (current_load > capacity) return false;
        }

        return true;
    }
}