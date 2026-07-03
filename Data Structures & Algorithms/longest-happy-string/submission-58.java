class Solution {
    public String longestDiverseString(int a, int b, int c) {
        PriorityQueue<int[]> max_heap = new PriorityQueue<>(
            (x, y) -> Integer.compare(y[0], x[0])
        );
        if (a > 0) max_heap.offer(new int[]{a, 'a'});
        if (b > 0) max_heap.offer(new int[]{b, 'b'});
        if (c > 0) max_heap.offer(new int[]{c, 'c'});

        StringBuilder res = new StringBuilder();

        while (!max_heap.isEmpty()) {
            int[] pair = max_heap.poll();
            int cnt = pair[0];
            char ch = (char) pair[1];

            int n = res.length();
            if (n >= 2 && res.charAt(n - 1) == ch && res.charAt(n - 2) == ch) {
                if (max_heap.isEmpty()) break;

                int[] pair2 = max_heap.poll();
                int cnt2 = pair2[0];
                char ch2 = (char) pair2[1];

                cnt2--;
                res.append(ch2);

                if (cnt2 > 0) max_heap.offer(new int[]{cnt2, ch2});
                max_heap.offer(new int[]{cnt, ch});
            }
            else {
                cnt--;
                res.append(ch);
                if (cnt > 0) max_heap.offer(new int[]{cnt, ch});
            }
        }
        
        return res.toString();
    }
}