class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int[][] projects = new int[capital.length][2];
        for (int i = 0; i < capital.length; i++) {
            projects[i][0] = capital[i];
            projects[i][1] = profits[i];
        }
        Arrays.sort(projects, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> max_prof_heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b, a)
        );
        int i = 0;

        for (int j = 0; j < k; j++) {
            while (i < projects.length && projects[i][0] <= w) {
                max_prof_heap.offer(projects[i][1]);
                i++;
            }

            if (max_prof_heap.isEmpty()) {
                break;
            }
            else {
                w += max_prof_heap.poll();
            }
        } 

        return w;
    }
}