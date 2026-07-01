class Solution {
    public String foreignDictionary(String[] words) {
        Map<Character, Set<Character>> graph = new HashMap<>();
        Map<Character, Integer> indeg = new HashMap<>();
        for (String word : words) {
            for (char c : word.toCharArray()) {
                indeg.put(c, 0);
            }
        }

        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i + 1];
            if (w1.length() > w2.length() && w1.startsWith(w2)) return "";

            int n = Math.min(w1.length(), w2.length());
            for (int j = 0; j < n; j++) {
                char c1 = w1.charAt(j), c2 = w2.charAt(j);

                if (c1 != c2) {
                    Set<Character> nbrs = graph.computeIfAbsent(c1, k -> new HashSet<>());
                    if (nbrs.add(c2)) {
                        indeg.put(c2, indeg.get(c2) + 1);
                    }
                    break;
                }
            }
        }

        Deque<Character> q = new ArrayDeque<>();
        StringBuilder res = new StringBuilder();
        for (char c : indeg.keySet()) {
            if (indeg.get(c) == 0) {
                q.offerLast(c);
            }
        }

        while (!q.isEmpty()) {
            char cur = q.pollFirst();
            res.append(cur);

            for (char nei : graph.getOrDefault(cur, Collections.emptySet())) {
                indeg.put(nei, indeg.get(nei) - 1);
                if (indeg.get(nei) == 0) {
                    q.offerLast(nei);
                }
            }
        }

        if (res.length() != indeg.size()) return "";
        return res.toString();
    }
}
