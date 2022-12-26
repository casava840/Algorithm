from collections import deque
import math

def solution(progresses, speeds):
    days = []
    answer = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    que = deque(days)
    while que:
        count = 0
        if que[0] > 0:
            temp = que[0]
            for i in range(len(que)):
                que[i] -= temp
        while que[0] <= 0:
            que.popleft()
            count += 1
            if len(que) == 0:
                break
        answer.append(count)
    return answer