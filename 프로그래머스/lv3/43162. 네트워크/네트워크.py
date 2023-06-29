def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for com in range(n):
        if visited[com] == 0:
            DFS(n, computers, com, visited)
            answer += 1 #방문안한 컴퓨터는 1개의 네트워크를 보장하므로 +1
    
    return answer

def DFS(n, computers, com, visited):
    visited[com] = 1
    stack = []
    stack.append(com)
    while len(stack) != 0:
        com = stack.pop(-1)
        for another_com in range(n):
            if com != another_com and computers[com][another_com] == 1:
                if visited[another_com] == 0:
                    stack.append(another_com)
                    visited[another_com] = 1