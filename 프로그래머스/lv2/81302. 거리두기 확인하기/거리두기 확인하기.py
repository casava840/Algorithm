from collections import deque

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer

def bfs(place):
    starts = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                starts.append([i, j])
    for start in starts:
        que = deque([start])
        visited = [[0 for col in range(5)] for row in range(5)]
        visited[start[0]][start[1]] = 1
        distance = [[0 for col in range(5)] for row in range(5)]
        while que:
            y, x = que.popleft()
            for i in range(4):
                dx = [-1, 1, 0, 0]
                dy = [0, 0, -1, 1]
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0<= new_x and new_x<5 and 0<= new_y and new_y<5 and visited[new_y][new_x] == 0:
                    if place[new_y][new_x] == 'O':
                        visited[new_y][new_x] = 1
                        distance[new_y][new_x] = distance[y][x] + 1
                        que.append([new_y,new_x])
                    if place[new_y][new_x] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1