def solution(dirs):
    answer = 0
    visited = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]
    x = 5
    y = 5
    #역방향일때도 고려해서 visited를 적어야한다.
    for dir in dirs:
        if dir == 'U' and y != 10:
            if visited[y][x][0] == 0:
                answer += 1
                visited[y][x][0] = 1
                visited[y+1][x][1] = 1
            y += 1
        elif dir == 'D' and y != 0:
            if visited[y][x][1] == 0:
                answer += 1
                visited[y][x][1] = 1
                visited[y-1][x][0] = 1
            y -= 1
        elif dir == 'R' and x != 10:
            if visited[y][x][2] == 0:
                answer += 1
                visited[y][x][2] = 1
                visited[y][x+1][3] = 1
            x += 1
        elif dir == 'L' and x != 0:
            if visited[y][x][3] == 0:
                answer += 1
                visited[y][x][3] = 1
                visited[y][x-1][2] = 1
            x -= 1
    return answer