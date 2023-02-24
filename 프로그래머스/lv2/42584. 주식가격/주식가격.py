from collections import deque

def solution(prices):
    answer = []
    deq = deque(prices)
    while len(deq) > 2:
        price = deq.popleft()
        flag = True
        for i, d in enumerate(deq):
            if price > d:
                flag = False
                answer.append(i+1)
                break
        if flag:
            answer.append(len(deq))
    answer.extend([1,0])
            
    return answer 