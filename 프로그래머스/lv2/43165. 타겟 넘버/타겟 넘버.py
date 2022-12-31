def solution(numbers, target):
    LENGTH = len(numbers)
    answer = 0
    def dfs(cur,result):
        if cur == LENGTH:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            dfs(cur+1, result+numbers[cur])
            dfs(cur+1, result-numbers[cur])
    dfs(0,0)
    return answer