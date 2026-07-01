class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> target = new HashMap<>();
        for (char c : t.toCharArray()) {
            target.put(c, target.getOrDefault(c, 0) + 1);
        }
        int required = target.size();

        Map<Character, Integer> window = new HashMap<>();
        int formed = 0;
        int l = 0;

        int res_len = Integer.MAX_VALUE, res_l = 0, res_r = 0;

        for (int r = 0; r < s.length(); r++) {
            char rc = s.charAt(r);
            window.put(rc, window.getOrDefault(rc, 0) + 1);

            if (target.containsKey(rc) && window.get(rc) == target.get(rc)) {
                formed++;
            }

            while (formed == required) {
                if (r - l + 1 < res_len) {
                    res_len = r - l + 1;
                    res_l = l;
                    res_r = r;
                }

                char lc = s.charAt(l);
                window.put(lc, window.get(lc) - 1);
                if (target.containsKey(lc) && window.get(lc) < target.get(lc)) {
                    formed--;
                }
                l++;
            }
        }
        
        if (res_len == Integer.MAX_VALUE) return "";
        return s.substring(res_l, res_r + 1);
    }
}
