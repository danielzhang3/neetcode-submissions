class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        PriorityQueue<int[]> max_heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[0], a[0])
        );
        for (char c : count.keySet()) {
            int cnt = count.get(c);
            max_heap.offer(new int[]{cnt, c});
        }
        int prev_cnt = 0;
        char prev_ch = '\0';
        StringBuilder res = new StringBuilder();

        while (!max_heap.isEmpty() || prev_cnt > 0) {
            if (max_heap.isEmpty()) return "";

            int[] pair = max_heap.poll();
            int cnt = pair[0];
            char ch = (char) pair[1];

            cnt--;
            res.append(ch);

            if (prev_cnt > 0) max_heap.offer(new int[]{prev_cnt, prev_ch});
            prev_cnt = cnt;
            prev_ch = ch;
        }
        
        return res.toString();
    }
}