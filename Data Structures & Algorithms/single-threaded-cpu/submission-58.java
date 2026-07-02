class Solution {
    public int[] getOrder(int[][] tasks) {
        int[][] newTasks = new int[tasks.length][3];
        for (int i = 0; i < tasks.length; i++) {
            newTasks[i][0] = tasks[i][0];
            newTasks[i][1] = tasks[i][1];
            newTasks[i][2] = i;
        }
        Arrays.sort(newTasks, (a, b) -> Integer.compare(a[0], b[0]));

        PriorityQueue<int[]> available = new PriorityQueue<>(
            (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1])
        );

        int i = 0;
        int time = 0;
        List<Integer> res = new ArrayList<>();

        while (i < newTasks.length || !available.isEmpty()) {
            while (i < newTasks.length && newTasks[i][0] <= time) {
                available.offer(new int[]{newTasks[i][1], newTasks[i][2]});
                i++;
            }

            if (available.isEmpty()) {
                time = newTasks[i][0];
            }
            else {
                int[] pair = available.poll();
                int proc = pair[0];
                int idx = pair[1];

                time += proc;
                res.add(idx);
            }
        }

        int[] result = new int[res.size()];
        for (int j = 0; j < result.length; j++) {
            result[j] = res.get(j);
        }
        return result;
    }
}