class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> count = new HashMap<>();
        for (char task : tasks) {
            count.put(task, count.getOrDefault(task, 0) + 1);
        }

        PriorityQueue<Integer> max_heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b, a)
        );
        for (char task : count.keySet()) {
            int cnt = count.get(task);
            max_heap.offer(cnt);
        }

        Deque<int[]> q = new ArrayDeque<>();
        int time = 0;

        while (!max_heap.isEmpty() || !q.isEmpty()) {
            time++;

            if (max_heap.isEmpty()) {
                time = q.peekFirst()[1];
            }
            else {
                int cnt = max_heap.poll() - 1;
                if (cnt > 0) {
                    q.offerLast(new int[]{cnt, time + n});
                }
            }
            if (!q.isEmpty() && time == q.peekFirst()[1]) {
                max_heap.offer(q.pollFirst()[0]);
            }
        }
        
        return time;
    }
}
