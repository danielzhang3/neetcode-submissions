class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length > n - 1) {
            return false;
        }
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        Set<Integer> visited = new HashSet<>();
        return dfs(0, -1, adj, visited) && visited.size() == n;

    }
    public boolean dfs(int node, int par, List<List<Integer>> adj, Set<Integer> visited) {
        if (visited.contains(node)) return false;

        visited.add(node);
        for (int nei : adj.get(node)) {
            if (nei == par) continue;
            if (dfs(nei, node, adj, visited) == false) return false;
        }
        return true;
    }
}
