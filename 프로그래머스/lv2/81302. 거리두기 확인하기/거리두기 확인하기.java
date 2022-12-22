import java.util.*;

class Solution {
    public static int[] solution(String[][] places) {
        int[] answer = new int[5];
        for (int i = 0; i < 5; i++) {
            answer[i] = bfs(places[i]);
        }
        return answer;
    }
    public static int bfs(String[] place){
        List<int[]> starts = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (place[i].charAt(j) == 'P') {
                    starts.add(new int[] {i, j});
                }
            }
        }
        for (int[] start:starts) {
            Queue<int[]> queue = new LinkedList<>();
            queue.add(start);
            int[][] visited = new int[5][5];
            int[][] distance = new int[5][5];
            visited[start[0]][start[1]] = 1;
            while (!queue.isEmpty()) {
                int[] temp = queue.poll();
                int x = temp[1];
                int y = temp[0];
                int[] dx = {-1, 1, 0, 0};
                int[] dy = {0, 0, -1, 1};
                for (int i = 0; i < 4; i++) {
                    int newX = x + dx[i];
                    int newY = y + dy[i];
                    if (0<=newX && newX<=4 && 0<=newY && newY<=4 && visited[newY][newX] == 0) {
                        if (place[newY].charAt(newX) == 'O') {
                            visited[newY][newX] = 1;
                            distance[newY][newX] = distance[y][x] + 1;
                            queue.add(new int[] {newY, newX});
                        }
                        if (place[newY].charAt(newX) == 'P' && distance[y][x] <= 1) {
                            return 0;
                        }
                    }
                }
            }
        }

        return 1;
    }
}