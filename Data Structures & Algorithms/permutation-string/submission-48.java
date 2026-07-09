class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character, Integer> target = new HashMap<>();
        for (char c : s1.toCharArray()) {
            target.put(c, target.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> window = new HashMap<>();
        int l = 0;

        for (int r = 0; r < s2.length(); r++) {
            char rc = s2.charAt(r);
            window.put(rc, window.getOrDefault(rc, 0) + 1);

            if (r - l + 1 > s1.length()) {
                char lc = s2.charAt(l);
                window.put(lc, window.get(lc) - 1);
                if (window.get(lc) == 0) {
                    window.remove(lc);
                }
                l++;
            }

            if (target.equals(window)) return true;
        }
        
        return false;
    }
}
