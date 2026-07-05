class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        boolean[] visited = new boolean[n];
        int res = 0;

        for (int node = 0; node < n; node++) {
            if (visited[node] == false) {
                visited[node] = true;
                dfs(node, adj, visited);
                res++;
            }
        }

        return res;
    }
    public void dfs(int node, List<List<Integer>> adj, boolean[] visited) {
        for (int nei : adj.get(node)) {
            if (visited[nei] == false) {
                visited[nei] = true;
                dfs(nei, adj, visited);
            }
        }
    }
}
