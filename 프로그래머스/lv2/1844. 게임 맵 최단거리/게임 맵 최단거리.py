from collections import deque

def solution(maps):
    # goal = n-1,m-1
    n = len(maps[0])
    m = len(maps)
    visited = [[0 for _ in range(n)] for _ in range(m)]
    visited[0][0] = 1
    answer = []
    def BFS(x, y, visited, maps):
        distance = {(0,0):1}
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        queue = deque([(x,y)])
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                    if nx == n-1 and ny == m-1:
                        return distance[x,y] + 1
                    visited[ny][nx] = 1
                    queue.append((nx,ny))
                    distance[(nx,ny)] = distance[(x,y)] + 1
        return -1
    
    return BFS(0, 0, visited, maps)